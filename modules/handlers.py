from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from modules.database import *
from modules.utils import generate_link
from config import OWNER_ID

def register_handlers(app):

    @app.on_message(filters.command("start"))
    async def start(client, message):
        user_id = message.from_user.id
        add_user(user_id)
        start_text = get_setting("start_text") or "Selamat datang di File Sharing Bot!"
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("⚙️ Pengaturan", callback_data="admin_panel")],
            [InlineKeyboardButton("👤 Owner", url=f"https://t.me/{OWNER_ID}")]
        ])
        await message.reply(start_text, reply_markup=keyboard)

    @app.on_message(filters.channel)
    async def channel_post(client, message):
        add_file(message.chat.id, message.message_id)

    @app.on_callback_query()
    async def admin_panel(client, query):
        data = query.data
        if data == "admin_panel":
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("🛡 Force Sub", callback_data="force_sub")],
                [InlineKeyboardButton("📝 Start Text", callback_data="start_text")],
                [InlineKeyboardButton("🔒 Protect Content", callback_data="protect")],
                [InlineKeyboardButton("📢 Broadcast", callback_data="broadcast")],
                [InlineKeyboardButton("👥 Users", callback_data="users")],
                [InlineKeyboardButton("👤 Admins", callback_data="admins")]
            ])
            await query.message.edit_text("Admin Panel:", reply_markup=keyboard)

    @app.on_message(filters.command("gcast"))
    async def gcast(client, message):
        if message.from_user.id not in [a["_id"] for a in get_admins()]:
            return
        if not message.reply_to_message:
            await message.reply("Reply pesan yang ingin di-broadcast.")
            return
        users = get_users()
        success, failed = 0, 0
        for u in users:
            try:
                await client.send_message(u["_id"], message.reply_to_message.text)
                success += 1
            except:
                failed += 1
        await message.reply(f"Broadcast selesai ✅\nTerkirim: {success}\nGagal: {failed}")
                
