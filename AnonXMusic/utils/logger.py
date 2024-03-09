from pyrogram.enums import ParseMode

from AnonXMusic import app
from AnonXMusic.utils.database import is_on_off
from config import LOGGER_ID


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""**⋖━⦿═⊷〩ᴠᴇɢᴀ々ᴍᴜsɪᴄ〩⊷⦿━⋗
<b>╭⦿<b>{app.mention}
<b>╰⦿ᴘʟᴀʏ ⸢ᴠᴇɢᴀ⸥ ᴍᴜsɪᴄ♪</b>

<b>╭⦿ᚐᴄʜᴀᴛ ɴᴀᴍᴇ :</b> {message.chat.title}
<b>╰⦿ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.chat.username}

<b>╭⦿ᚐɴᴀᴍᴇ :</b> {message.from_user.mention}
<b>╰⦿ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}

<b>╭⦿ǫᴜᴇʀʏ :</b> {message.text.split(None, 1)[1]}
<b>╰⦿sᴛʀᴇᴀᴍᴛʏᴘᴇ :</b> {streamtype}
⋖━⦿═⊷〩ᴠᴇɢᴀ々ᴍᴜsɪᴄ〩⊷⦿━⋗**"""
        if message.chat.id != LOGGER_ID:
            try:
                await app.send_message(
                    chat_id=LOGGER_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return