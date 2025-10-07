"""
Configuration module for Product Intelligence Engine.
Centralizes all configuration settings for the application.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Base directories
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Ensure directories exist
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

# API Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
if not GEMINI_API_KEY:
    print("⚠️ WARNING: GEMINI_API_KEY not found in environment variables!")

# Scraper Configuration
SCRAPER_CONFIG = {
    "app_id": "com.unnes.myunnes",  # Default app ID
    "max_reviews": 1000,
    "language": "id",  # Indonesian
    "country": "id",  # Indonesia
    "sort_by": "newest",
    "delay_between_requests": 1.0,  # seconds
}

# LLM Processing Configuration
LLM_CONFIG = {
    "model": "gemini-1.5-flash",
    "temperature": 0.3,  # Lower for more consistent categorization
    "max_retries": 3,
    "retry_delay": 2,  # seconds
    "batch_size": 10,  # Process reviews in batches
}

# Data Schema
REVIEW_SCHEMA = {
    "required_columns": [
        "review_id",
        "author",
        "rating",
        "content",
        "date",
        "thumbs_up"
    ],
    "processed_columns": [
        "review_id",
        "content",
        "rating",
        "date",
        "category",
        "subcategory",
        "sentiment",
        "priority",
        "summary"
    ]
}

# Classification Categories
FEEDBACK_CATEGORIES = {
    "UI/UX": ["Design", "Navigation", "Accessibility", "Layout"],
    "Performance": ["Speed", "Lag", "Crash", "Loading"],
    "Feature": ["Missing Feature", "Feature Request", "Feature Bug"],
    "Authentication": ["Login", "Registration", "Password Reset"],
    "Content": ["Information Accuracy", "Content Quality", "Updates"],
    "Technical": ["Bug", "Error", "Integration Issues"],
    "Other": ["General Feedback", "Praise", "Question"]
}

# Logging Configuration
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "standard",
            "stream": "ext://sys.stdout",
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "standard",
            "filename": str(BASE_DIR / "pipeline.log"),
            "mode": "a",
        },
    },
    "root": {
        "level": "INFO",
        "handlers": ["console", "file"]
    }
}
