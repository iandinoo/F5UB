import os
from dotenv import load_dotenv

# Load file .env jika ada
load_dotenv()

API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
OWNER_ID = int(os.getenv("OWNER_ID", 0))
DATABASE_CHANNEL = int(os.getenv("DATABASE_CHANNEL", 0))
MONGO_URI = os.getenv("MONGO_URI", "")
