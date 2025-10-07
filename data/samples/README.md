# 📝 Sample Data for Testing

This folder contains sample review data for testing the pipeline without scraping.

## Files

- `sample_reviews.csv` - Sample review data with various categories and sentiments
- `sample_processed.csv` - Example of processed output with LLM classifications

## Using Sample Data

To test the pipeline with sample data:

```bash
# Copy sample data to raw folder
cp data/samples/sample_reviews.csv data/raw/

# Run processing only
python main.py --process-only

# Or run visualization on sample processed data
cp data/samples/sample_processed.csv data/processed/
python main.py --visualize-only
```

## Sample Data Structure

### Raw Reviews Format
- review_id: Unique identifier
- author: Username
- rating: 1-5 stars
- content: Review text
- date: Review date
- thumbs_up: Number of helpful votes
- reply_content: Developer reply (if any)
- reply_date: Reply date (if any)

### Processed Format
- All raw fields plus:
- category: Main category (UI/UX, Performance, etc.)
- subcategory: Specific subcategory
- sentiment: positive/neutral/negative
- priority: high/medium/low
- summary: Brief issue summary
- keywords: Related keywords

## Notes

- Sample data is in Indonesian to match target use case
- Covers multiple categories and sentiment types
- Includes various priority levels
- Realistic data based on actual app reviews
