#data_grabber.py
"""
old_data = [{'LIST ITEM': 'one more thing yeet', 'QTY NEEDED': 10, 'PRICE PER UNIT': '$5', 'TOTAL PRICE': '$50', 'DATE ADDED': '5/26/1948', 'ORDER FILLED?': '$0.00', 'ACTUAL ORDERED': 10, 'DATE FILLED': '-', 'LINK': 'thing.com', 'NOTES': 'really good'}, {'LIST ITEM': 'another thing', 'QTY NEEDED': 20, 'PRICE PER UNIT': '$101', 'TOTAL PRICE': '$35', 'DATE ADDED': '3/9/58', 'ORDER FILLED?': '$1.00', 'ACTUAL ORDERED': 200, 'DATE FILLED': '-', 'LINK': 'example.org', 'NOTES': 'not needed i dont think so anyways '}, {'LIST ITEM': 'this item has to be removed', 'QTY NEEDED': 15, 'PRICE PER UNIT': '$20', 'TOTAL PRICE': '$1,000', 'DATE ADDED': '5/7/85', 'ORDER FILLED?': '$0.00', 'ACTUAL ORDERED': 5, 'DATE FILLED': '-', 'LINK': 'google.com', 'NOTES': 'nice'}, {'LIST ITEM': 'Motor Controllerjan 5', 'QTY NEEDED': 20, 'PRICE PER UNIT': '$240', 'TOTAL PRICE': '$300', 'DATE ADDED': '12/29/2018', 'ORDER FILLED?': '$0.00', 'ACTUAL ORDERED': 20, 'DATE FILLED': '12/31/2018', 'LINK': 'get rekt boi', 'NOTES': 'non'}]

new_data = [{'LIST ITEM': 'one more thing yeet', 'QTY NEEDED': 15, 'PRICE PER UNIT': '$50', 'TOTAL PRICE': '$450', 'DATE ADDED': '5/26/1948', 'ORDER FILLED?': '$1.00', 'ACTUAL ORDERED': 50, 'DATE FILLED': '-', 'LINK': 'thing.com', 'NOTES': 'really good'}, {'LIST ITEM': 'another thing', 'QTY NEEDED': 20, 'PRICE PER UNIT': '$115', 'TOTAL PRICE': '$513', 'DATE ADDED': '3/9/58', 'ORDER FILLED?': '$1.00', 'ACTUAL ORDERED': 200, 'DATE FILLED': '-', 'LINK': 'example.org', 'NOTES': 'extremely critical'}, {'LIST ITEM': 'is it a plane? a bird?', 'QTY NEEDED': 1, 'PRICE PER UNIT': '$10,000', 'TOTAL PRICE': '$10,000', 'DATE ADDED': '5/27/2019', 'ORDER FILLED?': '$1.00', 'ACTUAL ORDERED': '12/30/1899', 'DATE FILLED': '-', 'LINK': 'non-existent', 'NOTES': 'op'}, {'LIST ITEM': 'one more thing to be added', 'QTY NEEDED': 1, 'PRICE PER UNIT': '$500', 'TOTAL PRICE': '$200', 'DATE ADDED': '5/27/2019', 'ORDER FILLED?': '$1.00', 'ACTUAL ORDERED': '12/30/1899', 'DATE FILLED': '-', 'LINK': 'duckduck.com', 'NOTES': 'meh'}]
"""


