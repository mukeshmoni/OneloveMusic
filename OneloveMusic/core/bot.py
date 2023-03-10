import sys

from pyrogram import Client

import config

from ..logging import LOGGER


class OneloveBot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Beats...")
        super().__init__(
            "MusicBot",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        try:
            await self.send_message(
                config.LOG_GROUP_ID, "ยป ๐งโโโโโ๐ชโโโโโ๐ฆโโโโโ๐นโโโโโ๐ธโโโโโ ๐ธโโโโโ๐นโโโโโ๐ฆโโโโโ๐ทโโโโโ๐นโโโโโ๐ชโโโโโ๐ฉโโโโ,โ ๐ผโโโโโ๐ฆโโโโโ๐ฎโโโโโ๐นโโโโโ๐ฎโโโโโ๐ณโโโโโ๐ฌโโโโโ ๐ซโโโโโ๐ดโโโโโ๐ทโโโโโ ๐งโโโโโ๐ฑโโโโโ๐ดโโโโโ๐ดโโโโโ๐ฉโโโโโ ๐ซโโโโโ๐ฑโโโโโ๐ดโโโโโ๐ผโโโโโ..."
            )
        except:
            LOGGER(__name__).error(
                "Bot has failed to access the log Group. Make sure that you have added your bot to your log channel and promoted as admin!"
            )
            sys.exit()
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != "administrator":
            LOGGER(__name__).error("Thambi Thappu Panitaa da..........")
            sys.exit()
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER(__name__).info(f"MusicBot Started as {self.name}")
