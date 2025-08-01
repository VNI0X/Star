from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID

# ✅ Manually unlock command by admin
@Client.on_message(filters.command("unlock") & filters.user(OWNER_ID))
async def unlock_access(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply karo us user ke message pe jisko unlock dena hai.")

    user_id = message.reply_to_message.from_user.id
    try:
        # Send confirmation to user
        await client.send_message(
            user_id,
            "🎉 Aapka access unlock ho gaya hai!\nEnjoy your premium content!"
        )
