from pyrogram import Client, filters
from pyrogram.types import Message

# --- Config ---
API_ID = 22768311  # your api id
API_HASH = "702d8884f48b42e865425391432b3794"
BOT_TOKEN = "your_bot_token"

# --- Create Bot ---
app = Client(
    "JoinLeftApprovalDeleteBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# --- Delete Join/Left/Approved messages ---
@app.on_message(filters.group & (filters.new_chat_members | filters.left_chat_member))
async def delete_join_left(client, message: Message):
    try:
        await message.delete()
    except Exception as e:
        print(f"Failed to delete message: {e}")

# --- Run Bot ---
app.run()
