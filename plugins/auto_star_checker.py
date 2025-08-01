import json
import os
from pyrogram import Client, filters
from pyrogram.types import Message

# JSON File Path
JSON_FILE = "plugins/giveaway.json"

# Ensure the file exists with basic structure
if not os.path.exists(JSON_FILE) or os.path.getsize(JSON_FILE) == 0:
    with open(JSON_FILE, "w") as f:
        f.write("{}")

# Load JSON data safely
with open(JSON_FILE, "r") as f:
    try:
        giveaway_data = json.load(f)
    except json.JSONDecodeError:
        giveaway_data = {}

# Example handler (you can customize this)
@Client.on_message(filters.command("stars") & filters.private)
async def check_stars(client, message: Message):
    user_id = str(message.from_user.id)
    stars = giveaway_data.get(user_id, 0)
    await message.reply(f"🌟 You have {stars} stars.")

# Add more handlers below if needed
