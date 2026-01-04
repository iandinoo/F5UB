from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from modules.database import add_user, get_setting
from modules.force_sub import check_force_sub
from modules.admin import is_admin
from modules.broadcast import do_broadcast
from config import OWNER_ID


def register_handlers(app):

    @app.on_message(filters.command("start"))
    async def start(client, message):
        user_id = message.from_user.id
        add_user(user_id)

        start_text = get_setting("start_text") or "👋 Selamat datang di File Sharing Bot"

        buttons = [
            [InlineKeyboardButton("🔔 Join Channel", url="https://t.me/")],
            [InlineKeyboardButton("👤 Profil Owner", url=f"https://t.me/")]
        ]

        if is_admin(user_id):
            buttons.insert(1, [InlineKeyboardButton("⚙️ Pengaturan", callback_data="settings")])

        await message.reply_text(
            start_text,
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    @app.on_message(filters.command("gcast") & filters.reply)
    async def gcast(client, message):
        if not is_admin(message.from_user.id):
            return

        await message.reply("📢 Broadcast dimulai...")
        ok, fail = await do_broadcast(client, message.from_user.id, message.reply_to_message)
        await message.reply(f"✅ Broadcast selesai\n👤 Terkirim: {ok}\n❌ Gagal: {fail}")

    @app.on_callback_query()
    async def callbacks(client, cq):
        user_id = cq.from_user.id

        if cq.data == "settings":
            kb = [
                [InlineKeyboardButton("👮 Admin", callback_data="admin")],
                [InlineKeyboardButton("📢 Force Sub", callback_data="forcesub")],
                [InlineKeyboardButton("📝 Teks Start", callback_data="starttext")],
                [InlineKeyboardButton("🔐 Protect Konten", callback_data="protect")],
                [InlineKeyboardButton("📊 Statistik User", callback_data="stats")],
                [InlineKeyboardButton("🔙 Kembali", callback_data="back")]
            ]
            await cq.message.edit("⚙️ Pengaturan", reply_markup=InlineKeyboardMarkup(kb))

        elif cq.data == "stats":
            from modules.database import users
            total = users.count_documents({})
            await cq.answer(f"👤 Total User: {total}", show_alert=True)
            
