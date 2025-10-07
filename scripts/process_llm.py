"""
LLM Processor for Product Intelligence Engine.
Uses Google Gemini API to classify and analyze user feedback.
"""

import time
import json
import logging
from typing import List, Dict, Optional
from datetime import datetime
import pandas as pd
import google.generativeai as genai
from tqdm import tqdm

from config.config import (
    GEMINI_API_KEY, 
    LLM_CONFIG, 
    FEEDBACK_CATEGORIES,
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    REVIEW_SCHEMA
)
from utils import DataHandler, get_logger

logger = get_logger(__name__)


class FeedbackProcessor:
    """Processes user feedback using LLM for classification and analysis."""
    
    def __init__(self):
        """Initialize the LLM processor."""
        if not GEMINI_API_KEY:
            raise ValueError("❌ GEMINI_API_KEY not found in environment variables!")
        
        # Configure Gemini API
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel(LLM_CONFIG['model'])
        self.temperature = LLM_CONFIG['temperature']
        self.max_retries = LLM_CONFIG['max_retries']
        self.retry_delay = LLM_CONFIG['retry_delay']
        
        logger.info(f"✅ Initialized Gemini model: {LLM_CONFIG['model']}")
    
    def create_classification_prompt(self, review_content: str, rating: int) -> str:
        """
        Create a structured prompt for review classification.
        
        Args:
            review_content: The review text
            rating: Star rating (1-5)
            
        Returns:
            Formatted prompt string
        """
        categories_str = json.dumps(FEEDBACK_CATEGORIES, indent=2, ensure_ascii=False)
        
        prompt = f"""Analisis ulasan pengguna berikut dan klasifikasikan dengan detail:

ULASAN: "{review_content}"
RATING: {rating}/5 ⭐

Berikan analisis dalam format JSON berikut:
{{
    "category": "kategori utama dari {list(FEEDBACK_CATEGORIES.keys())}",
    "subcategory": "sub-kategori yang spesifik",
    "sentiment": "positive/neutral/negative",
    "priority": "high/medium/low (berdasarkan severity dan impact)",
    "summary": "ringkasan singkat masalah/feedback dalam 1-2 kalimat",
    "keywords": ["kata kunci 1", "kata kunci 2", "kata kunci 3"]
}}

KATEGORI YANG TERSEDIA:
{categories_str}

ATURAN:
1. Pilih kategori yang paling sesuai
2. Sentiment harus konsisten dengan rating
3. Priority HIGH untuk bug kritis, crash, atau masalah keamanan
4. Summary harus dalam Bahasa Indonesia dan jelas
5. Keywords maksimal 5 kata yang relevan

Jawab HANYA dengan JSON, tanpa penjelasan tambahan."""

        return prompt
    
    def classify_review(self, review_content: str, rating: int) -> Optional[Dict]:
        """
        Classify a single review using LLM.
        
        Args:
            review_content: The review text
            rating: Star rating
            
        Returns:
            Classification results or None if failed
        """
        for attempt in range(self.max_retries):
            try:
                prompt = self.create_classification_prompt(review_content, rating)
                
                response = self.model.generate_content(
                    prompt,
                    generation_config=genai.types.GenerationConfig(
                        temperature=self.temperature,
                    )
                )
                
                # Parse JSON response
                result_text = response.text.strip()
                
                # Remove markdown code blocks if present
                if result_text.startswith('```json'):
                    result_text = result_text[7:]
                if result_text.startswith('```'):
                    result_text = result_text[3:]
                if result_text.endswith('```'):
                    result_text = result_text[:-3]
                
                result = json.loads(result_text.strip())
                
                # Validate required fields
                required_fields = ['category', 'subcategory', 'sentiment', 'priority', 'summary']
                if all(field in result for field in required_fields):
                    return result
                else:
                    logger.warning(f"⚠️ Missing fields in response: {result}")
                    
            except json.JSONDecodeError as e:
                logger.warning(f"⚠️ JSON parse error (attempt {attempt + 1}/{self.max_retries}): {e}")
                logger.debug(f"Response text: {response.text[:200]}")
                
            except Exception as e:
                logger.warning(f"⚠️ Classification error (attempt {attempt + 1}/{self.max_retries}): {e}")
            
            # Wait before retry
            if attempt < self.max_retries - 1:
                time.sleep(self.retry_delay)
        
        # Return default classification if all retries failed
        logger.error(f"❌ Failed to classify review after {self.max_retries} attempts")
        return self._get_default_classification(rating)
    
    def _get_default_classification(self, rating: int) -> Dict:
        """
        Get default classification for failed cases.
        
        Args:
            rating: Star rating
            
        Returns:
            Default classification dictionary
        """
        sentiment = "negative" if rating <= 2 else ("neutral" if rating == 3 else "positive")
        
        return {
            'category': 'Other',
            'subcategory': 'General Feedback',
            'sentiment': sentiment,
            'priority': 'low',
            'summary': 'Klasifikasi otomatis gagal',
            'keywords': []
        }
    
    def process_reviews(self, reviews_df: pd.DataFrame) -> pd.DataFrame:
        """
        Process multiple reviews in batch.
        
        Args:
            reviews_df: DataFrame with review data
            
        Returns:
            DataFrame with classification results added
        """
        logger.info(f"🤖 Processing {len(reviews_df)} reviews with LLM...")
        
        classifications = []
        
        for idx, row in tqdm(reviews_df.iterrows(), total=len(reviews_df), desc="Classifying reviews"):
            review_content = str(row.get('content', ''))
            rating = int(row.get('rating', 3))
            
            # Skip empty reviews
            if not review_content or review_content.strip() == '':
                classification = self._get_default_classification(rating)
            else:
                classification = self.classify_review(review_content, rating)
            
            classifications.append(classification)
            
            # Small delay to avoid rate limiting
            time.sleep(0.5)
        
        # Add classifications to dataframe
        for key in ['category', 'subcategory', 'sentiment', 'priority', 'summary', 'keywords']:
            reviews_df[key] = [c.get(key, '') for c in classifications]
        
        logger.info("✅ Classification completed!")
        return reviews_df
    
    def save_processed_data(self, df: pd.DataFrame, filename: str = None) -> bool:
        """
        Save processed reviews to CSV.
        
        Args:
            df: DataFrame with processed data
            filename: Output filename
            
        Returns:
            bool: Success status
        """
        try:
            if not filename:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"processed_reviews_{timestamp}.csv"
            
            filepath = PROCESSED_DATA_DIR / filename
            
            # Select only relevant columns
            output_columns = REVIEW_SCHEMA['processed_columns'] + ['keywords']
            available_columns = [col for col in output_columns if col in df.columns]
            
            df_output = df[available_columns]
            success = DataHandler.save_to_csv(df_output.to_dict('records'), filepath)
            
            if success:
                logger.info(f"💾 Processed data saved to: {filepath}")
            
            return success
            
        except Exception as e:
            logger.error(f"❌ Error saving processed data: {e}")
            return False
    
    def run(self, input_file: str, output_file: str = None) -> pd.DataFrame:
        """
        Run the complete processing pipeline.
        
        Args:
            input_file: Path to raw reviews CSV
            output_file: Path for output file (optional)
            
        Returns:
            Processed DataFrame
        """
        logger.info("=" * 60)
        logger.info("🤖 Starting LLM Processing Pipeline")
        logger.info("=" * 60)
        
        # Load data
        input_path = RAW_DATA_DIR / input_file
        df = DataHandler.load_from_csv(input_path)
        
        if df is None or df.empty:
            logger.error("❌ Failed to load data or data is empty")
            return pd.DataFrame()
        
        # Validate data
        if not DataHandler.validate_reviews(df, REVIEW_SCHEMA['required_columns']):
            logger.error("❌ Data validation failed")
            return pd.DataFrame()
        
        # Clean data
        df = DataHandler.clean_reviews(df)
        
        # Process with LLM
        df_processed = self.process_reviews(df)
        
        # Save results
        self.save_processed_data(df_processed, output_file)
        
        # Display summary
        self._display_summary(df_processed)
        
        logger.info("=" * 60)
        logger.info("✅ Processing pipeline completed!")
        logger.info("=" * 60)
        
        return df_processed
    
    def _display_summary(self, df: pd.DataFrame):
        """Display processing summary statistics."""
        logger.info("\n📊 PROCESSING SUMMARY:")
        logger.info(f"   Total reviews processed: {len(df)}")
        
        if 'category' in df.columns:
            logger.info("\n   Category Distribution:")
            for cat, count in df['category'].value_counts().head(5).items():
                logger.info(f"      {cat}: {count}")
        
        if 'sentiment' in df.columns:
            logger.info("\n   Sentiment Distribution:")
            for sent, count in df['sentiment'].value_counts().items():
                logger.info(f"      {sent}: {count}")
        
        if 'priority' in df.columns:
            logger.info("\n   Priority Distribution:")
            for pri, count in df['priority'].value_counts().items():
                logger.info(f"      {pri}: {count}")


def main():
    """Main entry point for LLM processor."""
    from utils import setup_logging
    setup_logging()
    
    # Get the latest raw data file
    import os
    raw_files = list(RAW_DATA_DIR.glob("*.csv"))
    
    if not raw_files:
        logger.error("❌ No raw data files found in data/raw/")
        logger.info("💡 Please run scraper.py first to collect reviews")
        return
    
    # Use the most recent file
    latest_file = max(raw_files, key=os.path.getctime)
    logger.info(f"📂 Using input file: {latest_file.name}")
    
    # Initialize and run processor
    processor = FeedbackProcessor()
    df_processed = processor.run(latest_file.name)
    
    if not df_processed.empty:
        print(f"\n✅ Success! Processed {len(df_processed)} reviews")
        print(f"📁 Output saved to: {PROCESSED_DATA_DIR}")


if __name__ == "__main__":
    main()
