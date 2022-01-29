import os
from pyrogram import filters
from tg_bot import DUMP_CHANNEL, CHANNELS, logger
from tg_bot.tg_bot import TG_UBOT as ubot


@ubot.on_message(
    filters.chat(CHANNELS)
    & filters.channel
    & ~filters.chat(DUMP_CHANNEL)
    & ~filters.edited
    & ~filters.reply
)
async def msg_forward(client, message):
    cap = message.caption if message.caption else text
    if cap:
        try:
            await client.send_message(DUMP_CHANNEL, cap)
        except Exception as e:
            logger.error(e)
    return
    file_path = ""
    try:
        if message.document:
            file_path = await message.download()
            await client.send_document(DUMP_CHANNEL, file_path, cap)
        elif message.photo:
            file_path = await message.download()
            await client.send_photo(DUMP_CHANNEL, file_path, cap)
        elif message.video:
            file_path = await message.download()
            await client.send_video(DUMP_CHANNEL, file_path, cap)
        elif message.voice:
            file_path = await message.download()
            await client.send_voice(DUMP_CHANNEL, file_path, cap)
        elif message.audio:
            file_path = await message.download()
            await client.send_audio(DUMP_CHANNEL, file_path, cap)
        elif message.animation:
            file_path = await message.download()
            await client.send_animation(DUMP_CHANNEL, file_path, cap)
        elif message.sticker:
            file_path = await message.download()
            await client.send_sticker(DUMP_CHANNEL, file_path)
        elif message.video_note:
            file_path = await message.download()
            await client.send_video_note(DUMP_CHANNEL, file_path)
    except Exception as e:
        logger.error(e)
    try:
        os.remove(file_path)
    except:
        logger.error("failed to delete downloaded file")
