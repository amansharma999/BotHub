"""use cmd .xcruzhd2
aaahaaa you can edit this 😉"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 30)

    input_str = event.pattern_match.group(1)

    if input_str == "xcruzhd2":

        await event.edit(input_str)

        animation_chars = [

            "👑xcruzhd2👑👑👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑",

            "◼️👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑",

            "◼️◼️👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑",

            "◼️◼️◼️️👑xcruzhd2👑👑xcruzhd2👑\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑",

            "◼️◼️◼️◼️👑xcruzhd2👑\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑",

            "‎◼️◼️◼️◼️◼️\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑",

            "◼️◼️◼️◼️◼️\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑",

            "◼️◼️◼️◼️◼️\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑",

            "◼️◼️◼️◼️◼️\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑",

            "◼️◼️◼️◼️◼️\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️",

            "◼️◼️◼️◼️◼️\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️◼️",

            "◼️◼️◼️◼️◼️\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n👑xcruzhd2👑👑xcruzhd2👑◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n👑xcruzhd2👑◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n◼️👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n◼️👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n◼️👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n◼️👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n◼️👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️👑xcruzhd2👑👑xcruzhd2👑◼️\n◼️👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n◼️👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️👑xcruzhd2👑◼️\n◼️👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n◼️👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n◼️👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑xcruzhd2👑👑xcruzhd2👑◼️◼️\n◼️👑xcruzhd2👑👑xcruzhd2👑👑xcruzhd2👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑xcruzhd2👑👑xcruzhd2👑◼️◼️\n◼️👑xcruzhd2👑👑xcruzhd2👑◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑xcruzhd2👑👑xcruzhd2👑◼️◼️\n◼️👑xcruzhd2👑◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑xcruzhd2👑👑xcruzhd2👑◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️👑xcruzhd2👑◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️",

            "◼️◼️◼️\n◼️◼️◼️\n◼️◼️◼️",

            "◼️◼️\n◼️◼️",

            "◼️",
            "👑 xcruzhd2 👑"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 31])