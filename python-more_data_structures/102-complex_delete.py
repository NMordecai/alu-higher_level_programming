#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """
    Deletes keys with a specific value from a dictionary.

    Args:
        a_dictionary: The dictionary to modify.
        value: The value to search for and delete keys associated with it.

    Returns:
        The modified dictionary.
    """
    keys_to_delete = []  # Store keys to delete to avoid modifying during iteration

    for key, val in a_dictionary.items():
        if val == value:
            keys_to_delete.append(key)

    for key in keys_to_delete:
        del a_dictionary[key]

    return a_dictionary
