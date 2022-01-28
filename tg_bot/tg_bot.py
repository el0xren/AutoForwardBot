from pyrogram import Client
from pyrogram import __version__
from pyrogram.raw.all import layer

from tg_bot import logger
from tg_bot import APP_ID, API_HASH, SESSION


class TG_UBOT(Client):
    def __init__(self):
        super().__init__(
            SESSION,
            plugins=dict(root="tg_bot/uplugins"),
            api_id=APP_ID,
            api_hash=API_HASH,
        )

    async def start(self):
        await super().start()

        bot_me = await self.get_me()
        self.set_parse_mode("html")
        logger.info(
            f"UserBot based on Pyrogram v{__version__} "
            f"(Layer {layer}) started on @{bot_me.username}. "
        )

    async def stop(self, *args):
        await super().stop()
        logger.info("UserBot stopped. Bye.")
