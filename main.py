import os

from discord.ext import commands

import global_vars

from pytz import timezone
from datetime import datetime as dt
tz = timezone('US/Arizona')

# Try to get tokenfile
# If we don't find it, then exit

try:
    token = os.environ["BOT_BUCKET_TOKEN"]
except:
    print("Your environment is not setup properly and the 'BOT_BUCKET_TOKEN' environment variable is missing.")
    exit()

bot = commands.Bot(command_prefix=".") # set prefix
bot.remove_command("help") # to make our own

bot.current_status = None
bot.sleep_time = global_vars.BOT_SLEEP_TIME

global_vars.bot = bot

import shopping.shopping as shopping
import ping_craig

@bot.event
async def on_ready():

    bot.shopping_channel_id = global_vars.SHOPPING_CHANNEL_ID
    bot.CRAIG_PING_CHANNEL_ID = global_vars.CRAIG_PING_CHANNEL_ID
    bot.test_channel_id = global_vars.TEST_CHANNEL_ID

    bot.shopping_channel = bot.get_channel(bot.shopping_channel_id)
    bot.ping_channel = bot.get_channel(bot.CRAIG_PING_CHANNEL_ID)
    bot.test_channel = bot.get_channel(bot.test_channel_id)

    # We send ready messages to personal server and not real since it keeps restarting, which causes confusion and clutters up the channel
    ready_msg = f"""\
Shopping bot up!
Time: {dt.now(tz).strftime("%c")}
"""
    # Bot is fully up now
    print(ready_msg)
    await bot.test_channel.send(ready_msg)

    # if global_vars.SHOPPING_MODE:
    #     await shopping.initialize_shopping()

bot.run(token, bot=True)