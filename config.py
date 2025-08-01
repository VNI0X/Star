import os

# Required Values
API_ID = int(os.getenv("API_ID", "23961027"))
API_HASH = os.getenv("API_HASH", "f3add6d66bd20a3ae78e385e81f1df8a")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7925420715:AAH755d3r1StHZWVCdnC5pwQbAkyM9aIns8")

# Bot Owner / Admin ID
ADMIN_ID = int(os.getenv("ADMIN_ID", "6972508083"))
OWNER_USERNAME = "VNI0X"  # 🔥 Ye line add karni thi

# How many stars are needed to unlock content
REQUIRED_STARS = 1

# Unlockable content message
UNLOCK_MESSAGE = f"""
🎉 Congratulations!

You've unlocked the premium content. Here's your access:

👉 [Click Here to Access](https://example.com/premium-content)

⭐ Required: {REQUIRED_STARS} Stars
"""

# Giveaway toggle
ENABLE_GIVEAWAY = True

# Logging (True to log actions in DB or file)
ENABLE_LOGGING = True

# Your payment/gift link (where users send stars)
GIFT_LINK = "https://t.me/StarEntryBot?start=gift"

# Message shown to users before unlocking
WELCOME_MESSAGE = f"""
👋 Hello {{user}},

Welcome to Star Entry Bot! 🚀

To unlock premium content, please send ⭐ {REQUIRED_STARS} Star(s).

Once done, type `/unlocked` to check your status.

{{gift}}
"""
