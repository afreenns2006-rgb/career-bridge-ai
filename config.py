"""
Configuration module for Career Bridge AI.

Contains global settings, path management, and constants used
throughout the application.
"""

import os
from pathlib import Path
from typing import Final

# Project root directory
PROJECT_ROOT: Final[Path] = Path(__file__).parent

# Database configuration
DB_PATH: Final[Path] = PROJECT_ROOT / "data" / "career_bridge.db"
DB_TIMEOUT: Final[int] = 10

# File paths
DATA_DIR: Final[Path] = PROJECT_ROOT / "data"
UPLOADS_DIR: Final[Path] = PROJECT_ROOT / "uploads"
MODELS_DIR: Final[Path] = PROJECT_ROOT / "models"
ASSETS_DIR: Final[Path] = PROJECT_ROOT / "assets"
LOGS_DIR: Final[Path] = PROJECT_ROOT / "logs"
TESTS_DIR: Final[Path] = PROJECT_ROOT / "tests"

# CSV file paths
CAREERS_CSV: Final[Path] = DATA_DIR / "careers.csv"
SCHOLARSHIPS_CSV: Final[Path] = DATA_DIR / "scholarships.csv"
SCHEMES_CSV: Final[Path] = DATA_DIR / "schemes.csv"
OPPORTUNITIES_CSV: Final[Path] = DATA_DIR / "opportunities.csv"

# Streamlit configuration
STREAMLIT_PAGE_TITLE: Final[str] = "Career Bridge AI"
STREAMLIT_PAGE_ICON: Final[str] = "🎓"
STREAMLIT_LAYOUT: Final[str] = "wide"

# Upload configuration
MAX_UPLOAD_SIZE_MB: Final[int] = 10
ALLOWED_UPLOAD_FORMATS: Final[tuple[str, ...]] = (".pdf", ".docx", ".txt")

# Logging configuration
LOG_LEVEL: Final[str] = "INFO"
LOG_FILE: Final[Path] = LOGS_DIR / "career_bridge.log"

# Resume parsing configuration
MIN_ATS_SCORE: Final[float] = 40.0
MAX_ATS_SCORE: Final[float] = 100.0

# Application constants
DEFAULT_BATCH_SIZE: Final[int] = 32
RANDOM_STATE: Final[int] = 42


def ensure_directories() -> None:
    """
    Create necessary directories if they don't exist.
    
    TODO: Implement directory creation.
    """
    pass


def get_config() -> dict[str, any]:
    """
    Get application configuration as a dictionary.
    
    Returns:
        dict: Configuration dictionary with all settings.
        
    TODO: Implement configuration retrieval.
    """
    pass
