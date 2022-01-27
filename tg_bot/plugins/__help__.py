from pyrogram import filters

from tg_bot.tg_bot import TG_BOT as tbot
from tg_bot.tg_bot import TG_UBOT as ubot

#from tg_bot import POST_CHANNEL


@tbot.on_message(filters.command(["start"]))
async def start(bot, update):
    text = "Hey ya, I'm Alive!"
    await bot.send_message(
        chat_id=update.chat.id,
        text=text,
        reply_to_message_id=update.message_id,
    )