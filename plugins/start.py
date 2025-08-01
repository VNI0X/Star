from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import OWNER_USERNAME

@Client.on_message(filters.command("start") & filters.private)
async def start_handler(client, message):
    await message.reply(
        text=(
            f"👋 Hello {message.from_user.mention},\n\n"
            "Welcome to 💫 StarEntryBot!\n"
            "Yahaan aap *Star* dekar premium content unlock kar sakte ho.\n\n"
            "⭐ Send a Star & Unlock your access!"
        ),
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("💬 Contact Admin", url=f"https://t.me/{OWNER_USERNAME}")]]
        )
    )
