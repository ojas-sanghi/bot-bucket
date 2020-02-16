import pygsheets
from shopping.differ import differ, itemdiffer, pricediffer
from asyncio import sleep

import global_vars

def get_init_data(bot):
    # Connects to Google Sheets and gets inital data

    bot.current_status = "Connecting to Google Sheets"
    pyclient = pygsheets.authorize()
    if global_vars.USE_TEST_SHEET:
        sh = pyclient.open_by_key(global_vars.TEST_SHEET_ID)
    else:
        sh = pyclient.open_by_key(global_vars.SHOPPING_SHEET_ID)
    
    bot.wks = sh.sheet1
    
    bot.current_status = "Getting initial data"
    bot.old_data = bot.wks.get_all_records(empty_value='-', head=2)
    
    bot.old_total_to_be_ordered = bot.wks.get_value(global_vars.TOTAL_TO_BE_ORDERED_CELL)
    bot.old_total_spent = bot.wks.get_value(global_vars.TOTAL_SPENT_CELL)

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

    if bot.old_total_to_be_ordered != bot.new_total_to_be_ordered:
        bot.item_diff = itemdiffer(bot.old_total_to_be_ordered, bot.new_total_to_be_ordered)
        bot.old_total_to_be_ordered = bot.new_total_to_be_ordered
    else:
        bot.item_diff = None
    
    if bot.old_total_spent != bot.new_total_spent:
        bot.price_diff = pricediffer(bot.old_total_spent, bot.new_total_spent)
        bot.old_total_spent = bot.new_total_spent
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

        bot.new_total_to_be_ordered = bot.wks.get_value(global_vars.TOTAL_TO_BE_ORDERED_CELL)
        bot.new_total_spent = bot.wks.get_value(global_vars.TOTAL_SPENT_CELL)

        print(bot.old_total_to_be_ordered)
        print(bot.new_total_to_be_ordered)

        if bot.new_data != bot.old_data:
            get_difference(bot)
            info_updated = True
            bot.old_data = bot.new_data
        
        if bot.new_total_to_be_ordered != bot.old_total_to_be_ordered:
            get_difference(bot)
            info_updated = True
            bot.old_total_to_be_ordered = bot.new_total_to_be_ordered
        
        if bot.new_total_spent != bot.old_total_spent:
            get_difference(bot)
            info_updated = True
            bot.old_total_spent = bot.new_total_spent

        if info_updated: # If something was changed/added/removed
            info_updated = False # reset this
            print('Something new')
            return [bot.change_diff, bot.added_diff, bot.removed_diff, bot.item_diff, bot.price_diff]
        else:
            print("Nothing new")
            bot.current_status = "Sleeping"
            await sleep(bot.sleep_time)