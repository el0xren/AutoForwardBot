from pyrogram import filters
from tg_bot import DUMP_CHANNEL
from tg_bot.tg_bot import TG_UBOT as ubot

@ubot.on_message(filters.channel & ~filters.chat(DUMP_CHANNEL))
async def scammer(client, message):
    if message.text:
        await message.copy(DUMP_CHANNEL)
    elif message.document:
       file_path = await message.download()
       await client.send_document(DUMP_CHANNEL, file_path)
    elif message.photo:
       file_path = await message.download()
       await client.send_photo(DUMP_CHANNEL, file_path)
    elif message.video:
       file_path = await message.download()
       await client.send_video(DUMP_CHANNEL, file_path)
    elif message.voice:
       file_path = await message.download()
       await client.send_voice(DUMP_CHANNEL, file_path)
    elif message.audio:
       file_path = await message.download()
       await client.send_audio(DUMP_CHANNEL, file_path)
    elif message.animation:
       file_path = await message.download()
       await client.send_animation(DUMP_CHANNEL, file_path)
    elif message.sticker:
       file_path = await message.download()
       await client.send_sticker(DUMP_CHANNEL, file_path)
    elif message.video_note:
       file_path = await message.download()
       await client.send_video_note(DUMP_CHANNEL, file_path)
    else:
    	print(message)
    	
    	