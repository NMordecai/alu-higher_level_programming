#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    """
    Executes a function safely.

    Args:
        fct: The function to execute.
        *args: The arguments to pass to the function.

    Returns:
        The result of the function if successful, None otherwise.
    """
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
