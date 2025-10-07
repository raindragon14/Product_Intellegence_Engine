# ⚙️ Configuration Module

Central configuration management for Product Intelligence Engine.

## Files

- `config.py` - Main configuration file with all settings

## Configuration Categories

### 1. Directory Paths
```python
BASE_DIR          # Project root
DATA_DIR          # Data folder
RAW_DATA_DIR      # Raw scraped data
PROCESSED_DATA_DIR # Processed data with LLM classifications
```

### 2. API Configuration
```python
GEMINI_API_KEY    # Google Gemini API key (from .env)
```

### 3. Scraper Settings
```python
SCRAPER_CONFIG = {
    "app_id": "com.unnes.myunnes",  # Target app
    "max_reviews": 1000,             # Max reviews to fetch
    "language": "id",                # Language (Indonesian)
    "country": "id",                 # Country (Indonesia)
    "sort_by": "newest",             # Sort order
    "delay_between_requests": 1.0,   # Rate limiting (seconds)
}
```

### 4. LLM Processing Settings
```python
LLM_CONFIG = {
    "model": "gemini-1.5-flash",    # Gemini model
    "temperature": 0.3,              # Consistency (0-1)
    "max_retries": 3,                # Retry on failure
    "retry_delay": 2,                # Delay between retries
    "batch_size": 10,                # Reviews per batch
}
```

### 5. Data Schema
```python
REVIEW_SCHEMA = {
    "required_columns": [
        "review_id", "author", "rating",
        "content", "date", "thumbs_up"
    ],
    "processed_columns": [
        "review_id", "content", "rating", "date",
        "category", "subcategory", "sentiment",
        "priority", "summary"
    ]
}
```

### 6. Classification Categories
```python
FEEDBACK_CATEGORIES = {
    "UI/UX": ["Design", "Navigation", "Accessibility", "Layout"],
    "Performance": ["Speed", "Lag", "Crash", "Loading"],
    "Feature": ["Missing Feature", "Feature Request", "Feature Bug"],
    "Authentication": ["Login", "Registration", "Password Reset"],
    "Content": ["Information Accuracy", "Content Quality", "Updates"],
    "Technical": ["Bug", "Error", "Integration Issues"],
    "Other": ["General Feedback", "Praise", "Question"]
}
```

### 7. Logging Configuration
```python
LOGGING_CONFIG = {
    # See config.py for full configuration
    # Controls console and file logging
}
```

## Customization

### Change Target App

Edit in `config.py`:
```python
SCRAPER_CONFIG = {
    "app_id": "com.your.app",  # Your app ID
    ...
}
```

### Adjust LLM Model

Edit in `config.py`:
```python
LLM_CONFIG = {
    "model": "gemini-1.5-pro",  # Use Pro model for better quality
    "temperature": 0.2,         # Lower for more consistency
    ...
}
```

### Add New Categories

Edit in `config.py`:
```python
FEEDBACK_CATEGORIES = {
    ...
    "YourCategory": ["SubCat1", "SubCat2"],
}
```

### Modify Logging

Edit in `config.py`:
```python
LOGGING_CONFIG = {
    "handlers": {
        "console": {
            "level": "DEBUG",  # Change to DEBUG for verbose logs
            ...
        }
    }
}
```

## Environment Variables

Required in `.env` file:

```env
GEMINI_API_KEY=your-api-key-here
```

Optional:
```env
APP_ID=com.your.app
MAX_REVIEWS=1000
```

## Best Practices

1. **Never commit API keys** - Use `.env` file (gitignored)
2. **Use constants** - Don't hardcode values in scripts
3. **Centralize config** - All settings in one place
4. **Document changes** - Add comments for custom settings
5. **Version control** - Track config changes in git

## Import Usage

```python
# In your scripts
from config.config import (
    GEMINI_API_KEY,
    SCRAPER_CONFIG,
    LLM_CONFIG,
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR
)
```

## Troubleshooting

**Issue**: Config not loading
- Ensure you're importing from `config.config`
- Check Python path includes project root

**Issue**: Environment variables not found
- Create `.env` file from `.env.example`
- Add required variables

**Issue**: Path errors
- Paths are auto-created in config.py
- Check directory permissions
