import json
import os
from pyrogram import Client, filters
from pyrogram.types import Message

DATA_FILE = "giveaway_data.json"
REQUIRED_STARS = 3  # Minimum Stars required to unlock

# Load star data
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        giveaway_data = json.load(f)
else:
    giveaway_data = {}

def has_enough_stars(user_id: int) -> bool:
    return str(user_id) in giveaway_data and giveaway_data[str(user_id)] >= REQUIRED_STARS

@Client.on_message(filters.command("check") & filters.private)
async def check_stars(client, message: Message):
    user_id = message.from_user.id
    if has_enough_stars(user_id):
        await message.reply("✅ You have enough Stars! Premium access granted.")
    else:
        current = giveaway_data.get(str(user_id), 0)
        await message.reply(
            f"❌ You only have {current}⭐.\nYou need {REQUIRED_STARS}⭐ to unlock content.\n\n"
            "Send more Stars to access premium content."
                                       )
