from pyrogram import Client, filters
from pyrogram.types import Message

LOG_CHAT_ID = 6972508083  # Vishal bhai ka Telegram ID

@Client.on_message(filters.command("start") & filters.private)
async def log_start(client, message: Message):
    user = message.from_user
    mention = user.mention
    user_id = user.id
    username = f"@{user.username}" if user.username else "No Username"

    log_text = (
        f"🚀 <b>New User Started Bot</b>\n\n"
        f"👤 Name: {mention}\n"
        f"🆔 ID: <code>{user_id}</code>\n"
        f"🔗 Username: {username}\n"
        f"📩 Message: {message.text}"
    )

    try:
        await client.send_message(LOG_CHAT_ID, log_text)
    except Exception as e:
        print(f"❌ Failed to send log: {e}")
