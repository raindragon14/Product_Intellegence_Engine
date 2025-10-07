"""
Logging utilities for Product Intelligence Engine.
Provides consistent logging across all modules.
"""

import logging
import logging.config
from pathlib import Path
from config.config import LOGGING_CONFIG


def setup_logging():
    """Configure logging for the application."""
    logging.config.dictConfig(LOGGING_CONFIG)
    logger = logging.getLogger(__name__)
    logger.info("🚀 Logging initialized")


def get_logger(name: str) -> logging.Logger:
    """
    Get a logger instance.
    
    Args:
        name: Name of the logger (typically __name__)
        
    Returns:
        Logger instance
    """
    return logging.getLogger(name)
