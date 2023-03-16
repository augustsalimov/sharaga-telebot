from pydantic import BaseSettings
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


class BotSettings(BaseSettings):
    TELEGRAM_BOT_TOKEN: str
    CHAT_ID: str
    ADMIN_USER_ID: str
    # TELEGRAM_BOT_CHANNEL_ID = int(os.getenv("TELEGRAM_BOT_CHANNEL_ID", "0"))

    class Config:
        env_file = "./.env"


bot_settings = BotSettings()


BASE_DIR = Path(__file__).resolve().parent.parent
SQLITE_DB_FILE = BASE_DIR / "db.sqlite3"
TEMPLATES_DIR = BASE_DIR / "templates"
FILES_DIR = BASE_DIR / "files"
