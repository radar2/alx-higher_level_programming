#!/usr/bin/python3
def uniq_add(my_list=[]):
    list = []
    result = 0
    for item in my_list:
        if item not in list:
            list.append(item)
    for item in list:
        result = result + item
    return result
