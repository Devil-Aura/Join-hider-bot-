from pyrogram import Client, filters
from pyrogram.types import Message

# --- Bot Settings ---
API_ID = 35728174  # your api id
API_HASH = "your_api_hash"  # your api hash
BOT_TOKEN = "your_bot_token"  # your bot token

# --- Create Client ---
app = Client(
    "JoinLeftDeleteBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# --- Delete Join, Left, and Approval Messages ---
@app.on_message(filters.group, group=-1)
async def auto_delete(client, message: Message):
    if (
        message.new_chat_members or
        message.left_chat_member or
        (message.sender_chat and message.sender_chat.id == message.chat.id)  # approval messages
    ):
        try:
            await message.delete()
        except:
            pass  # Ignore errors silently (e.g., no permission)

# --- Run Bot ---
app.run()
