"""
Visualization utilities for Product Intelligence Engine.
Generates charts and exports for Looker Studio dashboard.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from typing import Optional
import json

from config.config import PROCESSED_DATA_DIR, BASE_DIR
from utils import DataHandler, get_logger

logger = get_logger(__name__)

# Set visualization style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette('husl')


class DashboardGenerator:
    """Generates visualizations and exports for dashboards."""
    
    def __init__(self, output_dir: Path = None):
        """
        Initialize dashboard generator.
        
        Args:
            output_dir: Directory to save dashboard outputs
        """
        self.output_dir = output_dir or (BASE_DIR / "dashboard" / "exports")
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
    def load_processed_data(self, filename: str = None) -> Optional[pd.DataFrame]:
        """
        Load processed data for visualization.
        
        Args:
            filename: Specific file to load, or None for latest
            
        Returns:
            DataFrame or None
        """
        try:
            if filename:
                filepath = PROCESSED_DATA_DIR / filename
            else:
                # Get latest file
                processed_files = list(PROCESSED_DATA_DIR.glob("*.csv"))
                if not processed_files:
                    logger.error("No processed data files found")
                    return None
                filepath = max(processed_files, key=lambda x: x.stat().st_ctime)
            
            df = DataHandler.load_from_csv(filepath)
            logger.info(f"✅ Loaded data for visualization: {filepath.name}")
            return df
            
        except Exception as e:
            logger.error(f"❌ Error loading data: {e}")
            return None
    
    def generate_category_chart(self, df: pd.DataFrame, save: bool = True):
        """Generate category distribution chart."""
        if 'category' not in df.columns:
            logger.warning("No category column found")
            return
        
        plt.figure(figsize=(12, 6))
        category_counts = df['category'].value_counts()
        
        ax = category_counts.plot(kind='barh', color='skyblue', edgecolor='navy')
        plt.title('📊 Top Complaints by Category', fontsize=16, fontweight='bold', pad=20)
        plt.xlabel('Number of Reviews', fontsize=12)
        plt.ylabel('Category', fontsize=12)
        
        # Add value labels
        for i, v in enumerate(category_counts.values):
            ax.text(v + 5, i, str(v), va='center', fontweight='bold')
        
        plt.tight_layout()
        
        if save:
            filepath = self.output_dir / 'category_distribution.png'
            plt.savefig(filepath, dpi=300, bbox_inches='tight')
            logger.info(f"💾 Saved chart: {filepath}")
        
        plt.show()
    
    def generate_sentiment_chart(self, df: pd.DataFrame, save: bool = True):
        """Generate sentiment analysis chart."""
        if 'sentiment' not in df.columns:
            logger.warning("No sentiment column found")
            return
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        sentiment_counts = df['sentiment'].value_counts()
        colors = {'positive': '#2ecc71', 'neutral': '#f39c12', 'negative': '#e74c3c'}
        sentiment_colors = [colors.get(s, 'gray') for s in sentiment_counts.index]
        
        # Bar chart
        sentiment_counts.plot(kind='bar', ax=ax1, color=sentiment_colors, edgecolor='black')
        ax1.set_title('😊 Sentiment Distribution', fontsize=14, fontweight='bold')
        ax1.set_xlabel('Sentiment', fontsize=12)
        ax1.set_ylabel('Count', fontsize=12)
        ax1.tick_params(axis='x', rotation=45)
        
        # Pie chart
        sentiment_counts.plot(kind='pie', ax=ax2, autopct='%1.1f%%', 
                             colors=sentiment_colors, startangle=90)
        ax2.set_title('😊 Sentiment Percentage', fontsize=14, fontweight='bold')
        ax2.set_ylabel('')
        
        plt.tight_layout()
        
        if save:
            filepath = self.output_dir / 'sentiment_analysis.png'
            plt.savefig(filepath, dpi=300, bbox_inches='tight')
            logger.info(f"💾 Saved chart: {filepath}")
        
        plt.show()
    
    def generate_trend_chart(self, df: pd.DataFrame, save: bool = True):
        """Generate trend analysis over time."""
        if 'date' not in df.columns or 'rating' not in df.columns:
            logger.warning("Missing date or rating columns")
            return
        
        df['date'] = pd.to_datetime(df['date'])
        df['month'] = df['date'].dt.to_period('M')
        
        monthly_stats = df.groupby('month').agg({
            'rating': 'mean',
            'review_id': 'count'
        }).reset_index()
        
        monthly_stats['month'] = monthly_stats['month'].astype(str)
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 8))
        
        # Average rating trend
        ax1.plot(monthly_stats['month'], monthly_stats['rating'], 
                marker='o', linewidth=2, markersize=8, color='#3498db')
        ax1.set_title('📈 Average Rating Trend', fontsize=14, fontweight='bold')
        ax1.set_ylabel('Average Rating', fontsize=12)
        ax1.set_ylim(0, 5.5)
        ax1.grid(True, alpha=0.3)
        ax1.tick_params(axis='x', rotation=45)
        
        # Review volume trend
        ax2.bar(monthly_stats['month'], monthly_stats['review_id'], 
               color='#9b59b6', alpha=0.7, edgecolor='black')
        ax2.set_title('📊 Review Volume Trend', fontsize=14, fontweight='bold')
        ax2.set_xlabel('Month', fontsize=12)
        ax2.set_ylabel('Number of Reviews', fontsize=12)
        ax2.tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        
        if save:
            filepath = self.output_dir / 'trend_analysis.png'
            plt.savefig(filepath, dpi=300, bbox_inches='tight')
            logger.info(f"💾 Saved chart: {filepath}")
        
        plt.show()
    
    def generate_priority_chart(self, df: pd.DataFrame, save: bool = True):
        """Generate priority distribution chart."""
        if 'priority' not in df.columns:
            logger.warning("No priority column found")
            return
        
        priority_counts = df['priority'].value_counts()
        colors_priority = {'high': '#e74c3c', 'medium': '#f39c12', 'low': '#2ecc71'}
        priority_colors = [colors_priority.get(p, 'gray') for p in priority_counts.index]
        
        plt.figure(figsize=(10, 6))
        ax = priority_counts.plot(kind='bar', color=priority_colors, edgecolor='black')
        plt.title('⚠️ Priority Distribution', fontsize=14, fontweight='bold', pad=20)
        plt.xlabel('Priority Level', fontsize=12)
        plt.ylabel('Count', fontsize=12)
        plt.xticks(rotation=45)
        
        # Add value labels
        for i, v in enumerate(priority_counts.values):
            ax.text(i, v + 5, str(v), ha='center', fontweight='bold')
        
        plt.tight_layout()
        
        if save:
            filepath = self.output_dir / 'priority_distribution.png'
            plt.savefig(filepath, dpi=300, bbox_inches='tight')
            logger.info(f"💾 Saved chart: {filepath}")
        
        plt.show()
    
    def export_for_looker(self, df: pd.DataFrame) -> bool:
        """
        Export data in Looker Studio friendly format.
        
        Args:
            df: DataFrame to export
            
        Returns:
            Success status
        """
        try:
            # Main export
            looker_file = self.output_dir / 'looker_studio_data.csv'
            df.to_csv(looker_file, index=False, encoding='utf-8-sig')
            logger.info(f"💾 Exported for Looker Studio: {looker_file}")
            
            # Summary statistics
            summary = {
                'total_reviews': len(df),
                'average_rating': float(df['rating'].mean()) if 'rating' in df.columns else 0,
                'positive_sentiment_pct': float((df['sentiment'] == 'positive').sum() / len(df) * 100) if 'sentiment' in df.columns else 0,
                'negative_sentiment_pct': float((df['sentiment'] == 'negative').sum() / len(df) * 100) if 'sentiment' in df.columns else 0,
                'high_priority_count': int((df['priority'] == 'high').sum()) if 'priority' in df.columns else 0,
                'top_category': df['category'].mode()[0] if 'category' in df.columns and not df.empty else 'N/A',
            }
            
            summary_file = self.output_dir / 'dashboard_summary.json'
            with open(summary_file, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2, ensure_ascii=False)
            
            logger.info(f"💾 Saved summary: {summary_file}")
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Export error: {e}")
            return False
    
    def generate_all_charts(self, df: pd.DataFrame):
        """Generate all visualization charts."""
        logger.info("🎨 Generating all charts...")
        
        self.generate_category_chart(df)
        self.generate_sentiment_chart(df)
        self.generate_priority_chart(df)
        self.generate_trend_chart(df)
        
        logger.info("✅ All charts generated!")
    
    def run(self, filename: str = None):
        """
        Run complete visualization pipeline.
        
        Args:
            filename: Specific processed file to visualize
        """
        logger.info("=" * 60)
        logger.info("🎨 Starting Visualization Pipeline")
        logger.info("=" * 60)
        
        # Load data
        df = self.load_processed_data(filename)
        if df is None or df.empty:
            logger.error("❌ No data to visualize")
            return
        
        # Generate charts
        self.generate_all_charts(df)
        
        # Export for Looker
        self.export_for_looker(df)
        
        logger.info("=" * 60)
        logger.info(f"✅ Visualization complete! Check: {self.output_dir}")
        logger.info("=" * 60)


def main():
    """Main entry point for visualization."""
    from utils import setup_logging
    setup_logging()
    
    generator = DashboardGenerator()
    generator.run()


if __name__ == "__main__":
    main()
