#!/usr/bin/env python3
'''Description: Learning Dictionaries'''

dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
print(dict_york.values()) # Values in the dictionary {key: value}
print(dict_york.keys()) # Keys in the dictionary {key: value}

print('')
print('---------------------------------------------------')
print('')

# Prints the value of the specified key
print(dict_york['Address'])
print(dict_york['Postal Code'])

print('')
print('---------------------------------------------------')
print('')

dict_york['Country'] = 'Canada' # Adds a new key and value to the dictionary
print(dict_york)
print(dict_york.values())
print(dict_york.keys())

print('')
print('---------------------------------------------------')
print('')

dict_york['Province'] = 'BC' # Changes the value of the specified key
print(dict_york)
print(dict_york.values())
print(dict_york.keys())

print('')
print('---------------------------------------------------')
print('')

dict_york['Province'] = 'ON'
print(dict_york)
print(dict_york.values())
print(dict_york.keys())

print('')
print('---------------------------------------------------')
print('')

list_of_keys = list(dict_york.keys())
print(list_of_keys[0])

list_of_keys = list(dict_york.keys())
for key in list_of_keys:
    print(key)
for value in dict_york.values():
    print(value)