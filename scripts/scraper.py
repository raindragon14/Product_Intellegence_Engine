"""
Google Play Store Scraper for Product Intelligence Engine.
Collects user reviews from Google Play Store apps.
"""

import time
import logging
from typing import List, Dict, Optional
from datetime import datetime
from google_play_scraper import app, reviews, Sort
from tqdm import tqdm

from config.config import SCRAPER_CONFIG, RAW_DATA_DIR
from utils import DataHandler, get_logger

logger = get_logger(__name__)


class PlayStoreScraper:
    """Scrapes reviews from Google Play Store."""
    
    def __init__(self, app_id: str = None, max_reviews: int = None):
        """
        Initialize the scraper.
        
        Args:
            app_id: Google Play Store app ID (e.g., 'com.unnes.myunnes')
            max_reviews: Maximum number of reviews to fetch
        """
        self.app_id = app_id or SCRAPER_CONFIG['app_id']
        self.max_reviews = max_reviews or SCRAPER_CONFIG['max_reviews']
        self.language = SCRAPER_CONFIG['language']
        self.country = SCRAPER_CONFIG['country']
        self.delay = SCRAPER_CONFIG['delay_between_requests']
        
    def get_app_info(self) -> Optional[Dict]:
        """
        Fetch basic app information.
        
        Returns:
            Dictionary with app information or None if error
        """
        try:
            logger.info(f" Fetching app info for: {self.app_id}")
            info = app(self.app_id, lang=self.language, country=self.country)
            
            app_data = {
                'app_id': info.get('appId'),
                'title': info.get('title'),
                'score': info.get('score'),
                'ratings': info.get('ratings'),
                'reviews_count': info.get('reviews'),
                'installs': info.get('installs'),
                'version': info.get('version'),
                'updated': info.get('updated'),
            }
            
            logger.info(f" App: {app_data['title']} | Rating: {app_data['score']:.1f} | Reviews: {app_data['reviews_count']:,}")
            return app_data
            
        except Exception as e:
            logger.error(f" Error fetching app info: {e}")
            return None
    
    def scrape_reviews(self, continuation_token: str = None) -> List[Dict]:
        """
        Scrape reviews from Google Play Store.
        
        Args:
            continuation_token: Token for pagination (to continue from where left off)
            
        Returns:
            List of review dictionaries
        """
        try:
            logger.info(f" Starting to scrape reviews (max: {self.max_reviews})...")
            
            all_reviews = []
            token = continuation_token
            
            with tqdm(total=self.max_reviews, desc="Scraping reviews") as pbar:
                while len(all_reviews) < self.max_reviews:
                    # Fetch batch of reviews
                    result, token = reviews(
                        self.app_id,
                        lang=self.language,
                        country=self.country,
                        sort=Sort.NEWEST,
                        count=min(200, self.max_reviews - len(all_reviews)),
                        continuation_token=token
                    )
                    
                    if not result:
                        logger.warning(" No more reviews available")
                        break
                    
                    # Process and store reviews
                    for review in result:
                        review_data = {
                            'review_id': review.get('reviewId'),
                            'author': review.get('userName'),
                            'rating': review.get('score'),
                            'content': review.get('content'),
                            'date': review.get('at'),
                            'thumbs_up': review.get('thumbsUpCount'),
                            'reply_content': review.get('replyContent'),
                            'reply_date': review.get('repliedAt'),
                        }
                        all_reviews.append(review_data)
                    
                    pbar.update(len(result))
                    
                    # Break if no more continuation token
                    if not token:
                        logger.info(" Reached end of available reviews")
                        break
                    
                    # Rate limiting
                    time.sleep(self.delay)
            
            logger.info(f" Successfully scraped {len(all_reviews)} reviews")
            return all_reviews
            
        except Exception as e:
            logger.error(f" Error scraping reviews: {e}")
            return []
    
    def save_reviews(self, reviews_data: List[Dict], filename: str = None) -> bool:
        """
        Save scraped reviews to CSV.
        
        Args:
            reviews_data: List of review dictionaries
            filename: Output filename (default: auto-generated with timestamp)
            
        Returns:
            bool: True if successful, False otherwise
        """
        if not reviews_data:
            logger.warning(" No reviews to save")
            return False
        
        try:
            if not filename:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"reviews_{self.app_id}_{timestamp}.csv"
            
            filepath = RAW_DATA_DIR / filename
            success = DataHandler.save_to_csv(reviews_data, filepath)
            
            if success:
                logger.info(f" Reviews saved to: {filepath}")
            
            return success
            
        except Exception as e:
            logger.error(f" Error saving reviews: {e}")
            return False
    
    def run(self, save_file: bool = True) -> List[Dict]:
        """
        Run the complete scraping pipeline.
        
        Args:
            save_file: Whether to save results to CSV
            
        Returns:
            List of scraped reviews
        """
        logger.info("=" * 60)
        logger.info(" Starting Google Play Store Scraper")
        logger.info("=" * 60)
        
        # Get app info
        app_info = self.get_app_info()
        if not app_info:
            logger.error(" Failed to fetch app info. Aborting.")
            return []
        
        # Scrape reviews
        reviews_data = self.scrape_reviews()
        
        if not reviews_data:
            logger.error(" No reviews scraped. Aborting.")
            return []
        
        # Save to file
        if save_file:
            self.save_reviews(reviews_data)
        
        logger.info("=" * 60)
        logger.info(f" Scraping completed! Total reviews: {len(reviews_data)}")
        logger.info("=" * 60)
        
        return reviews_data


def main():
    """Main entry point for the scraper."""
    from utils import setup_logging
    setup_logging()
    
    # Initialize and run scraper
    scraper = PlayStoreScraper()
    reviews_data = scraper.run()
    
    # Display summary
    if reviews_data:
        print(f"\n Summary:")
        print(f"   Total reviews: {len(reviews_data)}")
        print(f"   Data saved to: {RAW_DATA_DIR}")


if __name__ == "__main__":
    main()
