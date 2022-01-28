from pyrogram import filters
from tg_bot import OWNER_ID, logger
from tg_bot.tg_bot import TG_UBOT as ubot


async def send_msg(client, message, text):
    if message.from_user.id == OWNER_ID:
        await message.delete()
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
        "<b>Hey ya, I'm Alive 🙌</b>\n send <code>/help</code> to see avaliable commands",
    )


@ubot.on_message(
    (filters.me | filters.user(OWNER_ID)) & filters.command("help", ["/", "."])
)
async def help_msg(client, message):
    help_text = """
🤖 <b>Avaliable Commands:</b>

- <b>/alive or /start</b>: to check if bot is alive.
- <b>/join or /add</b>: followed by channel <u>link</u> or <u>username</u>.
- <b>/leave or /remove</b>: followed by channel <u>username</u>.
- <b>/chatid or /getchatid</b>: followed by channel <u>link</u> or <u>username</u>.

<b>You can Prefix commands with / or .</b>",
  
    """
    await send_msg(client, message, help_text)


@ubot.on_message(
    (filters.me | filters.user(OWNER_ID)) & filters.command(["join", "add"], ["/", "."])
)
async def join_channel(client, message):
    if len(message.command) != 2:
        await send_msg(
            client,
            message,
            "⚠ Please use <b>/join or /add:</b> followed by channel <u>link</u> or <u>username</u>\ni.e: <code>/add @telegram</code>",
        )
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
        await send_msg(
            client,
            message,
            "⚠ Please use <b>/leave or /remove:</b> followed by <u>username</u>\ni.e: <code>/remove @telegram</code>",
        )
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


@ubot.on_message(
    (filters.me | filters.user(OWNER_ID))
    & filters.command(["chatid", "getchatid"], ["/", "."])
)
async def get_chat_id(client, message):
    if len(message.command) != 2:
        await send_msg(
            client,
            message,
            "⚠ Please use <b>/chatid or /getchatid:</b> followed by <u>username</u> or <u>link</u>\ni.e: <code>/id @telegram</code>",
        )
        return
    try:
        await send_msg(
            client,
            message,
            f"🔄 <b>Trying get chat id:</b>\n<code>{message.command[-1]}</code>",
        )
        try:
            await join_channel(client, message)
        except Exception as e:
            raise Exception(e)
        chat = await client.get_chat(message.command[-1].strip("@"))
        await send_msg(client, message, f"✅ <b>ID:</b>\n<code>{chat.id}</code>")
    except Exception as e:
        await send_msg(client, message, f"❌ <b>Error:</b>\n{e}")
        logger.error(e)


@ubot.on_message(
    (filters.me | filters.user(OWNER_ID))
    & filters.command(["id", "getuserid"], ["/", "."])
)
async def get_user_id(client, message):
    target_msg = message.reply_to_message if message.reply_to_message else message
    await send_msg(
        client,
        message,
        f"<b>{target_msg.from_user.first_name}'s</b> ID is <code>{target_msg.from_user.id}</code>",
    )


@ubot.on_message(
    (filters.me | filters.user(OWNER_ID)) & filters.command("pchatid", ["/", "."])
)
async def get_chat_id_from_link(client, message):
    if len(message.command) != 2:
        await send_msg(
            client,
            message,
            "⚠ Please use <b>/chatid or /getchatid:</b> followed by <u>username</u> or <u>link</u>\ni.e: <code>/id @telegram</code>",
        )
        return
    try:
        await send_msg(
            client,
            message,
            f"🔄 <b>Trying get chat id:</b>\n<code>{message.command[-1]}</code>",
        )
        _, msg_data = message.command[-1].split("/c/")
        ch_id, msg_id = msg_data.split("/")
        ch_id_int = int(f"-100{ch_id}")
        target_message = await client.get_messages(ch_id_int, msg_id)
        await send_msg(
            client, message, f"✅ <b>ID:</b>\n<code>{target_message} .chat.id</code>"
        )
    except Exception as e:
        await send_msg(client, message, f"❌ <b>Error:</b>\n{e}")
        logger.error(e)
