from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from router import router

app = Client("filesharingbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Register all handlers
router.register(app)

if __name__ == "__main__":
    print("Bot starting ...")
    app.run()
    
