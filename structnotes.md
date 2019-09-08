We use namedtuples to hold the differences  
For each change made, we have a *list* of *namedtuples*

Each *namedtuple* has the name of the item changed, and another *list* of namedtuples of its properties

The namedtuple for the properties contain: 

- what info is being changed ("QTY NEEDED)  
- old value  
- new value

The same format is used for added items as well; we just use `None` for the old value.  
We don't pass any properties for removed items; just the name

Let's walk through it

Note: `properties()` and `changes()` are namedtuples declared previously. You can view them in `differ.py`

1. We delcare the namedtuples
```py
>>> properties = namedtuple('properties', 'name old new', defaults=(None,)*3)
>>> changes = namedtuple('changes', 'name property')
```

2. We make a property

```py
>>> new_property = properties("QTY NEEDED", "5", "10")
```
we can view it:

```py
>>> new_property
properties(name='QTY NEEDED', old='5', new='10')
```

3. We add it to a list
```py 
new_change_properties = []
new_change_properties.append(new_property)
```
we can view it:
```py
>>> new_change_properties
[properties(name='QTY NEEDED', old='5', new='10')]
```

4. We make another property and it to the list

```py
>>> new_property = properties ("PRICE PER UNIT", "$10", "$5")
>>> new_change_properties.append(new_property)
```

Now, the list has two properties:

```py
>>> new_property
properties(name='PRICE PER UNIT', old='$10', new='$5')
>>> new_change_properties
[properties(name='QTY NEEDED', old='5', new='10'), properties(name='PRICE PER UNIT', old='$10', new='$5')]
```

5. Then, we make a change, which has the name of the item changed, and the list of properties

```py
>>> new_change = changes("motor controller", new_change_properties)
```
We can see it:
```py
>>> new_change
changes(name='motor controller', property=[properties(name='QTY NEEDED', old='5', new='10'), properties(name='PRICE PER UNIT', old='$10', new='$5')])
```
6. Then, we append the change to a list of changes
```py
>>> changes_list = []
>>> changes_list.append(new_change)
```
and we can view it
```py
>>> changes_list
[changes(name='motor controller', property=[properties(name='QTY NEEDED', old='5', new='10'), properties(name='PRICE PER UNIT', old='$10', new='$5')])]
```

7. Lets make another change, with the same properties

```py
>>> new_change = changes("motors", new_change_properties)
>>> changes_list.append(new_change)
```
and we view it:
```py
>>> new_change
changes(name='motors', property=[properties(name='QTY NEEDED', old='5', new='10'), properties(name='PRICE PER UNIT', old='$10', new='$5')])
>>> changes_list
[changes(name='motor controller', property=[properties(name='QTY NEEDED', old='5', new='10'), properties(name='PRICE PER UNIT', old='$10', new='$5')]), changes(name='motors', property=[properties(name='QTY NEEDED', old='5', new='10'), properties(name='PRICE PER UNIT', old='$10', new='$5')])]
```

8. To refer to the items in the list:
```py
>>> one_change = changes_list[0]
>>> one_change
changes(name='motor controller', property=[properties(name='QTY NEEDED', old='5', new='10'), properties(name='PRICE PER UNIT', old='$10', new='$5')])

>>> one_change.name
'motor controller'

>>> one_change.property
[properties(name='QTY NEEDED', old='5', new='10'), properties(name='PRICE PER UNIT', old='$10', new='$5')]

>>> one_change.property[0]
properties(name='QTY NEEDED', old='5', new='10')

>>> one_change.property[0].name
'QTY NEEDED'
```

9. Of course, most of this would be done with a loop in reality:
```py
>>> for p in one_change.property:
...     print(p)
...
properties(name='QTY NEEDED', old='5', new='10')
properties(name='PRICE PER UNIT', old='$10', new='$5')

>>> for p in one_change.property:
...     print(p.name)
...     print(p.old)
...     print(p.new)
...
QTY NEEDED
5
10
PRICE PER UNIT
$10
$5

# And we can format these values in another string to make it look good:

>>> for p in one_change.property:
...     print(f'Item name: {p.name}')
...     print(f'Old value: {p.old}')
...     print(f'New value: {p.new}')
...
Item name: QTY NEEDED
Old value: 5
New value: 10
Item name: PRICE PER UNIT
Old value: $10
New value: $5

```

Hopefully that explains how namedtuples are used in this bot, and what they do!