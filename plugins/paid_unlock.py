import json
import os
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

# JSON file jisme star data save hoga
DATA_FILE = "giveaway_data.json"
REQUIRED_STARS = 3  # Kitne Stars chahiye unlock ke liye

# Premium content (yahan aap link, file, ya message dal sakte ho)
PREMIUM_CONTENT = "🎉 Congratulations! You've unlocked the premium content!\n👉 https://t.me/your_channel/123"

# Load star data
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        giveaway_data = json.load(f)
else:
    giveaway_data = {}

def has_enough_stars(user_id: int) -> bool:
    return str(user_id) in giveaway_data and giveaway_data[str(user_id)] >= REQUIRED_STARS

@Client.on_message(filters.command("unlock") & filters.private)
async def unlock_premium(client, message: Message):
    user_id = message.from_user.id

    if has_enough_stars(user_id):
        await message.reply(
            PREMIUM_CONTENT,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("💎 Join Premium Channel", url="https://t.me/your_channel")]
            ])
        )
    else:
        current = giveaway_data.get(str(user_id), 0)
        await message.reply(
            f"❌ You only have {current}⭐.\nYou need {REQUIRED_STARS}⭐ to unlock this content.\n\n"
            "Please send more Stars to unlock access!"
        )
