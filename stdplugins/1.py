"""Fun pligon...for HardcoreUserbot
\nCode by @Rambo_86
type `.1` and `.A1` to see the fun.
"""
import random, re
from uniborg.util import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="1 ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("Teri ammy ke choot mei earphone laga ke gaane sununga maderchod")
        await asyncio.sleep(0.7)
        await event.edit("gand mei powder laga ke chodunga teri behn ko")
        await asyncio.sleep(1)
        await event.edit("darwaje ke beech mei ungli laga ke daba dunga teri behn ke")
        await asyncio.sleep(0.8)
        await event.edit("muh pe apna loda thap thapa dunga teri behn ke")
        await asyncio.sleep(0.9)
        await event.edit("brush se saaf krke pelung teri ammy ki choot")
        await asyncio.sleep(1)
        await event.edit("kursi pe baitha ke gand mei loda dal dunga tere pure khandan ke")
        await asyncio.sleep(0.8)
        await event.edit("tange tod dunga teri maderchod mil tu mere ko")
        await asyncio.sleep(0.7)
        await event.edit("teri behn ka boxda bohot charge rehta hai usme apna charger laga ke phone charge krlunga")
        await asyncio.sleep(1)
        await event.edit("`tere ammy ke gand mei morpankhi laga dunga`")
        await asyncio.sleep(0.7)
        await event.edit("`Gand mei kante wale pudhe laga dunga teri behn ke`")
        await event.edit("𝐀𝐁 𝐁𝐀𝐀𝐏 𝐊 𝐌𝐔𝐇 𝐌𝐀𝐓 𝐋𝐀𝐆𝐀𝐍𝐀 𝐁𝐄𝐓𝐄 𝐘𝐄 𝐓𝐄𝐋𝐄𝐑 𝐇𝐀𝐈𝐍 🎃🤣`")
        await asyncio.sleep(1)
        
@borg.on(events.NewMessage(pattern=r"\.A1", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("`𝙋𝙄𝘾𝙏𝙐𝙍𝙀 𝘾𝙃𝘼𝙃𝙄𝙔𝙀 𝙏𝙊 𝘼𝙋𝙉𝙄 𝙈𝘼𝘼 𝙆𝙊 𝙈𝙀𝙍𝙀 𝙋𝘼𝘼𝙎 𝘽𝙃𝙀𝙅 𝘿𝙀 🤣🤣`")
    await asyncio.sleep(999)
