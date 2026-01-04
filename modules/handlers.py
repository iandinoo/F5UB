from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from modules.database import get_file, get_setting
from modules.force_sub import check_force_sub

def register_handlers(app):

    @app.on_message(filters.command("start"))
    async def start(client, message):
        if len(message.command) == 1:
            text = get_setting("start_text") or "Selamat datang di File Sharing Bot!"
            return await message.reply(text)

        token = message.command[1]
        file_data = get_file(token)

        if not file_data:
            return await message.reply("Link tidak valid.")

        not_joined = await check_force_sub(client, message.from_user.id)

        if not_joined:
            buttons = [
                [InlineKeyboardButton("Join Channel", url=f"https://t.me/c/{abs(cid)}")]
                for cid in not_joined
            ]
            buttons.append([
                InlineKeyboardButton("🔄 Coba Lagi", callback_data=f"retry_{token}")
            ])

            return await message.reply(
                "Silakan join semua channel terlebih dahulu.",
                reply_markup=InlineKeyboardMarkup(buttons)
            )

        await client.send_cached_media(
            chat_id=message.chat.id,
            file_id=file_data["file_id"],
            protect_content=True
        )

    @app.on_callback_query(filters.regex("^retry_"))
    async def retry(client, callback):
        token = callback.data.split("_", 1)[1]
        not_joined = await check_force_sub(client, callback.from_user.id)

        if not not_joined:
            file_data = get_file(token)
            await callback.message.delete()
            await client.send_cached_media(
                callback.message.chat.id,
                file_data["file_id"],
                protect_content=True
            )
        else:
            await callback.answer("Masih belum join semua channel.", show_alert=True)
        
