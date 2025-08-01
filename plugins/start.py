from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import OWNER_USERNAME

@Client.on_message(filters.command("start") & filters.private)
async def start_handler(client, message):
    await message.reply_photo(
        photo="https://files.catbox.moe/g37dvh.png",
        caption=f"👋 Hello {message.from_user.mention},\n\n🌟 *Welcome to StarEntryBot!*\n\nUnlock premium content by sending stars ⭐",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("💬 Contact Admin", url=f"https://t.me/{OWNER_USERNAME}")]]
        )
    )
