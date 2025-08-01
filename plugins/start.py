# plugins/start.py

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import OWNER_USERNAME

@Client.on_message(filters.command("start") & filters.private)
async def start_handler(client, message):
    await message.reply(
        text=f"""👋 Hello {message.from_user.mention},

Welcome to **StarEntryBot** ✨

🎁 Send a 'Star' to unlock exclusive content!

📢 Premium content is posted in our channel.""",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📢 Join Channel", url="https://t.me/heroku_culb")],
            [InlineKeyboardButton("💬 Contact Admin", url=f"https://t.me/{OWNER_USERNAME}")]
        ])
    )
