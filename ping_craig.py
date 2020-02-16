from discord.ext import commands
from asyncio import sleep

import global_vars
from global_vars import bot

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if not global_vars.PING_CRAIG_MODE:
        return
    
    if message.author.id != global_vars.GITHUB_BOT_ID:
        return

    embed = message.embeds[0]
    embed_title = embed.title

    if embed_title.startswith("[BitBucketsFRC4183/FRC2020_Infinite_Recharge] Pull request opened:"):
        sent_ping_message = await bot.ping_channel.send("<@" + str(global_vars.CRAIG_USER_ID) + ">")