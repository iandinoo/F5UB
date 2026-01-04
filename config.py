import os

def must_env(key: str, cast=str):
    val = os.getenv(key)
    if not val:
        raise RuntimeError(f"ENV {key} belum diisi")
    return cast(val)

API_ID = must_env("API_ID", int)
API_HASH = must_env("API_HASH")
BOT_TOKEN = must_env("BOT_TOKEN")

OWNER_ID = must_env("OWNER_ID", int)
DATABASE_CHAT_ID = must_env("DATABASE_CHAT_ID", int)
MONGODB_URL = must_env("MONGODB_URL")
