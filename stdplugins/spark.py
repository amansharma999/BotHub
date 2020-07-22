#made by @xcruzhd2
""" displays the Truth
use cmd .ok"""

from telethon import events

import asyncio

from uniborg.util import admin_cmd

@borg.on(admin_cmd("(.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.05
    animation_ttl = range(0, 90)
    input_str = event.pattern_match.group(1)
    if input_str == "spark":
        await event.edit(input_str)
        animation_chars = [
            "S",
            "P",
            "A",
            "R",
            "K",
            "E",
            "S",
            "P",
            "I"
            "S"
            "T",
            "H",
            "E",
            "B",
            "E",
            "S",
            "T",
            "SPARK ESP IS THE BEST"
        ]

        for i in animation_ttl:
        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 78])
