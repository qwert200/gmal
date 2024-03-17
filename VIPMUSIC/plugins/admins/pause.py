from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from VIPMUSIC import app
from VIPMUSIC.core.call import VIP
from VIPMUSIC.utils.database import is_music_playing, music_off
from VIPMUSIC.utils.decorators import AdminRightsCheck
from VIPMUSIC.utils.inline import close_markup
from config import BANNED_USERS

@app.on_message(filters.command(["وقف", "pause","اسكت","ايقاف مؤقت"] ,prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await VIP.pause_stream(chat_id)
    
    buttons = [
        [
            InlineKeyboardButton(text="𝙍𝙚𝙨𝙪𝙢𝙚", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="𝙍𝙚𝙥𝙡𝙖𝙮", callback_data=f"ADMIN Replay|{chat_id}"),
        ],
    ]
    
    await message.reply_text(
        _["admin_2"].format(message.from_user.mention), reply_markup=InlineKeyboardMarkup(buttons)
    )
