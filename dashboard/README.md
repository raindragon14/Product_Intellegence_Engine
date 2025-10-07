# 📊 Dashboard Configuration & Setup

This folder contains dashboard configuration and exported data for visualization tools like Looker Studio.

## 📁 Contents

- `exports/` - Exported data and charts for Looker Studio
- `looker_studio_guide.md` - Guide for setting up Looker Studio dashboard
- `sample_dashboard_config.json` - Sample dashboard configuration

## 🚀 Quick Start

### 1. Generate Dashboard Data

Run the visualization script to generate charts and export data:

```bash
python scripts/visualize.py
```

This will create:
- Charts (PNG files) in `dashboard/exports/`
- `looker_studio_data.csv` - Main data file for Looker Studio
- `dashboard_summary.json` - Summary statistics

### 2. Import to Looker Studio

1. Go to [Looker Studio](https://lookerstudio.google.com/)
2. Create a new data source
3. Upload `exports/looker_studio_data.csv`
4. Create visualizations based on the sample configuration

### 3. Use Pre-generated Charts

The exported PNG files can be used directly in presentations or reports:
- `category_distribution.png`
- `sentiment_analysis.png`
- `trend_analysis.png`
- `priority_distribution.png`

## 📊 Dashboard Metrics

### Key Performance Indicators (KPIs)
- Total Reviews Count
- Average Rating
- Sentiment Distribution (%)
- High Priority Issues Count

### Visualizations
1. **Category Distribution** - Bar chart of complaint categories
2. **Sentiment Analysis** - Pie/bar chart of positive/neutral/negative
3. **Trend Analysis** - Time series of ratings and review volume
4. **Priority Matrix** - Distribution of priority levels
5. **Feature Comparison** - Comparative analysis with competitors

## 🎯 Recommended Dashboard Layout

```
┌─────────────────────────────────────────────┐
│  KPI Cards: Total | Avg Rating | Sentiment  │
├──────────────────┬──────────────────────────┤
│  Top Categories  │   Sentiment Distribution │
│  (Bar Chart)     │   (Pie Chart)            │
├──────────────────┼──────────────────────────┤
│  Trend Analysis (Line Chart)                │
├──────────────────┬──────────────────────────┤
│  Priority Issues │   Top Complaints Table   │
└──────────────────┴──────────────────────────┘
```

## 📝 Notes

- Data is automatically exported when running the main pipeline
- Refresh data by running `python scripts/visualize.py`
- Customize charts by editing `scripts/visualize.py`
