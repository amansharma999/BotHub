""" Userbot module for getting information about the spark tutorial. 
made by @xcruzhd2"""

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


DEFAULTUSER = Config.ALIVE_NAME if Config.ALIVE_NAME else uname().node



@borg.on(admin_cmd(pattern="sparktut ?(.*)"))
async def follow(follow):
    """ For .sparktutorial command, check if the bot is running.  """
  #  client.parse_mode = 'html'
    await follow.edit(
                     
                     f"[How to use sparkloader](https://t.me/sparkcheats/72)"
                     )    

