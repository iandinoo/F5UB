from pyrogram import filters
from config import OWNER_ID, DATABASE_CHAT_ID
from modules.database import save_file
from modules.utils import generate_token

def register_admin(app):

    @app.on_message(filters.private & filters.user(OWNER_ID) & filters.document)
    async def upload_file(client, message):
        sent = await message.forward(DATABASE_CHAT_ID)
        token = generate_token()
        save_file(token, sent.document.file_id)

        link = f"https://t.me/{(await client.get_me()).username}?start={token}"
        await message.reply(f"✅ File tersimpan\n\n🔗 Link:\n{link}")
      
