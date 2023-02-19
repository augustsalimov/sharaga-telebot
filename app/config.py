import os

from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
CHAT_ID = os.getenv("CHAT_ID")
ADMIN_USER_ID = os.getenv("ADMIN_USER_ID")
# TELEGRAM_BOT_CHANNEL_ID = int(os.getenv("TELEGRAM_BOT_CHANNEL_ID", "0"))

BASE_DIR = Path(__file__).resolve().parent
SQLITE_DB_FILE = BASE_DIR / "db.sqlite3"
TEMPLATES_DIR = BASE_DIR / "templates"
FILES_DIR = BASE_DIR / "files"
