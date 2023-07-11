
def get_dict_key_by_value(dictionary: dict, value: str | int | float | bool) -> str:
    """
    Takes a dictionary and dictionary value, Finds the key associated with the value and returns the key

    :param dictionary: dict
    :param value: str | int | float | bool
    :return: str
    """
    return list(dictionary.keys())[list(dictionary.values()).index(value)]
