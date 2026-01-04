import os
from dotenv import load_dotenv

# Load .env JIKA ADA (tidak error kalau tidak ada)
load_dotenv()


def must_env(key: str, cast=str):
    val = os.getenv(key)
    if val is None or val == "":
        raise RuntimeError(f"ENV {key} belum diisi")
    try:
        return cast(val)
    except Exception:
        raise RuntimeError(f"ENV {key} tidak valid")


API_ID = must_env("API_ID", int)
API_HASH = must_env("API_HASH")
BOT_TOKEN = must_env("BOT_TOKEN")

OWNER_ID = must_env("OWNER_ID", int)
DATABASE_CHAT_ID = must_env("DATABASE_CHAT_ID", int)

MONGODB_URL = must_env("MONGODB_URL")