# differ.py
"""
old_Items =[{'LIST ITEM': 'one more thing yeet', 'QTY NEEDED': 10, 'PRICE PER UNIT': '$5', 'TOTAL PRICE': '$50', 'DATE ADDED': '5/26/1948', 'ORDER FILLED?': '$0.00', 'ACTUAL ORDERED': 10, 'DATE FILLED': '-', 'LINK': 'thing.com', 'NOTES': 'really good'}, {'LIST ITEM': 'another thing', 'QTY NEEDED': 20, 'PRICE PER UNIT': '$101', 'TOTAL PRICE': '$35', 'DATE ADDED': '3/9/58', 'ORDER FILLED?': '$1.00', 'ACTUAL ORDERED': 200, 'DATE FILLED': '-', 'LINK': 'example.org', 'NOTES': 'not needed i dont think so anyways '}, {'LIST ITEM': 'this item has to be removed', 'QTY NEEDED': 15, 'PRICE PER UNIT': '$20', 'TOTAL PRICE': '$1,000', 'DATE ADDED': '5/7/85', 'ORDER FILLED?': '$0.00', 'ACTUAL ORDERED': 5, 'DATE FILLED': '-', 'LINK': 'google.com', 'NOTES': 'nice'}, {'LIST ITEM': 'Motor Controllerjan 5', 'QTY NEEDED': 20, 'PRICE PER UNIT': '$240', 'TOTAL PRICE': '$300', 'DATE ADDED': '12/29/2018', 'ORDER FILLED?': '$0.00', 'ACTUAL ORDERED': 20, 'DATE FILLED': '12/31/2018', 'LINK': 'get rekt boi', 'NOTES': 'non'}]

new_Items = [{'LIST ITEM': 'one more thing yeet', 'QTY NEEDED': 15, 'PRICE PER UNIT': '$50', 'TOTAL PRICE': '$450', 'DATE ADDED': '5/26/1948', 'ORDER FILLED?': '$1.00', 'ACTUAL ORDERED': 50, 'DATE FILLED': '-', 'LINK': 'thing.com', 'NOTES': 'really good'}, {'LIST ITEM': 'another thing', 'QTY NEEDED': 20, 'PRICE PER UNIT': '$115', 'TOTAL PRICE': '$513', 'DATE ADDED': '3/9/58', 'ORDER FILLED?': '$1.00', 'ACTUAL ORDERED': 200, 'DATE FILLED': '-', 'LINK': 'example.org', 'NOTES': 'extremely critical'}, {'LIST ITEM': 'is it a plane? a bird?', 'QTY NEEDED': 1, 'PRICE PER UNIT': '$10,000', 'TOTAL PRICE': '$10,000', 'DATE ADDED': '5/27/2019', 'ORDER FILLED?': '$1.00', 'ACTUAL ORDERED': '12/30/1899', 'DATE FILLED': '-', 'LINK': 'non-existent', 'NOTES': 'op'}, {'LIST ITEM': 'one more thing to be added', 'QTY NEEDED': 1, 'PRICE PER UNIT': '$500', 'TOTAL PRICE': '$200', 'DATE ADDED': '5/27/2019', 'ORDER FILLED?': '$1.00', 'ACTUAL ORDERED': '12/30/1899', 'DATE FILLED': '-', 'LINK': 'duckduck.com', 'NOTES': 'meh'}]

key = 'another item'

chl = differ(oldIs, newIs)
    chl = chl['added']

    for c in chl:

        print('\n')
        print(f'name: {c.name}')
    
        for eproperty in c.property:
            print(f"Property: {eproperty.name}")
            print(f"Old: {eproperty.old}")
            print(f"New: {eproperty.new}")
"""


