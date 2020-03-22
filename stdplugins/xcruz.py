"""COMMAND : .xcru"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "xcru":

        await event.edit(input_str)

        animation_chars = [

            "✋🏻\n  =====> 👉HI 🤗🤗🙂🙂🙂 ",
            "✋🏻\n  =====> 👉👉How Are You Guys😙😙😙 ",    
            "✋🏻\n  =====> 😎I am xcruzhd2 😎 ",
            "✋🏻\n  =====> 👉👉👉 ❤️ MODSEC ",
            "✋🏻\n  =====> 👉👉👉❤️TCA ",    
            "✋🏻\n  =====> 👉👉👉❤️LEETCOOL BRO  👑 ",
            "✋🏻\n  =====> 👉👉👉❤️ ILLUSIONIST BRO 👑 ",
            "✋🏻\n  =====> 👉👉👉 ❤️ HEWHONOTMUSTBENAMED 👑 ",    
            "✋🏻\n  =====> 👉👉👉 ❤️ BUTMAYURISPRINCEANYWAYS 👑"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 9])