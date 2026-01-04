import os
from dotenv import load_dotenv

load_dotenv()

def must_env(key):
    value = os.getenv(key)
    if not value:
        raise RuntimeError(f"ENV {key} belum diisi")
    return value

API_ID = int(must_env("API_ID"))
API_HASH = must_env("API_HASH")
BOT_TOKEN = must_env("BOT_TOKEN")

OWNER_ID = int(must_env("OWNER_ID"))
DATABASE_CHAT_ID = int(must_env("DATABASE_CHAT_ID"))

MONGODB_URL = must_env("MONGODB_URL")
