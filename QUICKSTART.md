# 🚀 Product Intelligence Engine - Quick Start Guide

## 📋 Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment
```bash
# Copy the example env file
cp .env.example .env

# Edit .env and add your Gemini API key
# Get your key from: https://ai.google.dev/
```

### 3. Update Configuration (Optional)
Edit `config/config.py` to customize:
- App ID (default: `com.unnes.myunnes`)
- Max reviews to scrape
- LLM model settings

## 🏃 Running the Pipeline

### Option 1: Full Pipeline (Recommended)
Run everything from scraping to analysis:
```bash
python main.py
```

### Option 2: With Custom Parameters
```bash
python main.py --app-id com.example.app --max-reviews 500
```

### Option 3: Step by Step

**Step 1: Scrape Reviews**
```bash
python main.py --scrape-only
```

**Step 2: Process with LLM**
```bash
python main.py --process-only
```

### Option 4: Individual Scripts

**Scraping only:**
```bash
python scripts/scraper.py
```

**Processing only:**
```bash
python scripts/process_llm.py
```

## 📊 Using Jupyter Notebook

For data exploration and visualization:
```bash
jupyter notebook notebooks/data_exploration.ipynb
```

## 📁 Output Files

- **Raw Data**: `data/raw/reviews_*.csv`
- **Processed Data**: `data/processed/processed_reviews_*.csv`
- **Logs**: `pipeline.log`

## 🎯 Next Steps

1. **Import to Looker Studio**: Upload processed CSV to create dashboards
2. **Analyze Trends**: Use the Jupyter notebook for deeper insights
3. **Share with Team**: Export insights and visualizations

## ⚙️ Configuration Options

### In `config/config.py`:

```python
# Scraper settings
SCRAPER_CONFIG = {
    "app_id": "com.unnes.myunnes",
    "max_reviews": 1000,
    "language": "id",
    "country": "id",
}

# LLM settings
LLM_CONFIG = {
    "model": "gemini-1.5-flash",
    "temperature": 0.3,
    "batch_size": 10,
}
```

## 🆘 Troubleshooting

**Issue**: API key error
- **Solution**: Make sure `.env` file exists with valid `GEMINI_API_KEY`

**Issue**: No data scraped
- **Solution**: Check app ID is correct and app has reviews

**Issue**: Rate limiting
- **Solution**: Reduce `batch_size` in config or increase delay

## 📚 Project Structure

```
Product_Intellegence_Engine/
├── config/              # Configuration files
├── data/
│   ├── raw/            # Scraped reviews
│   └── processed/      # Classified reviews
├── scripts/            # Core modules
│   ├── scraper.py      # Web scraper
│   └── process_llm.py  # LLM processor
├── utils/              # Helper functions
├── notebooks/          # Jupyter notebooks
├── main.py             # Main pipeline
└── requirements.txt    # Dependencies
```

## 🤝 Contributing

Feel free to submit issues or pull requests!

## 📄 License

MIT License - see LICENSE file for details
