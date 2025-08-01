import os

API_ID = int(os.getenv("API_ID", "23961027"))
API_HASH = os.getenv("API_HASH", "f3add6d66bd20a3ae78e385e81f1df8a")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7925420715:AAH755d3r1StHZWVCdnC5pwQbAkyM9aIns8")

OWNER_ID = int(os.getenv("OWNER_ID", "6972508083"))  # ✅ Add this line
OWNER_USERNAME = "VNI0X"

REQUIRED_STARS = 1
UNLOCK_MESSAGE = f"""
🎉 Congratulations!

You've unlocked the premium content. Here's your access:

👉 [Click Here to Access](https://example.com/premium-content)

⭐ Required: {REQUIRED_STARS} Stars
"""

ENABLE_GIVEAWAY = True
ENABLE_LOGGING = True
GIFT_LINK = "https://t.me/StarEntryBot?start=gift"

WELCOME_MESSAGE = f"""
👋 Hello {{user}},

Welcome to Star Entry Bot! 🚀

To unlock premium content, please send ⭐ {REQUIRED_STARS} Star(s).

Once done, type `/unlocked` to check your status.

{{gift}}
"""
