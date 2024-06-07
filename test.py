#!/usr/bin/env python3

# Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

def create_dictionary(keys, values):
    # Place code here - refer to function specifics in section below
    i = 0
    new_dict = {}
    for item in keys[i]:
        new_dict[keys[i]] = str(values[i])
        i += 1
    return new_dict

if __name__ == '__main__':
    york = create_dictionary(list_keys, list_values)
    print('York: ', york)