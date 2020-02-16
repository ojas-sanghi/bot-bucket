from discord.ext import commands
from threading import Thread
from asyncio import sleep

from pytz import timezone
from datetime import datetime as dt
tz = timezone('US/Arizona')

import shopping.data_grabber as data_grabber
import shopping.diff_parser as diff_parser
import global_vars
from global_vars import bot

# Status and Help commands

@bot.command()
async def status(ctx):
    print("status")
    status_msg = f"""\
**Bot Bucket**
**Status**: {bot.current_status}
**Time**: {dt.now(tz).strftime("%c")}
"""
    await ctx.send(status_msg)

@bot.command(name="help")
async def help_msg(ctx):
    print("help")
    help_msg = f"""\
**Bot Bucket**
Commands:
```
.help:   Show this message
.status: View bot's current status
```
Shopping updates are posted in <#{bot.shopping_channel_id}>
"""
    await ctx.send(help_msg)

async def main():

    while True:

        # Get diff results bro
        bot.current_status = "Getting new data"
        diff_results = await data_grabber.get_data(bot)

        # Parse results
        bot.current_status = "Parsing changes"
        bot.all_differences = diff_parser.do_everything(diff_results)
        list_discord_msg = bot.all_differences

        if global_vars.USE_TEST_SHEET:
            channel = bot.test_channel
        else:
            channel = bot.shopping_channel

        for discord_msg in list_discord_msg:
            if discord_msg: # Don't send it if it's None
                # Makes sure we don't get yeeted if a thing is more than 2000 chars
                [await channel.send(discord_msg[i: i + 1990]) for i in range(0, len(discord_msg), 1990)]

        bot.current_status = "Sleeping"
        await sleep(bot.sleep_time)
            
async def initialize_shopping():

    # get inital data and establish connection
    bot.current_status = "Getting initial data"
    data_grabber.get_init_data(bot)

    # When it's connected to Discord, start the main function
    await main()