#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    largest = my_list[0]
    for num in my_list[1:]:
        if num > largest:
            largest = num

    return largest
