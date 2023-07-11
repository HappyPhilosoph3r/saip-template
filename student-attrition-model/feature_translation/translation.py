from db import create_controls, get_controls, update_controls
from feature_translation.tools import get_dict_key_by_value
from pandas import DataFrame
import json
import logging
import os

logging.getLogger(__name__)


def get_dataset_schema() -> dict:
    """
    Returns the json file containing all information to understand the dataset as a dictionary representation.

    :return: dict
    """
    current_file = 'translation.py'
    root = os.path.realpath(current_file).split('student-attrition-model')[0]
    path = os.path.join(root, 'student-attrition-model', 'data', 'dataset_legend.json')
    assert os.path.exists(path)
    with open(path, 'rb') as f:
        schema_info = json.load(f)
    return schema_info


def create_translator(df: DataFrame, initialise: bool = False) -> list:
    """
    Takes a dataframe containing the original dataset and returns a translation template as a list or returns unknown.

    If initialisation is true then the translation and meta-translation lists are added to the control database, if
    initialisation is false then a single translation list is returned.

    :param df: DataFrame
    :param initialise: bool
    :return: unknown | list
    """
    translation = list()
    meta_translation = list()
    schema = get_dataset_schema()
    features = [list(schema["variables"].keys())[list(schema["variables"].values()).index(feature)] for feature in df]
    for f in features:
        # Features which require one-hot encoding
        if schema['variable_types'].get(f) == 'one_hot_encoded':
            # if schema.get(f) and schema['drop_list'].get(f):
            key = 'parental_occupation_categories' if 'occupation' in f else f
            value_list = list(schema.get(key).values())
            value_list.remove(schema['drop_list'].get(f))
            translation.append(value_list)
            meta_translation.append([f] * len(value_list))
        elif f != "target":
            translation.append([f])
            meta_translation.append([f])

    if initialise:
        attributes = {
            "feature_translation": [item for sublist in translation for item in sublist],
            "meta_translation": [item for sublist in meta_translation for item in sublist]
        }
        assert len(attributes["feature_translation"]) == len(attributes["meta_translation"])
        try:
            assert create_controls(attributes) is True
        except Exception as e:
            logging.error("could not create controls... attempting to update instead", e)
            try:
                assert update_controls(attributes) is True
            except Exception as e:
                logging.error("could not create or update controls", e)
                raise Exception(e)
        return

    return [item for sublist in translation for item in sublist]


def features_hr(features: list) -> dict:
    """
    Takes a numeric list of features and returns a dictionary with feature_label: feature_value as key pairs.

    Assumes that input (features) is valid and in correct order for translation to dictionary.

    :param features: list
    :return: dict of feature label-value pairs
    """
    feature_dict = dict()
    schema = get_dataset_schema()
    controls = get_controls()
    translation, meta_translation = controls.feature_translation, controls.meta_translation
    for index, value in enumerate(features):
        category = meta_translation[index]
        if schema["variable_types"].get(category) == 'numeric':
            feature_dict[category] = value
            continue
        if schema["variable_types"].get(category) == 'binary':
            feature_dict[category] = "Yes" if value == 1 else "No"
            continue
        if schema["variable_types"].get(category) == 'boolean':
            feature_dict[category] = schema[category].get(str(value))
            continue
        if schema["variable_types"].get(category) == 'ordinal' and 'qualification' in category:
            meta_category = f'parental_{category.split("_")[1]}'
            key = get_dict_key_by_value(schema[f"{meta_category}_labels"], value)
            feature_dict[category] = schema[f"{meta_category}_categories"][key]
            continue
        if schema["variable_types"].get(category) == 'one_hot_encoded':
            # One hot encoded attributes have multiple entries, but only need to be calculated once.
            if feature_dict.get(category):
                continue
            # Find the indexes of all occurrences of the category in the translation array.
            indexes = [i for i, v in enumerate(meta_translation) if v == category]
            decoded = [translation[i] for i in indexes if features[i] != 0]
            feature_dict[category] = decoded[0] if len(decoded) == 1 else schema['drop_list'][category]
            continue
    assert len(set(meta_translation)) == len(feature_dict.keys())
    return feature_dict


def features_n(features: dict) -> list:
    """
    Takes a dictionary with feature label-value as key pairs. Returns a list of numeric representations of features.

    Assumes that input (features) is valid and in correct order for translation to dictionary.

    :param features: dict
    :return: list of numeric representations of features
    """
    feature_array = list()
    schema = get_dataset_schema()
    controls = get_controls()
    translation, meta_translation = controls.feature_translation, controls.meta_translation
    for index, value in enumerate(translation):
        category = meta_translation[index]
        if schema["variable_types"].get(category) == "numeric":
            feature_array.append(features.get(category))
            continue
        if schema["variable_types"].get(category) == 'binary':
            encode = 1 if features.get(category) is True or features.get(category) == "Yes" else 0
            feature_array.append(encode)
            continue
        if schema["variable_types"].get(category) == 'boolean':
            encode = int(get_dict_key_by_value(schema[category], features.get(category)))
            feature_array.append(encode)
            continue
        if schema["variable_types"].get(category) == 'ordinal' and 'qualification' in category:
            key = get_dict_key_by_value(schema["parental_qualification_categories"], features.get(category))
            encode = schema["parental_qualification_labels"].get(key)
            feature_array.append(encode)
            continue
        if schema["variable_types"].get(category) == 'one_hot_encoded':
            encode = 1 if value == features.get(category) else 0
            feature_array.append(encode)
            continue
    return feature_array


def features_update(features: list | dict, attribute: str,  value: str | int | float | bool, result_type: str = "list") -> list | dict:
    """
    Takes a list or dictionary representation of the features, updates and returns it in the desired format.

    Assumes that all inputs are valid values. Only one feature is altered, all other features remain the same.

    :param features: list | dict
    :param attribute: str
    :param value: str | int | float | bool
    :param result_type: str
    :return: list | dict representation of features
    """
    feature_dict = features_hr(features) if isinstance(features, list) else features
    feature_dict[attribute] = value
    if result_type == 'dict':
        return feature_dict
    return features_n(feature_dict)

