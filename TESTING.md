# 🧪 Testing Guide

Panduan untuk testing Product Intelligence Engine.

## Quick Test

### 1. Test with Sample Data

```bash
# Copy sample data
cp data/samples/sample_reviews.csv data/raw/test_reviews.csv

# Run processing
python scripts/process_llm.py
```

### 2. Test Individual Components

**Test Scraper (requires valid app ID):**
```bash
python scripts/scraper.py
```

**Test LLM Processor:**
```bash
python scripts/process_llm.py
```

**Test Visualization:**
```bash
python scripts/visualize.py
```

### 3. Test Full Pipeline

```bash
# Dry run with limited data
python main.py --max-reviews 50
```

## Unit Testing

### Create Test Environment

```bash
# Create virtual environment
python -m venv venv

# Activate
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dev dependencies
pip install -r requirements.txt
```

### Run Tests

```bash
# Test data handler
python -c "from utils import DataHandler; print('✅ DataHandler works!')"

# Test configuration
python -c "from config.config import GEMINI_API_KEY; print('✅ Config loaded!')"

# Test logging
python -c "from utils import setup_logging, get_logger; setup_logging(); logger = get_logger('test'); logger.info('✅ Logging works!')"
```

## Validation Checklist

- [ ] Environment variables loaded correctly
- [ ] Dependencies installed
- [ ] Scraper can fetch app info
- [ ] LLM processor can classify reviews
- [ ] Data saved to correct folders
- [ ] Visualizations generated
- [ ] Dashboard exports created
- [ ] Logs written properly

## Common Issues

**Issue**: ImportError for modules
- **Fix**: Make sure you're in project root directory
- **Fix**: Add project to PYTHONPATH: `set PYTHONPATH=%CD%` (Windows)

**Issue**: API key not found
- **Fix**: Copy `.env.example` to `.env` and add your key

**Issue**: No module named 'google_play_scraper'
- **Fix**: `pip install google-play-scraper`

## Performance Testing

Test with different data sizes:

```bash
# Small (50 reviews)
python main.py --max-reviews 50

# Medium (200 reviews)
python main.py --max-reviews 200

# Large (1000 reviews)
python main.py --max-reviews 1000
```

Monitor:
- Execution time
- API rate limits
- Memory usage
- Output quality

## Debug Mode

Enable verbose logging:

1. Edit `config/config.py`
2. Change logging level to DEBUG:
```python
"root": {
    "level": "DEBUG",  # Changed from "INFO"
    "handlers": ["console", "file"]
}
```

## CI/CD Testing

For automated testing in GitHub Actions or similar:

```yaml
- name: Test PI-Engine
  run: |
    pip install -r requirements.txt
    python -c "from utils import DataHandler; print('✅ Import OK')"
    # Add more tests
```

## Sample Output Validation

Expected outputs after running full pipeline:

```
data/
├── raw/
│   └── reviews_*.csv (with review data)
├── processed/
│   └── processed_reviews_*.csv (with classifications)
└── samples/
    └── sample_reviews.csv

dashboard/
└── exports/
    ├── looker_studio_data.csv
    ├── category_distribution.png
    ├── sentiment_analysis.png
    ├── trend_analysis.png
    └── priority_distribution.png
```

## Reporting Issues

If you find bugs, please report with:
1. Error message
2. Steps to reproduce
3. Python version
4. OS version
5. Log file (`pipeline.log`)
