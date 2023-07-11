import logging

logging.getLogger(__name__)


def one_hot_encoding(data_name: str, dropout_name: str, dictionary: dict) -> list[int] | None:
    """
    Takes the value given for a specified feature and converts it into a numerical one-hot encoded representation.

    :param data_name: str
    :param dropout_name: str
    :param dictionary: dict
    :return: list[int] | None
    """
    data_value = get_dict_value_index(dictionary, data_name)
    dropout_value = get_dict_value_index(dictionary, dropout_name)
    total_count = len(dictionary.keys())
    encoded = [0 for _ in range(total_count - 1)]
    # If the value is the dropout value then return a zero array of length categories - 1.
    if data_name == dropout_name:
        return encoded
    # If the value is < dropout value then return a zero array, except the desired category being == 1.
    if data_value < dropout_value:
        encoded[data_value] = 1
        return encoded
    # If the value is > the dropout value then return a zero array, except the desired category being == 1
    # Take into account the dropped value so need a - 1.
    if data_value > dropout_value:
        encoded[data_value - 1] = 1
        return encoded
    return None


def get_dict_value_index(dictionary: dict, value: str) -> int:
    """
    Returns the raw index of the position of a given value in a given dictionary.

    :param dictionary: dict
    :param value: str
    :return: int
    """
    return list(dictionary.values()).index(value)


def get_dict_key_by_value(dictionary: dict, value) -> str:
    """
    Returns the key value at the index of the position of a given value in a given dictionary.

    :param dictionary: dict
    :param value: str
    :return: str
    """
    return list(dictionary.keys())[list(dictionary.values()).index(value)]


def get_dict_key_from_array(dictionary: dict, value: str) -> str | None:
    """
        Returns the key at the index of the position of an array given the array contains the specified value.

        :param dictionary: dict
        :param value: str
        :return: str | None
        """
    try:
        return [k for k, v in dictionary.items() if value in v][0]
    except Exception as e:
        logging.error(f"Error occurred obtaining dict key from array: {e}")
        return None
