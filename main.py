from discord.ext import commands
from threading import Thread
from asyncio import sleep 
from pytz import timezone
from datetime import datetime as dt
tz = timezone('US/Arizona')

import data_grabber
import diff_parser

# Try to get tokenfile
# If we don't find it, then exit

try:
    token = open('tokenfile.txt').read()
except:
    print("Can't find token file, aborting")
    exit()

bot = commands.Bot(command_prefix='.') # set prefix
bot.remove_command('help') # remove command to make our own

bot.current_status = None

bot.sleep_time = 900

# Status and Help commands

@bot.command()
async def status(ctx):
    status_msg = f"""\
**Bot Bucket**
**Status**: {bot.current_status}
**Time**: {dt.now(tz)}
"""
    await ctx.send(status_msg)

@bot.command()
async def help(ctx):
    help_msg = f"""\
**Bot Bucket**
Commands:
```
.help:   Show this message
.status: View bot's current status
```
Shopping updates are posted in <#{bot.channel_id}>
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

        for discord_msg in list_discord_msg:
            if discord_msg: # Don't send it if it's None
                # Makes sure we don't get yeeted if a thing is more than 2000 chars
                [await bot.channel.send(discord_msg[i: i + 1990]) for i in range(0, len(discord_msg), 1990)]

        bot.current_status = "Sleeping"
        await sleep(bot.sleep_time)
            
@bot.event
async def on_ready():

    #server id: 525065737749135360
    #test id: 580553067511152670
    bot.channel_id = 525065737749135360
    bot.channel = bot.get_channel(bot.channel_id)

    # get inital data and establish connection
    bot.current_status = "Getting initial data"
    data_grabber.get_init_data(bot)

    # We send ready messages to personal server and not real since it keeps restarting, which causes confusion and clutters up the channel

    ready_msg = f"""\
Shopping bot up!
Time: {dt.now(tz)}
"""
    ready_msg_channel = bot.get_channel(580553067511152670)

    # Bot is fully up now
    print(ready_msg)
    await ready_msg_channel.send(ready_msg)

    # When it's connected to Discord, start the main function
    await main()

bot.run(token, bot=True)