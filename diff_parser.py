not_filled = ('$1.00', '1', '$1','1.00')    

def change_parser(all_changes):
    change_msg = ''
    if not all_changes: # If there are no changes
        return None

    change_msg += '\n**Changed Info**:\n'
    for each_change in all_changes:
        change_msg += f'\n*Item changed:* `{each_change.name}`\n'

        for each_property in each_change.property:
            old_value = each_property.old
            new_value = each_property.new

            # Replace $1 or $0 with 'Yes' or 'No' appropriately
            if each_property.name == 'ORDER FILLED?':
                if old_value in not_filled:
                    old_value = 'No'
                else:
                    old_value = 'Yes'
                if new_value in not_filled:
                    new_value = 'No'
                else:
                    new_value = 'Yes'

            change_msg += f"*Info changed:* {each_property.name}\n"
            change_msg += f"\t*Old value:* {old_value}\n"
            change_msg += f"\t*New value:* {new_value}\n"
    
    return change_msg

def add_parser(all_additions):
    add_msg = ''
    if not all_additions: # If there are no additions
        return None
    
    add_msg += '\n**Added Info**:\n'
    for each_addition in all_additions:
        add_msg += f'\nName: `{each_addition.name}`\n'
        
        for each_property in each_addition.property:
            new_value = each_property.new
            field_name = each_property.name
            
            # Replace $1 or $0 with 'Yes' or 'No' appropriately
            if field_name == 'ORDER FILLED?':
                if new_value in not_filled:
                    new_value = 'No'
                else:
                    new_value = 'Yes'
            # get rid of new line in this
            if field_name == '''SUBSYSTEM/
PROJECT''':
                field_name = 'SUBSYSTEM/PROJECT'
            # Add this here to prevent it from being spaced away
            add_msg += f'{field_name}: **{new_value}**\n'
            # We don't use old_value since it'll be none; no old_value in an addition
    
    return add_msg

def remove_parser(all_removals):
    remove_msg = ''
    if not all_removals: # If there are no removals
        return None
    
    remove_msg += '\n**Removed Info**:\n'
    for each_removal in all_removals:
        remove_msg += f'- `{each_removal.name}`\n'
    # We ignore the properties since all we want/need is the name of the item removed
    
    return remove_msg

def item_parser(all_items):
    item_msg = ''
    if not all_items: # If there is no change in number of items to be ordered
        return None
    
    item_msg += '\n**Items to be ordered**:\n'
    for each_item in all_items:
        for each_property in each_item.property:
            item_msg += f'Old value: {each_property.old}\n'
            item_msg += f'New value: {each_property.new}\n'
    
    return item_msg

def price_parser(all_prices):
    price_msg = ''
    if not all_prices:
        return None
    
    price_msg += '\n**Grand Total**:\n'
    for each_item in all_prices:
        for each_property in each_item.property:
            price_msg += f'Old value: {each_property.old}\n'
            price_msg += f'New value: {each_property.new}\n'
    
    return price_msg


def do_everything(diff_result):

    changes_list = diff_result[0]
    added_list = diff_result[1]
    removed_list = diff_result[2]
    items_list = diff_result[3]
    prices_list = diff_result[4]

    change_msg = change_parser(changes_list)
    add_msg = add_parser(added_list)
    remove_msg = remove_parser(removed_list)
    item_msg = item_parser(items_list)
    price_msg = price_parser(prices_list)

    return [change_msg, add_msg, remove_msg, item_msg, price_msg]
