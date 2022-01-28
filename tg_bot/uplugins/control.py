from pyrogram import filters
from tg_bot import OWNER_ID
from tg_bot.tg_bot import TG_UBOT as ubot


async def send_msg(client, message, text):
    if message.from_user.id == OWNER_ID:
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
        "Hi, I'm Alive 🙌\n\n<b>Avaliable Commands:</b>\n- /alive or /start: to check if bot is alive\n- /join or /add: folowed by channel link or username\n- leave or remove: followed by channel link or username\n\n <b>You can Prefix commands with / or .</b>",
    )


@ubot.on_message(
    (filters.me | filters.user(OWNER_ID)) & filters.command(["join", "add"], ["/", "."])
)
async def join_channel(client, message):
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


@ubot.on_message(
    (filters.me | filters.user(OWNER_ID))
    & filters.command(["leave", "remove"], ["/", "."])
)
async def leave_channel(client, message):
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
