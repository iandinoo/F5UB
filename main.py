from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from router import register_routes

app = Client(
    "filesharingbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True
)

register_routes(app)
