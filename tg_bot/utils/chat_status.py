from tg_bot import OWNER_ID

async def owner_cmd(update):
    if int(update.from_user.id) == int(OWNER_ID):
        return True
    else:
        return False
