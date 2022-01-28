from pyrogram import filters
from tg_bot import OWNER_ID, logger
from tg_bot.tg_bot import TG_UBOT as ubot


async def send_msg(client, message, text):
    if message.from_user.id == OWNER_ID:
        message.delete()
        await message.reply(text)
    else:
        await message.edit_text(text)


@ubot.on_message(
    (filters.me | filters.user(OWNER_ID))
    & filters.command(["alive", "start"], ["/", "."])
)
async def alive_msg(client, message):
    await send_msg(
        client,
        message,
        "<b>Hey ya, I'm Alive 🙌</b>\n send <code>/help</code> to see avaliable commands" )


@ubot.on_message(
    (filters.me | filters.user(OWNER_ID))
    & filters.command("help", ["/", "."])
)
async def help_msg(client, message):
    await send_msg(
        client,
        message,
        "\n\n🤖 <b>Avaliable Commands:</b>\n- /alive or /start: to check if bot is alive\n- /join or /add: followed by channel link or username\n- /leave or /remove: followed by channel link or username\n\n <b>You can Prefix commands with / or .</b>",
 )



@ubot.on_message(
    (filters.me | filters.user(OWNER_ID)) & filters.command(["join", "add"], ["/", "."])
)
async def join_channel(client, message):
    if len(message.command) != 2:
    	await send_msg(client, message, "⚠ Please use <b>/join or /add:</b> followed by channel <u>link</u> or <u>username</u>\ni.e: <code>/add @telegram</code>")
    	return
    try:
        await send_msg(
            client,
            message,
            f"🔄 <b>Trying to Join:</b>\n<code>{message.command[-1]}</code>",
        )
        await client.join_chat(message.command[-1].strip("@"))
        await send_msg(
            client, message, f"✅ <b>Joined:</b>\n<code>{message.command[-1]}</code>"
        )
    except Exception as e:
        await send_msg(client, message, f"❌ <b>Error</b>\n{e}")
        logger.error(e)


@ubot.on_message(
    (filters.me | filters.user(OWNER_ID))
    & filters.command(["leave", "remove"], ["/", "."])
)
async def leave_channel(client, message):
    if len(message.command) != 2:
    	await send_msg(client, message, "⚠ Please use <b>/leave or /remove:</b> followed by <u>username</u>\ni.e: <code>/remove @telegram</code>")
    	return
    try:
        await send_msg(
            client,
            message,
            f"🔄 <b>Trying to Leave:</b>\n<code>{message.command[-1]}</code>",
        )
        await client.leave_chat(message.command[-1].strip("@"))
        await send_msg(
            client, message, f"✅ <b>Left:</b>\n<code>{message.command[-1]}</code>"
        )
    except Exception as e:
        await send_msg(client, message, f"❌ <b>Error:</b>\n{e}")
        logger.error(e)
