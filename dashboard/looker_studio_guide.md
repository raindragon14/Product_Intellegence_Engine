# 📊 Looker Studio Dashboard Setup Guide

## Overview
This guide will help you create an interactive dashboard in Looker Studio using the processed review data from PI-Engine.

## Prerequisites
- Google account
- Processed data CSV from PI-Engine
- Access to [Looker Studio](https://lookerstudio.google.com/)

## Step-by-Step Setup

### 1. Prepare Your Data

First, generate the dashboard-ready data:
```bash
python scripts/visualize.py
```

This creates `dashboard/exports/looker_studio_data.csv` with all necessary fields.

### 2. Create Data Source in Looker Studio

1. Go to [Looker Studio](https://lookerstudio.google.com/)
2. Click **Create** → **Data Source**
3. Select **File Upload**
4. Upload `dashboard/exports/looker_studio_data.csv`
5. Configure field types:
   - `date` → Date
   - `rating` → Number
   - `category` → Text
   - `sentiment` → Text
   - `priority` → Text
   - `summary` → Text

### 3. Create Dashboard

1. Click **Create** → **Report**
2. Select your data source
3. Add visualizations as described below

## 📊 Recommended Visualizations

### KPI Scorecard Section

**Metric Cards (Add 4 cards):**

1. **Total Reviews**
   - Metric: `COUNT(review_id)`
   - Style: Large number with blue background

2. **Average Rating**
   - Metric: `AVG(rating)`
   - Style: Star icon, yellow background
   - Number format: `0.0`

3. **Positive Sentiment %**
   - Metric: `COUNT_IF(sentiment="positive") / COUNT(review_id) * 100`
   - Style: Green background
   - Number format: `0.0%`

4. **High Priority Issues**
   - Metric: `COUNT_IF(priority="high")`
   - Style: Red background, warning icon

### Chart 1: Top Categories (Bar Chart)

- **Chart Type**: Horizontal Bar Chart
- **Dimension**: `category`
- **Metric**: `COUNT(review_id)`
- **Sort**: Descending by count
- **Limit**: Top 10
- **Style**: 
  - Color: Blue gradient
  - Show data labels
  - Title: "📊 Top Complaint Categories"

### Chart 2: Sentiment Distribution (Pie Chart)

- **Chart Type**: Pie Chart
- **Dimension**: `sentiment`
- **Metric**: `COUNT(review_id)`
- **Style**:
  - Positive: Green (#2ecc71)
  - Neutral: Yellow (#f39c12)
  - Negative: Red (#e74c3c)
  - Show percentages
  - Title: "😊 Sentiment Distribution"

### Chart 3: Rating Distribution (Column Chart)

- **Chart Type**: Column Chart
- **Dimension**: `rating`
- **Metric**: `COUNT(review_id)`
- **Sort**: Descending by rating
- **Style**:
  - Color: Gold gradient
  - Show data labels
  - Title: "⭐ Rating Distribution"

### Chart 4: Trend Over Time (Time Series)

- **Chart Type**: Time Series Chart
- **Dimension**: `date` (by month)
- **Metrics**:
  - `AVG(rating)` (Line 1)
  - `COUNT(review_id)` (Line 2, right axis)
- **Style**:
  - Line 1: Blue
  - Line 2: Purple (bars)
  - Title: "📈 Rating & Volume Trends"

### Chart 5: Priority Matrix (Stacked Bar)

- **Chart Type**: Stacked Column Chart
- **Dimension**: `category`
- **Breakdown Dimension**: `priority`
- **Metric**: `COUNT(review_id)`
- **Style**:
  - High: Red
  - Medium: Yellow
  - Low: Green
  - Title: "⚠️ Priority by Category"

### Chart 6: Category vs Sentiment (Heatmap)

- **Chart Type**: Pivot Table with Heatmap
- **Row**: `category`
- **Column**: `sentiment`
- **Metric**: `COUNT(review_id)`
- **Style**:
  - Apply heatmap coloring
  - Show totals
  - Title: "🔥 Category-Sentiment Matrix"

### Table: High Priority Issues

- **Chart Type**: Table
- **Dimensions**: `category`, `rating`, `summary`
- **Filter**: `priority = "high"`
- **Sort**: By `date` (newest first)
- **Limit**: 20 rows
- **Style**:
  - Compact rows
  - Alternating row colors
  - Title: "🔴 Critical Issues Requiring Attention"

## 🎨 Dashboard Layout Template

```
┌──────────────────────────────────────────────────────────────┐
│                     PI-Engine Dashboard                       │
│                     Product: [App Name]                       │
├────────────┬────────────┬────────────┬─────────────────────┤
│Total Reviews│Avg Rating │ Positive % │ High Priority Issues │
│   [1,234]  │   [4.2⭐]  │   [65%]    │      [23]           │
├────────────┴────────────┴────────────┴─────────────────────┤
│                                                               │
│  📊 Top Categories          │   😊 Sentiment Distribution    │
│  [Bar Chart]                │   [Pie Chart]                  │
│                             │                                │
├─────────────────────────────┴────────────────────────────────┤
│                    📈 Trend Analysis                          │
│              [Time Series: Rating & Volume]                   │
│                                                               │
├────────────────────────┬─────────────────────────────────────┤
│  ⚠️ Priority Matrix    │   🔥 Category-Sentiment Heatmap    │
│  [Stacked Bar]         │   [Pivot Table]                     │
│                        │                                      │
├────────────────────────┴─────────────────────────────────────┤
│            🔴 Critical Issues Requiring Attention             │
│                    [Filtered Table]                           │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

## 🎯 Interactive Features

### Add Filters

1. **Date Range Filter**
   - Field: `date`
   - Type: Date range control
   - Default: Last 90 days

2. **Category Filter**
   - Field: `category`
   - Type: Dropdown list
   - Allow multiple selections

3. **Sentiment Filter**
   - Field: `sentiment`
   - Type: Fixed-size list
   - Default: All selected

4. **Rating Filter**
   - Field: `rating`
   - Type: Slider
   - Range: 1-5

### Add Parameters

Create a parameter for dynamic title:
- **Name**: `app_name`
- **Type**: Text
- **Default**: "MyUNNES"
- Use in title: `${app_name} - Product Intelligence Dashboard`

## 📱 Mobile Optimization

1. Enable mobile layout in Page settings
2. Adjust chart sizes for mobile:
   - Use 1-column layout
   - Simplify charts (fewer data points)
   - Larger fonts for readability

## 🔄 Auto-Refresh Data

### Option 1: Google Sheets Integration

1. Upload CSV to Google Sheets
2. Use Google Sheets as data source
3. Set up automatic updates via Apps Script

### Option 2: Direct Upload (Manual)

1. Re-upload CSV when data changes
2. Dashboard auto-updates

### Option 3: BigQuery (Advanced)

1. Load data to BigQuery
2. Connect Looker Studio to BigQuery
3. Set up scheduled queries

## 🎨 Styling Tips

- **Color Scheme**: Use consistent brand colors
- **Typography**: Clear, readable fonts (min 12pt)
- **White Space**: Don't overcrowd the dashboard
- **Alignment**: Align elements for professional look
- **Branding**: Add logo and footer

## 📊 Sample Dashboard Template

Download our pre-made template:
1. Visit: [Sample PI-Engine Dashboard](#)
2. Click "Make a copy"
3. Replace data source with your own
4. Customize as needed

## 🆘 Troubleshooting

**Issue**: Data not showing
- Check field types are correct
- Verify CSV encoding (UTF-8)
- Refresh data source

**Issue**: Date formatting wrong
- Set date format in data source settings
- Use `PARSE_DATE()` function if needed

**Issue**: Charts look different
- Browser cache - try incognito mode
- Check data source is connected
- Verify chart configuration

## 📚 Additional Resources

- [Looker Studio Documentation](https://support.google.com/looker-studio)
- [Data Visualization Best Practices](https://www.tableau.com/learn/articles/data-visualization-tips)
- [Dashboard Design Principles](https://www.klipfolio.com/resources/articles/dashboard-design-best-practices)

---

**Need Help?** Open an issue on GitHub or check the project documentation.
