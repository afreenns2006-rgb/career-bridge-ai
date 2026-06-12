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

# ============================================
# AI Configuration (NEW)
# ============================================

# AI Provider: "ollama" or "byok"
AI_PROVIDER: Final[str] = os.getenv("AI_PROVIDER", "ollama")

# Ollama configuration
OLLAMA_API_URL: Final[str] = os.getenv("OLLAMA_API_URL", "http://localhost:11434/api/generate")
OLLAMA_MODEL: Final[str] = os.getenv("OLLAMA_MODEL", "llama3")

# BYOK Configuration
BYOK_API_KEY: Final[str] = os.getenv("BYOK_API_KEY", "")
BYOK_PROVIDER_TYPE: Final[str] = os.getenv("BYOK_PROVIDER_TYPE", "generic")

# ============================================
# Language Configuration (NEW)
# ============================================

# Default language
DEFAULT_LANGUAGE: Final[str] = os.getenv("DEFAULT_LANGUAGE", "English")

# Enable multilingual support
ENABLE_MULTILINGUAL: Final[bool] = os.getenv("ENABLE_MULTILINGUAL", "True").lower() == "true"

# Supported languages
SUPPORTED_LANGUAGES: Final[list[str]] = ["English", "हिंदी", "తెలుగు"]


def ensure_directories() -> None:
    """
    Create necessary directories if they don't exist.
    
    TODO: Implement directory creation.
    """
    directories = [
        DATA_DIR,
        UPLOADS_DIR,
        MODELS_DIR,
        ASSETS_DIR,
        LOGS_DIR,
        TESTS_DIR
    ]
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)


def get_config() -> dict[str, any]:
    """
    Get application configuration as a dictionary.
    
    Returns:
        dict: Configuration dictionary with all settings.
        
    TODO: Implement configuration retrieval.
    """
    return {
        "db_path": str(DB_PATH),
        "db_timeout": DB_TIMEOUT,
        "uploads_dir": str(UPLOADS_DIR),
        "models_dir": str(MODELS_DIR),
        "max_upload_size_mb": MAX_UPLOAD_SIZE_MB,
        "allowed_formats": ALLOWED_UPLOAD_FORMATS,
        "log_level": LOG_LEVEL,
        "log_file": str(LOG_FILE),
        "min_ats_score": MIN_ATS_SCORE,
        "max_ats_score": MAX_ATS_SCORE,
        "batch_size": DEFAULT_BATCH_SIZE,
        "random_state": RANDOM_STATE
    }
