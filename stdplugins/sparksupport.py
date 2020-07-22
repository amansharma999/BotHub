""" plugin for   spark support  made by @xcruzhd2"""

from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from platform import python_version, uname
from shutil import which
from os import remove
from telethon import version
from random import randint
from asyncio import sleep
from os import execl
import sys
import os
import io
import sys
import json
from sample_config import Config
from uniborg.util import admin_cmd
import uniborg


# ================= CONSTANT =================
DEFAULTUSER = Config.ALIVE_NAME if Config.ALIVE_NAME else uname().node
# ============================================


@borg.on(admin_cmd(pattern="sparksupport ?(.*)"))
async def follow(follow):
    """ For .support command, check if the bot is running.  """
    await follow.edit(
                     f"`SPARK SUPPORT` \n\n"
                     f"[SparkLoader](https://sparkcheats.tech) \n\n"
                     f"[OUR OFFICIAL CHANNEL ](https://t.me/sparkcheats) \n\n"
                     f"[OUR OFFICIAL GROUP](https://t.me/sparkcheatsofficial)"
                     )    

