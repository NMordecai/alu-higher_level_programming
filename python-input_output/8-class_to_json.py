#!/usr/bin/python3
def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization of an object.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: A dictionary representation of the object's attributes.
    """
    if not hasattr(obj, "__dict__"):
        return {}
    
    json_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value
    return json_dict
