from pathlib import Path

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Data Directories
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
ARCHIVE_DATA_DIR = DATA_DIR / "archive"

# Database
DATABASE_DIR = BASE_DIR / "database"
DATABASE_PATH = DATABASE_DIR / "realnut.db"

DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

# Logs
LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "app.log"

# Reports
REPORT_DIR = BASE_DIR / "reports"

# Assets
ASSETS_DIR = BASE_DIR / "assets"