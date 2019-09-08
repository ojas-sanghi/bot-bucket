import copy
from collections import namedtuple

# namedtuples used to store differences
properties = namedtuple('properties', 'name old new', defaults=(None,)*3)
adds = namedtuple('adds', 'name property')
changes = namedtuple('changes', 'name property')
removals = namedtuple('removals', 'name')

items = namedtuple('items', 'name property')
prices = namedtuple('prices', 'name property')

adds_list = []
changes_list = []
removals_list = []

def compareItems(oldItem, newItem, key):
    global changes, changes_list

    # Get the keys present in old item and new item so we can easily find
    # keys which have been added/removed
    oldSet = set(oldItem)
    newSet = set(newItem)

    changed = oldSet & newSet

    new_change_properties = []

    # Column -> Price, Amount Needed etc
    # oldItem[column] and newItem[column] -> Old and New value

    # Key -> Name of item (Motorcontroller, etc)

    # Keys are present in both
    if changed and changed != '':
        for column in changed: # for each property
            if oldItem[column] != newItem[column]: # if they're different
                # Make property and add it to list
                new_property = properties(column, oldItem[column], newItem[column])
                new_change_properties.append(new_property)
        # Make a new change, with the name of the item and the list of properties(changed values)
        new_change = changes(key, new_change_properties)
        # Add change to list of changes
        changes_list.append(new_change)
    else:
        changes_list = None

# Converts an array of dictionaries, to an array of dictionaries, indexed by
# the item name
def itemsArrayToDict(items):
    mapping = {}

    for item in items:
        mapping = itemDetailsToDict(item, mapping)

    return mapping

# Converts a dictionary to a dictionary indexed on item name
def itemDetailsToDict(item, mapping={}):
    # Get the item name
    key = item['LIST ITEM']

    # Delete the item name from the dict
    del item['LIST ITEM']

    # Store in a mapping on item name   
    mapping[key] = item

    return mapping

def differ(oldItems, newItems):
    global adds_list, changes_list, removals_list

    # Returns dict of namedtuples of:
    # added items
    # changed items
    # removed items

    changes_list = []
    adds_list = []
    removals_list = []

    # Make sure we don't manipulate the calling data
    oldItemsCopy = copy.deepcopy(oldItems)
    newItemsCopy = copy.deepcopy(newItems)

    oldItemsMapping = itemsArrayToDict(oldItemsCopy)
    newItemsMapping = itemsArrayToDict(newItemsCopy)

    # Get just the items so we can see which items were removed/added
    oldItemsKeys = set(oldItemsMapping.keys())
    newItemsKeys = set(newItemsMapping.keys())

    addedItems = newItemsKeys - oldItemsKeys
    removedItems = oldItemsKeys - newItemsKeys
    possiblyChangedItems = newItemsKeys & oldItemsKeys

    if addedItems and str(addedItems) != 'set()':
        if next(iter(addedItems)) != '':
            # addition = Name of item (Motorcontroller, etc)
            # col_value = Price, Amount Needed etc
            # cell_value = $100, 5, etc
            for addition in addedItems:
                new_addition_properties = []
                for col_value in newItemsMapping[addition]:
                    cell_value = newItemsMapping[addition][col_value]
                    # Make property and add it to list
                    new_property = properties(col_value, None, cell_value)
                    new_addition_properties.append(new_property)
                # Make a new addition, with the name of the item and the list of properties (info on added items)
                new_addition = adds(addition, new_addition_properties)
                # Add addition to list of additions
                adds_list.append(new_addition)
    else:
        adds_list = None

    if removedItems and str(removedItems) != 'set()':
        if next(iter(removedItems)) != '':
            # removal = Name of item removed (Motorcontroller, etc)
            for removal in removedItems:
                    # Make a new removal with just the name
                    new_removal = removals(removal)
                    # Add each to a list
                    removals_list.append(new_removal)
    else:
        removals_list = None
    
    for key in possiblyChangedItems:
        if oldItemsMapping[key] != newItemsMapping[key]:
            compareItems(oldItemsMapping[key], newItemsMapping[key], key)
    
    if changes_list == []:
        changes_list = None

    return {'changed': changes_list, 'added': adds_list, 'removed': removals_list}

def itemdiffer(old_items, new_items):

    #  Returns list of a namedtuple of the change in the number (amount) of items to be ordered

    items_list = []

    # Make a new property and pass none for name
    new_item_properties = [properties(None, old_items, new_items)]
    # Make new item change and pass none for name
    new_item_change = items(None, new_item_properties)

    # Append to list
    items_list.append(new_item_change)
    
    return items_list

def pricediffer(old_price, new_price):

    # Returns list of a namedtuple of change in the price (total cost) of items to be ordered

    prices_list = []

    # Make a new property and pass none for name
    new_price_properties = [properties(None, old_price, new_price)]
    # Make new item change and pass none for name
    new_price_change = prices(None, new_price_properties)

    # Append to list
    prices_list.append(new_price_change)

    return prices_list