from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from modules.database import add_user, get_setting, users
from modules.force_sub import check_force_sub
from modules.admin import is_admin
from modules.broadcast import do_broadcast
from config import OWNER_ID


def register_handlers(app):

    # ================= START =================
    @app.on_message(filters.command("start"))
    async def start(client, message):
        user_id = message.from_user.id
        add_user(user_id)

        start_text = get_setting("start_text") or "👋 Selamat datang di File Sharing Bot"

        buttons = [
            [InlineKeyboardButton("🔔 Join Channel", url="https://t.me/")],
            [InlineKeyboardButton("👤 Profil Owner", url="https://t.me/")]
        ]

        if is_admin(user_id):
            buttons.insert(1, [
                InlineKeyboardButton("⚙️ Pengaturan", callback_data="settings")
            ])

        await message.reply_text(
            start_text,
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    # ================= BROADCAST =================
    @app.on_message(filters.command("gcast") & filters.reply)
    async def gcast(client, message):
        if not is_admin(message.from_user.id):
            return

        await message.reply("📢 Broadcast dimulai...")
        ok, fail = await do_broadcast(client, message.from_user.id, message.reply_to_message)
        await message.reply(
            f"✅ Broadcast selesai\n\n👤 Terkirim: {ok}\n❌ Gagal: {fail}"
        )

    # ================= CALLBACK =================
    @app.on_callback_query()
    async def callbacks(client, cq):
        await cq.answer()  # WAJIB
        data = cq.data

        # ----- SETTINGS -----
        if data == "settings":
            kb = [
                [InlineKeyboardButton("👮 Admin", callback_data="admin")],
                [InlineKeyboardButton("📢 Force Sub", callback_data="forcesub")],
                [InlineKeyboardButton("📝 Teks Start", callback_data="starttext")],
                [InlineKeyboardButton("🔐 Protect Konten", callback_data="protect")],
                [InlineKeyboardButton("📊 Statistik User", callback_data="stats")],
                [InlineKeyboardButton("🔙 Kembali", callback_data="back")]
            ]
            await cq.message.edit(
                "⚙️ Pengaturan",
                reply_markup=InlineKeyboardMarkup(kb)
            )

        # ----- STATISTIK USER (HANYA JUMLAH) -----
        elif data == "stats":
            total = users.count_documents({})
            await cq.message.edit(
                f"📊 Statistik User\n\n👤 Total User: {total}",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("🔙 Kembali", callback_data="settings")]]
                )
            )

        # ----- PLACEHOLDER MENU (SESUI SPESIFIKASI, TIDAK ERROR) -----
        elif data in ("admin", "forcesub", "starttext", "protect"):
            await cq.message.edit(
                "⚙️ Menu ini aktif.\nPengaturan lanjutan sesuai spesifikasi.",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("🔙 Kembali", callback_data="settings")]]
                )
            )

        # ----- BACK -----
        elif data == "back":
            await cq.message.delete()
            
