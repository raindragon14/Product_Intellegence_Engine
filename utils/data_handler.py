"""
Data handling utilities for Product Intelligence Engine.
Handles CSV operations, data validation, and cleaning.
"""

import pandas as pd
import logging
from pathlib import Path
from typing import List, Dict, Optional
from datetime import datetime

logger = logging.getLogger(__name__)


class DataHandler:
    """Handles data operations for reviews."""
    
    @staticmethod
    def save_to_csv(data: List[Dict], filepath: Path, mode: str = 'w') -> bool:
        """
        Save data to CSV file.
        
        Args:
            data: List of dictionaries containing review data
            filepath: Path to save the CSV file
            mode: Write mode ('w' for overwrite, 'a' for append)
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            df = pd.DataFrame(data)
            
            # Ensure parent directory exists
            filepath.parent.mkdir(parents=True, exist_ok=True)
            
            # Save to CSV
            if mode == 'a' and filepath.exists():
                df.to_csv(filepath, mode='a', header=False, index=False, encoding='utf-8-sig')
            else:
                df.to_csv(filepath, index=False, encoding='utf-8-sig')
            
            logger.info(f" Saved {len(data)} records to {filepath}")
            return True
            
        except Exception as e:
            logger.error(f" Error saving data to CSV: {e}")
            return False
    
    @staticmethod
    def load_from_csv(filepath: Path) -> Optional[pd.DataFrame]:
        """
        Load data from CSV file.
        
        Args:
            filepath: Path to the CSV file
            
        Returns:
            DataFrame or None if error occurs
        """
        try:
            if not filepath.exists():
                logger.warning(f" File not found: {filepath}")
                return None
            
            df = pd.read_csv(filepath, encoding='utf-8-sig')
            logger.info(f" Loaded {len(df)} records from {filepath}")
            return df
            
        except Exception as e:
            logger.error(f" Error loading CSV: {e}")
            return None
    
    @staticmethod
    def validate_reviews(df: pd.DataFrame, required_columns: List[str]) -> bool:
        """
        Validate review data structure.
        
        Args:
            df: DataFrame to validate
            required_columns: List of required column names
            
        Returns:
            bool: True if valid, False otherwise
        """
        try:
            missing_columns = set(required_columns) - set(df.columns)
            
            if missing_columns:
                logger.error(f" Missing columns: {missing_columns}")
                return False
            
            # Check for empty dataframe
            if df.empty:
                logger.warning(" DataFrame is empty")
                return False
            
            logger.info(" Data validation passed")
            return True
            
        except Exception as e:
            logger.error(f" Validation error: {e}")
            return False
    
    @staticmethod
    def clean_reviews(df: pd.DataFrame) -> pd.DataFrame:
        """
        Clean and preprocess review data.
        
        Args:
            df: DataFrame to clean
            
        Returns:
            Cleaned DataFrame
        """
        try:
            # Remove duplicates based on content
            original_count = len(df)
            df = df.drop_duplicates(subset=['content'], keep='first')
            logger.info(f"🧹 Removed {original_count - len(df)} duplicate reviews")
            
            # Remove empty reviews
            df = df[df['content'].notna() & (df['content'].str.strip() != '')]
            
            # Clean text
            df['content'] = df['content'].str.strip()
            
            # Convert date to datetime if it's a string
            if 'date' in df.columns and df['date'].dtype == 'object':
                df['date'] = pd.to_datetime(df['date'], errors='coerce')
            
            logger.info(f" Cleaned data: {len(df)} valid reviews remaining")
            return df
            
        except Exception as e:
            logger.error(f" Cleaning error: {e}")
            return df
    
    @staticmethod
    def get_summary_stats(df: pd.DataFrame) -> Dict:
        """
        Get summary statistics of the review data.
        
        Args:
            df: DataFrame to analyze
            
        Returns:
            Dictionary with summary statistics
        """
        try:
            stats = {
                "total_reviews": len(df),
                "date_range": {
                    "start": df['date'].min() if 'date' in df.columns else None,
                    "end": df['date'].max() if 'date' in df.columns else None
                },
                "rating_distribution": df['rating'].value_counts().to_dict() if 'rating' in df.columns else {},
                "average_rating": df['rating'].mean() if 'rating' in df.columns else None,
            }
            
            return stats
            
        except Exception as e:
            logger.error(f" Error generating stats: {e}")
            return {}
