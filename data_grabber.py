import pygsheets
from differ import differ, itemdiffer, pricediffer
from asyncio import sleep

def get_init_data(bot):
    # Connects to Google Sheets and gets inital data

    bot.current_status = "Connecting to Google Sheets"
    pyclient = pygsheets.authorize()
    sh = pyclient.open('SHOPPING LIST')
    
    bot.wks = sh.sheet1
    
    bot.current_status = "Getting initial data"
    bot.old_data = bot.wks.get_all_records(empty_value='-', head=2)
    bot.old_items = bot.wks.cell('G1').value
    bot.old_price = bot.wks.cell('E1').value

    print("Received Data\n")

def get_difference(bot):

    bot.current_status = "Checking data for anything new"

    if bot.old_data != bot.new_data:
        difference = differ(bot.old_data, bot.new_data)
    else:
        bot.change_diff = None
        bot.added_diff = None
        bot.removed_diff = None
        difference = None

    if bot.old_items != bot.new_items:
        bot.item_diff = itemdiffer(bot.old_items, bot.new_items)
        bot.old_items = bot.new_items
    else:
        bot.item_diff = None
    
    if bot.old_price != bot.new_price:
        bot.price_diff = pricediffer(bot.old_price, bot.new_price)
        bot.old_price = bot.new_price
    else:
        bot.price_diff = None

    if difference:
        # Get just the namedtuples
        bot.change_diff = difference['changed']
        bot.added_diff = difference['added']
        bot.removed_diff = difference['removed']

async def get_data(bot):
    while True:
        info_updated = False
        bot.current_status = "Getting new data"
        bot.new_data = bot.wks.get_all_records(empty_value='-', head=2)

        bot.new_items = bot.wks.cell('G1').value
        bot.new_price = bot.wks.cell('E1').value

        if bot.new_data != bot.old_data:
            get_difference(bot)
            info_updated = True
            bot.old_data = bot.new_data
        
        if bot.new_price != bot.old_price:
            get_difference(bot)
            info_updated = True
            bot.old_price = bot.new_price
        
        if bot.new_items != bot.old_items:
            get_difference(bot)
            info_updated = True
            bot.old_items = bot.new_items

        if info_updated: # If something was changed/added/removed
            info_updated = False # reset this
            print('Something new')
            return [bot.change_diff, bot.added_diff, bot.removed_diff, bot.item_diff, bot.price_diff]
        else:
            print("Nothing new")
            bot.current_status = "Sleeping"
            await sleep(bot.sleep_time)