# diff_parser.py
"""
from collections import namedtuple
properties = namedtuple('properties', 'name old new', defaults=(None,)*3)
changes = namedtuple('changes', 'name property')
adds = namedtuple('adds', 'name property')
removals = namedtuple('removals', 'name')
items = namedtuple('items', 'name property')
prices = namedtuple('prices', 'name property')


#(old)_diff_res = ({'changed': {'changes': [['Motor Controllerjan 5'],['PRICE PER UNIT'],[['$200', '$240']],['Motor Controllerjan 5'],['ORDER FILLED?'],[['$0.00', '$1.00']],['Motor Controllerjan 5'],['QTY NEEDED'],[[110, 120]]]},'added': {'adds': {'a new item hatbh be e aded': {'QTY NEEDED': '10','PRICE PER UNIT': '$2,130','TOTAL PRICE': '$213','DATE ADDED': '123','ORDER FILLED?': '$1.00','ACTUAL ORDERED': '13','DATE FILLED': '13','LINK': '123','NOTES': '12'},'this is a new item too ya yeet': {'QTY NEEDED': '$0','PRICE PER UNIT': '123123123','TOTAL PRICE': '132134','DATE ADDED': '3413527645324','ORDER FILLED?': '$0.00','ACTUAL ORDERED': '6587657237','DATE FILLED': '','LINK': ' ','NOTES': '685543256764'}}},'removed': {'removed': ['3 CIM Ball Shifter (2.65x Spread, 64:20 WCD extension)', 'this is a new item yeet']}}, None, None)

---
# diff_res for an isolated type of change which includes the full list
# pass to do_everything()
---

diff_res = [[changes(name='one more thing yeet', property=[properties(name='ORDER FILLED?', old='$0.00', new='$1.00'), properties(name='ACTUAL ORDERED', old=10, new=50), properties(name='QTY NEEDED', old=10, new=15), properties(name='PRICE PER UNIT', old='$5', new='$50'), properties(name='TOTAL PRICE', old='$50', new='$450')]), changes(name='another thing', property=[properties(name='NOTES', old='not needed i dont think so anyways ', new='extremely critical'), properties(name='PRICE PER UNIT', old='$101', new='$115'), properties(name='TOTAL PRICE', old='$35', new='$513')])], [adds(name='one more thing to be added', property=[properties(name='QTY NEEDED', old=None, new=1), properties(name='PRICE PER UNIT', old=None,new='$500'), properties(name='TOTAL PRICE', old=None, new='$200'), properties(name='DATE ADDED', old=None, new='5/27/2019'), properties(name='ORDER FILLED?', old=None, new='$1.00'), properties(name='ACTUAL ORDERED', old=None, new='12/30/1899'), properties(name='DATE FILLED', old=None, new='-'), properties(name='LINK', old=None, new='duckduck.com'), properties(name='NOTES', old=None, new='meh')]), adds(name='is it a plane? a bird?', property=[properties(name='QTY NEEDED',old=None, new=1), properties(name='PRICE PER UNIT', old=None, new='$500'), properties(name='TOTAL PRICE', old=None, new='$200'), properties(name='DATE ADDED', old=None, new='5/27/2019'), properties(name='ORDER FILLED?', old=None, new='$1.00'), properties(name='ACTUAL ORDERED', old=None, new='12/30/1899'), properties(name='DATE FILLED', old=None, new='-'), properties(name='LINK', old=None, new='duckduck.com'), properties(name='NOTES', old=None, new='meh')])], [removals(name='Motor Controllerjan 5', property=[properties(name=None, old=None, new=None)]), removals(name='this item has to be removed', property=[properties(name=None, old=None, new=None)])], None, None]

#TODO
# add and change full diff_res here

remove_diff_res = [None, None, [removals(name='est-ce qe bir'), removals(name='one more thing to be added')], None, None]

item_diff_res = [None, None, None, [items(name=None, property=[properties(name=None, old='6', new='4')])], None]

price_diff_res = [None, None, None, None, [prices(name=None, property=[properties(name=None, old='$200.00', new='$150.00')])]]

------------------------------------------------
# diff_res for only one thing
# pass directly to appropriate function

just_change_diff_res = [[changes(name='another thing', property=[properties(name='PRICE PER UNIT', old='$101', new='$115'), properties(name='NOTES', old='not needed i dont think so anyways ', new='extremely critical'), properties(name='TOTAL PRICE', old='$35', new='$513')]), changes(name='one more thing yeet', property=[properties(name='PRICE PER UNIT', old='$5', new='$50'), properties(name='ACTUAL ORDERED', old=10, new=50), properties(name='ORDER FILLED?', old='$0.00', new='$1.00'), properties(name='QTY NEEDED', old=10, new=15), properties(name='TOTAL PRICE', old='$50', new='$450')])], None, None, None, None]

---
# NOTE: THIS DATA (add_diff_res) is FAULTY. If we test again, do 2 test additions on a sheet and print the result, and REPLACE this one. An error in differ.py caused all properties of added items to be the same(fixed now)
----
just_add_diff_res = [adds(name='another added thing', property=[properties(name='QTY NEEDED', old=None, new=5), properties(name='PRICE PER UNIT', old=None, new='$10.00'), properties(name='TOTAL PRICE', old=None, new='$50.00'), properties(name='DATE ADDED', old=None, new='today'), properties(name='DATE NEEDED', old=None, new='-'), properties(name='ORDER FILLED?', old=None, new='$1.00'), properties(name='ACTUAL ORDERED', old=None, new='-'), properties(name='DATE FILLED', old=None, new='-'), properties(name='LINK/SOURCE', old=None, new='google.com'), properties(name='REQUESTER', old=None, new='ohas'), properties(name='SUBSYSTEM/\nPROJECT', old=None, new='sofware dud'), properties(name='NOTES', old=None, new='none')]), adds(name='1/2" hex x 30T gear', property=[properties(name='QTY NEEDED', old=None, new=5), properties(name='PRICE PER UNIT', old=None, new='$10.00'), properties(name='TOTAL PRICE', old=None, new='$50.00'), properties(name='DATE ADDED', old=None, new='today'), properties(name='DATE NEEDED', old=None, new='-'), properties(name='ORDER FILLED?', old=None, new='$1.00'), properties(name='ACTUAL ORDERED', old=None, new='-'), properties(name='DATE FILLED', old=None, new='-'), properties(name='LINK/SOURCE', old=None, new='google.com'), properties(name='REQUESTER', old=None, new='ohas'), properties(name='SUBSYSTEM/\nPROJECT', old=None, new='sofware dud'), properties(name='NOTES', old=None, new='none')])]

just_remove_diff_res = [removals(name='Motor Controllerjan 5', property=[properties(name=None, old=None, new=None)]), removals(name='this item has to be removed', property=[properties(name=None, old=None, new=None)])]

just_item_diff_res = [items(name=None, property=[properties(name=None, old=10, new=10)])]

just_price_diff_res = [prices(name=None, property=[properties(name=None, old='$150.00', new='$200.00')])]

---
#old_change_diff_res = {'changed': {'changes': [['Motor Controllerjan 5'], ['QTY NEEDED'], [[10, 20]]]}, 'added': None, 'removed': None}
"""

# TODO: get diff_res for only changes and adds, with None for the others also included