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

**Step 3: Generate Visualizations**
```bash
python main.py --visualize-only
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

**Visualization only:**
```bash
python scripts/visualize.py
```

## 📊 Using Jupyter Notebook

For data exploration and visualization:
```bash
jupyter notebook notebooks/data_exploration.ipynb
```

## 📁 Output Files

- **Raw Data**: `data/raw/reviews_*.csv`
- **Processed Data**: `data/processed/processed_reviews_*.csv`
- **Dashboard Exports**: `dashboard/exports/`
  - `looker_studio_data.csv` - Main file for Looker Studio
  - `*.png` - Generated charts
  - `dashboard_summary.json` - Summary statistics
- **Logs**: `pipeline.log`

## 🎯 Next Steps

1. **Check Generated Charts**: Open `dashboard/exports/` to see visualizations
2. **Import to Looker Studio**: Upload `looker_studio_data.csv` to create interactive dashboards
3. **Follow Dashboard Guide**: Read `dashboard/looker_studio_guide.md` for detailed setup
4. **Analyze Trends**: Use the Jupyter notebook for deeper insights
5. **Share with Team**: Export insights and visualizations

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
│   └── config.py       # Central configuration
├── data/
│   ├── raw/            # Scraped reviews
│   └── processed/      # Classified reviews
├── scripts/            # Core modules
│   ├── scraper.py      # Web scraper
│   ├── process_llm.py  # LLM processor
│   └── visualize.py    # Chart generator
├── utils/              # Helper functions
│   ├── data_handler.py # Data operations
│   └── logger.py       # Logging utilities
├── notebooks/          # Jupyter notebooks
│   └── data_exploration.ipynb
├── dashboard/          # Dashboard files
│   ├── exports/        # Generated charts & data
│   ├── README.md       # Dashboard guide
│   ├── looker_studio_guide.md
│   └── sample_dashboard_config.json
├── main.py             # Main pipeline
├── requirements.txt    # Dependencies
├── .env.example        # Environment template
└── QUICKSTART.md       # This file
```

## 🤝 Contributing

Feel free to submit issues or pull requests!

## 📄 License

MIT License - see LICENSE file for details
