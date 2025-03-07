#!/usr/bin/python3
def remove_char_at(str, n):
    """
    Creates a copy of the string, removing the character at position n.

    Args:
        str: The input string.
        n: The index of the character to remove.

    Returns:
        A new string with the character at position n removed, or the original string if n is invalid.
    """
    if n < 0 or n >= len(str):
        return str

    result = ""
    i = 0
    while i < len(str):
        if i != n:
            result += str[i]
        i += 1
    return result
