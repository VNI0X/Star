
API_ID = 23961027 API_HASH = "f3add6d66bd20a3ae78e385e81f1df8a" BOT_TOKEN = "8463222827:AAG8e8qf0i--HsOQKqn6pRkebKpFtvTC1bw" OWNER_ID = 6972508083 OWNER_USERNAME = "VNI0X"

requirements.txt

pyrogram==2.0.106 tgcrypto

bot.py

from pyrogram import Client from config import API_ID, API_HASH, BOT_TOKEN import plugins.start

app = Client( "StarEntryBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins={"root": "plugins"} )

app.run()

plugins/start.py

from pyrogram import Client, filters from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton from config import OWNER_USERNAME

@Client.on_message(filters.command("start") & filters.private) async def start_handler(client, message): await message.reply( text=f"👋 Hello {message.from_user.mention},\nWelcome to the bot!", reply_markup=InlineKeyboardMarkup([ [InlineKeyboardButton("💬 Contact Admin", url=f"https://t.me/{OWNER_USERNAME}")] ]) )

