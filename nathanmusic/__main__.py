import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from nathanmusic import LOGGER, app, userbot
from nathanmusic.core.call import Anony
from nathanmusic.misc import sudo
from nathanmusic.plugins import ALL_MODULES
from nathanmusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("nathanmusic.plugins" + all_module)
    LOGGER("nathanmusic.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Anony.start()
    try:
        await Anony.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("nathanmusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Anony.decorators()
    LOGGER("nathanmusic").info(
        "NathanMusic Bot started sucsesfully."
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("nathanmusic").info("Stopping Nathan Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
