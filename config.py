import os
from dotenv import load_dotenv

load_dotenv()  # load .env otomatis

def _int(name, default=0):
    try:
        return int(os.getenv(name, default))
    except ValueError:
        return default

API_ID = _int("API_ID")
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

OWNER_ID = _int("OWNER_ID")
DATABASE_CHANNEL = _int("DATABASE_CHANNEL")
MONGO_URI = os.getenv("MONGO_URI", "")
