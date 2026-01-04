from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import OWNER_ID, DATABASE_CHAT_ID
from modules.database import *
from modules.force_sub import check_force_sub
from modules.utils import generate_code


def register_handlers(app):

    @app.on_message(filters.command("start"))
    async def start(client, message):
        user_id = message.from_user.id
        save_user(user_id)

        start_text = get_setting("start_text") or "Selamat datang di File Sharing Bot!"

        if len(message.command) > 1:
            code = message.command[1]
            msg_id = get_file(code)
            if not msg_id:
                return await message.reply("❌ File tidak ditemukan.")

            if not await check_force_sub(client, user_id):
                buttons = []
                for cid in get_force_subs():
                    chat = await client.get_chat(cid)
                    buttons.append([InlineKeyboardButton(
                        f"Join {chat.title}", url=chat.invite_link
                    )])
                buttons.append([InlineKeyboardButton("🔄 Coba Lagi", callback_data=f"retry_{code}")])

                return await message.reply(
                    "⚠️ Silakan join dulu channel/group:",
                    reply_markup=InlineKeyboardMarkup(buttons)
                )

            protect = get_setting("protect") or False
            return await client.copy_message(
                message.chat.id,
                DATABASE_CHAT_ID,
                msg_id,
                protect_content=protect
            )

        await message.reply(start_text, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("👤 Profil Owner", url=f"https://t.me/{OWNER_ID}")]
        ]))


    @app.on_message(filters.private & filters.media & filters.user([OWNER_ID] + get_admins()))
    async def upload(client, message):
        code = generate_code()
        sent = await message.copy(DATABASE_CHAT_ID)
        save_file(code, sent.id)

        await message.reply(
            f"✅ File tersimpan\n\n🔗 Link:\nhttps://t.me/{client.me.username}?start={code}"
                )
            
