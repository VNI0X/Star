import json
import os
from pyrogram import Client, filters
from pyrogram.types import Message

DATA_FILE = "giveaway_data.json"

# Load or initialize data
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        giveaway_data = json.load(f)
else:
    giveaway_data = {}

def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(giveaway_data, f)

@Client.on_message(filters.command("star") & filters.private)
async def add_star(client, message: Message):
    user_id = str(message.from_user.id)
    if user_id not in giveaway_data:
        giveaway_data[user_id] = 1
    else:
        giveaway_data[user_id] += 1

    save_data()
    await message.reply(f"⭐ 1 Star added!\nTotal Stars: {giveaway_data[user_id]}")

@Client.on_message(filters.command("giveaway") & filters.user(6972508083))  # Vishal bhai only
async def show_top_users(client, message: Message):
    if not giveaway_data:
        await message.reply("❌ No star data available yet.")
        return

    sorted_users = sorted(giveaway_data.items(), key=lambda x: x[1], reverse=True)
    top_list = ""

    for i, (uid, stars) in enumerate(sorted_users[:10], 1):
        mention = f"<a href='tg://user?id={uid}'>User</a>"
        top_list += f"{i}. {mention} – {stars}⭐\n"

    await message.reply(f"🎉 <b>Top Star Contributors</b>:\n\n{top_list}", parse_mode="html")
