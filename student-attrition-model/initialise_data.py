import os
from db import create_all_indexes, generate_new_student, student_count
from db import create_training_test_datasets
from system_tools import prints
from feature_translation import create_translator
import pandas
import json
import logging

logging.getLogger(__name__)


def dataset_path() -> str:
    """
    Returns the path of the dataset.

    :return: str
    """
    current_file = 'initialise_data.py'
    current_file_path = os.path.realpath(current_file)
    return os.path.join(current_file_path.split(current_file)[0], 'data', 'dataset.csv')


def get_dataset_schema() -> dict:
    """
    Returns the schema json as a python dictionary.

    :return: dict
    """
    current_file = 'initialise_data.py'
    current_file_path = os.path.realpath(current_file)
    path = os.path.join(current_file_path.split(current_file)[0], 'data', 'dataset_legend.json')
    with open(path, 'rb') as f:
        schema_info = json.load(f)
    return schema_info


def check_data_exists(path: str):
    """
    Check that the dataset csv has been downloaded and actually exist.

    :return: bool
    """
    path_exists = os.path.exists(path)
    if not path_exists:
        raise FileNotFoundError('dataset.csv does not exist, please download the dataset and add to your codebase.')

    return True


def initialise_database():
    """
    Creates the database for system and also generates a training / test split in the dataset.

    :return: None
    """
    logging.info('initialising database')
    if not check_data_exists(dataset_path()):
        return

    # create database and add indexes
    create_all_indexes()

    if student_count() > 0:
        logging.info('Database already exists. If you want to rerun initialisation, please delete the database first!')
        return

    # Add documents to database
    data = pandas.read_csv(dataset_path())
    schema = get_dataset_schema()
    dataset = data.to_dict('records')

    create_translator(data, schema)

    for index, student in enumerate(dataset):
        generate_new_student(student, schema, True)
        prints(f'Added new student to database: {index + 1} out of {len(dataset)} completed '
               f'|| {round(100 / len(dataset) * (index + 1), 2)}% ')

    logging.info('Database initialised')

    create_training_test_datasets()
