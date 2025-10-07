"""
Main pipeline orchestrator for Product Intelligence Engine.
Runs the complete ETL pipeline from scraping to analysis.
"""

import sys
import argparse
from pathlib import Path
from datetime import datetime

from config.config import RAW_DATA_DIR, PROCESSED_DATA_DIR
from utils import setup_logging, get_logger, DataHandler
from scripts.scraper import PlayStoreScraper
from scripts.process_llm import FeedbackProcessor

logger = get_logger(__name__)


class PIEnginePipeline:
    """Orchestrates the complete Product Intelligence Engine pipeline."""
    
    def __init__(self, app_id: str = None, max_reviews: int = None):
        """
        Initialize the pipeline.
        
        Args:
            app_id: Google Play Store app ID
            max_reviews: Maximum number of reviews to process
        """
        self.app_id = app_id
        self.max_reviews = max_reviews
        self.scraper = None
        self.processor = None
        
    def run_scraping(self) -> Path:
        """
        Run the scraping phase.
        
        Returns:
            Path to the scraped data file
        """
        logger.info("=" * 60)
        logger.info("📥 PHASE 1: DATA COLLECTION")
        logger.info("=" * 60)
        
        try:
            self.scraper = PlayStoreScraper(
                app_id=self.app_id,
                max_reviews=self.max_reviews
            )
            
            reviews_data = self.scraper.run(save_file=True)
            
            if not reviews_data:
                raise Exception("No reviews collected")
            
            # Get the latest file
            raw_files = list(RAW_DATA_DIR.glob("*.csv"))
            latest_file = max(raw_files, key=lambda x: x.stat().st_ctime)
            
            logger.info(f"✅ Phase 1 completed: {len(reviews_data)} reviews collected")
            return latest_file
            
        except Exception as e:
            logger.error(f"❌ Scraping phase failed: {e}")
            raise
    
    def run_processing(self, input_file: Path) -> Path:
        """
        Run the LLM processing phase.
        
        Args:
            input_file: Path to raw data file
            
        Returns:
            Path to processed data file
        """
        logger.info("\n" + "=" * 60)
        logger.info("🤖 PHASE 2: LLM PROCESSING & CLASSIFICATION")
        logger.info("=" * 60)
        
        try:
            self.processor = FeedbackProcessor()
            
            df_processed = self.processor.run(
                input_file=input_file.name,
                output_file=None
            )
            
            if df_processed.empty:
                raise Exception("Processing returned empty dataframe")
            
            # Get the latest processed file
            processed_files = list(PROCESSED_DATA_DIR.glob("*.csv"))
            latest_file = max(processed_files, key=lambda x: x.stat().st_ctime)
            
            logger.info(f"✅ Phase 2 completed: {len(df_processed)} reviews processed")
            return latest_file
            
        except Exception as e:
            logger.error(f"❌ Processing phase failed: {e}")
            raise
    
    def run_analysis(self, processed_file: Path):
        """
        Run analysis and generate insights.
        
        Args:
            processed_file: Path to processed data file
        """
        logger.info("\n" + "=" * 60)
        logger.info("📊 PHASE 3: ANALYSIS & INSIGHTS")
        logger.info("=" * 60)
        
        try:
            df = DataHandler.load_from_csv(processed_file)
            
            if df is None or df.empty:
                raise Exception("Failed to load processed data")
            
            # Generate insights
            self._generate_insights(df)
            
            logger.info("✅ Phase 3 completed: Analysis generated")
            
        except Exception as e:
            logger.error(f"❌ Analysis phase failed: {e}")
            raise
    
    def _generate_insights(self, df):
        """Generate and display key insights from processed data."""
        
        print("\n" + "=" * 60)
        print("📈 KEY INSIGHTS")
        print("=" * 60)
        
        # Overall stats
        print(f"\n📊 Overall Statistics:")
        print(f"   Total Reviews: {len(df)}")
        print(f"   Average Rating: {df['rating'].mean():.2f}/5.0")
        
        # Category breakdown
        if 'category' in df.columns:
            print(f"\n🗂️  Top Categories:")
            category_counts = df['category'].value_counts()
            for i, (cat, count) in enumerate(category_counts.head(5).items(), 1):
                pct = (count / len(df)) * 100
                print(f"   {i}. {cat}: {count} ({pct:.1f}%)")
        
        # Sentiment analysis
        if 'sentiment' in df.columns:
            print(f"\n😊 Sentiment Distribution:")
            sentiment_counts = df['sentiment'].value_counts()
            for sent in ['positive', 'neutral', 'negative']:
                count = sentiment_counts.get(sent, 0)
                pct = (count / len(df)) * 100 if len(df) > 0 else 0
                emoji = "😊" if sent == "positive" else ("😐" if sent == "neutral" else "😞")
                print(f"   {emoji} {sent.title()}: {count} ({pct:.1f}%)")
        
        # Priority issues
        if 'priority' in df.columns:
            print(f"\n⚠️  Priority Distribution:")
            priority_counts = df['priority'].value_counts()
            for pri in ['high', 'medium', 'low']:
                count = priority_counts.get(pri, 0)
                pct = (count / len(df)) * 100 if len(df) > 0 else 0
                emoji = "🔴" if pri == "high" else ("🟡" if pri == "medium" else "🟢")
                print(f"   {emoji} {pri.title()}: {count} ({pct:.1f}%)")
        
        # Top issues (high priority)
        if 'priority' in df.columns and 'summary' in df.columns:
            high_priority = df[df['priority'] == 'high']
            if not high_priority.empty:
                print(f"\n🔴 Top High-Priority Issues:")
                for i, row in enumerate(high_priority.head(5).itertuples(), 1):
                    print(f"   {i}. [{row.category}] {row.summary[:70]}...")
        
        # Rating distribution
        print(f"\n⭐ Rating Distribution:")
        rating_counts = df['rating'].value_counts().sort_index(ascending=False)
        for rating, count in rating_counts.items():
            pct = (count / len(df)) * 100
            stars = "⭐" * int(rating)
            bar = "█" * int(pct / 2)
            print(f"   {stars} ({rating}): {bar} {count} ({pct:.1f}%)")
        
        print("\n" + "=" * 60)
    
    def run_full_pipeline(self):
        """Run the complete end-to-end pipeline."""
        start_time = datetime.now()
        
        logger.info("\n" + "=" * 70)
        logger.info("🚀 PRODUCT INTELLIGENCE ENGINE - FULL PIPELINE")
        logger.info("=" * 70)
        logger.info(f"⏰ Started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        
        try:
            # Phase 1: Scraping
            raw_file = self.run_scraping()
            
            # Phase 2: Processing
            processed_file = self.run_processing(raw_file)
            
            # Phase 3: Analysis
            self.run_analysis(processed_file)
            
            # Final summary
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()
            
            logger.info("\n" + "=" * 70)
            logger.info("✅ PIPELINE COMPLETED SUCCESSFULLY!")
            logger.info("=" * 70)
            logger.info(f"⏱️  Duration: {duration:.1f} seconds")
            logger.info(f"📁 Raw Data: {raw_file}")
            logger.info(f"📁 Processed Data: {processed_file}")
            logger.info("=" * 70)
            
            print("\n✨ Next steps:")
            print("   1. Open the processed CSV file in Excel/Google Sheets")
            print("   2. Import to Looker Studio for visualization")
            print("   3. Share insights with your product team!")
            
        except Exception as e:
            logger.error(f"\n❌ Pipeline failed: {e}")
            sys.exit(1)


def main():
    """Main entry point with CLI support."""
    parser = argparse.ArgumentParser(
        description="Product Intelligence Engine - Automated Review Analysis Pipeline"
    )
    
    parser.add_argument(
        '--app-id',
        type=str,
        help='Google Play Store app ID (e.g., com.unnes.myunnes)'
    )
    
    parser.add_argument(
        '--max-reviews',
        type=int,
        help='Maximum number of reviews to process'
    )
    
    parser.add_argument(
        '--scrape-only',
        action='store_true',
        help='Only run the scraping phase'
    )
    
    parser.add_argument(
        '--process-only',
        action='store_true',
        help='Only run the processing phase (requires existing raw data)'
    )
    
    args = parser.parse_args()
    
    # Setup logging
    setup_logging()
    
    # Initialize pipeline
    pipeline = PIEnginePipeline(
        app_id=args.app_id,
        max_reviews=args.max_reviews
    )
    
    # Run requested phases
    if args.scrape_only:
        pipeline.run_scraping()
    elif args.process_only:
        raw_files = list(RAW_DATA_DIR.glob("*.csv"))
        if not raw_files:
            logger.error("❌ No raw data files found. Run with --scrape-only first.")
            sys.exit(1)
        latest_file = max(raw_files, key=lambda x: x.stat().st_ctime)
        pipeline.run_processing(latest_file)
        processed_files = list(PROCESSED_DATA_DIR.glob("*.csv"))
        latest_processed = max(processed_files, key=lambda x: x.stat().st_ctime)
        pipeline.run_analysis(latest_processed)
    else:
        # Run full pipeline
        pipeline.run_full_pipeline()


if __name__ == "__main__":
    main()
