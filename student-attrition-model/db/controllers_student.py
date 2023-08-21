from db.models_student import Student, student_info_projection
from db.services_pymongo import students
from db.tools import one_hot_encoding, get_dict_key_from_array, get_dict_key_by_value
import logging
import pandas as pd
from pandas import DataFrame
import json
import random
from pymongo import DESCENDING

logging.getLogger(__name__)


def generate_new_student(data: dict, schema: dict, initialise: bool = False):
    """
    Take a sample data instance in dict format and the relevant schema. Return an instance of class Student.

    This function is designed to take a data instance and convert it into a format that is standardised for the
    dataset and compatible with MongoDB. If initialise is true, it then saves the document to the database. The system
    returns the new document.

    :param data: dict - dataset
    :param schema: dict - legend provides metadata information for dataset
    :param initialise: bool - determines whether student is saved to the database
    :return: Student
    """
    sample = dict()
    features = list()
    for k, v in data.items():
        try:
            key = list(filter(lambda x: x[1] == k, schema['variables'].items()))[0][0]
        except IndexError:
            continue
        # Binary categories
        f = list()
        if schema['variable_types'].get(key) == 'binary':
            sample[key] = schema['binary_variables'][str(v)] == 'yes'
            f = [v]
        if schema['variable_types'].get(key) == 'numeric':
            sample[key] = v
            f = [v]
        if schema["variable_types"].get(key) == 'boolean':
            sample[key] = schema[key].get(str(v))
            f = [v]
        if schema["variable_types"].get(key) == 'ordinal':
            meta_key = f"parental_{key.split('_')[1]}" if 'mother' in key or 'father' in key else key
            # Assumes mothers_qualification and fathers_qualification are the only ordinal variables
            original = schema[meta_key].get(str(v))
            encoded = get_dict_key_from_array(schema[f"{meta_key}_categories_readable"], original)
            category_key = str(get_dict_key_by_value(schema[f"{meta_key}_categories"], encoded))
            sample[key] = encoded
            f = [schema[f"{meta_key}_labels"].get(category_key)]
        if schema["variable_types"].get(key) == 'one_hot_encoded':
            if 'mother' in key or 'father' in key:
                meta_key = f"parental_{key.split('_')[1]}"
                category_key = schema[meta_key].get(str(v))
                encoded = get_dict_key_from_array(schema[f"{meta_key}_categories_readable"], category_key)
                sample[key] = encoded
                f = one_hot_encoding(encoded, schema["drop_list"].get(key), schema[f"{meta_key}_categories"])
            else:
                sample[key] = schema[key].get(str(v))
                f = one_hot_encoding(schema[key][str(v)], schema["drop_list"].get(key), schema[key])
        if schema["variable_types"].get(key) == 'string':
            sample[key] = v

        assert None not in f
        features.append(f)

    # Flatten list to create feature vector
    features = [item for sublist in features for item in sublist]
    sample['features'] = features

    # create student and save to database
    student = Student(sample)

    if initialise:
        student.create_document()

    return student


def student_count() -> int:
    """
    Returns the number of student documents in the database.

    :return: int
    """
    return students.count_documents({})


def student_overview() -> dict:
    """
    Returns overview information for the student collection in the database.

    :return: dict
    """
    overview = {
        'graduate_count': students.count_documents({'target': 'Graduate', 'training_data': True}),
        'dropout_count': students.count_documents({'target': 'Dropout', 'training_data': True}),
        'enrolled_count': students.count_documents({'target': 'Enrolled', 'training_data': True}),
        'total_count': students.count_documents({'training_data': True}),
    }

    return overview


def student_priors(variable, variable_value, training=True) -> dict:
    """
    Returns overview information for the student collection in the database.

    :return: dict
    """

    total_students = students.count_documents({'training_data': True, variable: variable_value})

    overview = {
        'variable': variable,
        'graduate_count':  ((100 / total_students) * students.count_documents({'target': 'Graduate', 'training_data': training, variable: variable_value}) / 100),
        'dropout_count':  ((100 / total_students) * students.count_documents({'target': 'Dropout', 'training_data': training, variable: variable_value}) / 100),
        'enrolled_count': ((100 / total_students) * students.count_documents({'target': 'Enrolled', 'training_data': training, variable: variable_value}) / 100),
        'total_count': total_students
    }

    return overview


def pandas_category(categories: list, ordered: bool = False):
    """
    Takes a list of categories and ordered type returns a pandas category type for dataframe.

    :param categories: list
    :param ordered: bool
    :return: Pandas CategoricalDType
    """

    return pd.CategoricalDtype(categories=categories, ordered=ordered)


def get_students(info_only: bool = False, filters: dict | None = None) -> list[dict] | list[Student]:
    """
    Retrieves and returns a list of instances of the student class from the database.

    The info_only parameter determines whether the entire student class is returned or just the relevant variables
    contained in the info dictionary. The filters parameter determines whether the retrieved list is reduced by applying
    limitations, or whether all instances are returned.

    :param info_only: bool
    :param filters: dict | None
    :return: list[dict] | list[Student]
    """
    if filters is None:
        filters = dict()
    if info_only:
        return list(map(lambda x: Student(x).info(), students.find(filters)))
    return list(map(lambda x: Student(x), students.find(filters)))


def generate_student_dataframe(schema: dict) -> DataFrame:
    """
    Returns a dataframe for the student collection in the database.

    :param schema: dict
    :return: DataFrame
    """
    types_dict = {
        "_id": str,
        "marital_status": pandas_category(schema['marital_status'].values()),
        "application_mode": pandas_category(schema['application_mode'].values()),
        "application_order": int,
        "course": pandas_category(schema['course'].values()),
        "attendance_type": pandas_category(schema['attendance_type'].values()),
        "previous_qualification": pandas_category(schema['previous_qualification'].values()),
        "nationality": pandas_category(schema['nationality'].values()),
        "mothers_qualification": pandas_category(schema['parental_qualification_categories'].values(), ordered=True),
        "fathers_qualification": pandas_category(schema['parental_qualification_categories'].values(), ordered=True),
        "mothers_occupation": pandas_category(schema['parental_occupation_categories'].values()),
        "fathers_occupation": pandas_category(schema['parental_occupation_categories'].values()),
        "displaced": bool,
        "educational_special_needs": bool,
        "debtor": bool,
        "tuition_fees_up_to_date": bool,
        "gender": pandas_category(schema['gender'].values()),
        "scholarship_holder": bool,
        "age_at_enrolment": int,
        "international": bool,
        "curricular_units_1st_semester_credited": float,
        "curricular_units_1st_semester_enrolled": float,
        "curricular_units_1st_semester_evaluations": float,
        "curricular_units_1st_semester_approved": float,
        "curricular_units_1st_semester_grade": float,
        "curricular_units_1st_semester_without_evaluations": float,
        "curricular_units_2nd_semester_credited": float,
        "curricular_units_2nd_semester_enrolled": float,
        "curricular_units_2nd_semester_evaluations": float,
        "curricular_units_2nd_semester_approved": float,
        "curricular_units_2nd_semester_grade": float,
        "curricular_units_2nd_semester_without_evaluations": float,
        "unemployment_rate": float,
        "inflation_rate": float,
        "gdp": float,
        "target": pandas_category(['Dropout', 'Graduate', 'Enrolled'])
    }
    student_list = json.dumps(get_students(info_only=True))
    student_df = pd.read_json(student_list, dtype=types_dict)
    return student_df


def split_features_and_labels(dataset: list[Student]) -> tuple[list, list]:
    """
    Takes a set of students and separates out the respective feature lists and labels. Returns two lists.

    :param dataset: list[Student]
    :return: tuple[list, list]
    """

    features = list(map(lambda x: x.features, dataset))
    labels = list(map(lambda x: x.target, dataset))

    return features, labels


def training_dataset_resampled(validation_split: bool = False, validation_percentage: float = 20.0) -> tuple[list, list] | tuple[tuple[list, list], tuple[list, list]]:
    """
    Takes all training samples and creates a balanced dataset using bootstrapping and returns a dataframe.

    Due to the random nature of bootstrapping this method will produce a dataframe that contains different samples
    every time it is called, however the total number of entries and the total number of entries for each class will
    remain the same.

    :return: tuple[list, list] | tuple[tuple[list, list], tuple[list, list]]

    """
    all_students = get_students(filters={"training_data": True})
    classes = list(map(lambda x: x.target, all_students))
    mean = len(all_students) / len(set(classes))
    decimated_mean = mean / 10
    all_samples = list()
    for c in set(classes):
        try:
            assert len(list(filter(lambda x: x == c, classes))) > decimated_mean
        except AssertionError:
            raise AssertionError(f'Number of samples for class {c} is too small to resample meaningfully')

        for n in range(10):
            all_samples.append([Student(student) for student in list(students.aggregate([
                {"$match": {"training_data": True, "target": c}},
                {"$sample": {"size": decimated_mean}}
            ]))])

    # Flatten list
    all_samples = [item for sublist in all_samples for item in sublist]
    if not validation_split:
        return split_features_and_labels(all_samples)

    # Split training data into training and validation datasets
    validation_count = int(round((len(all_samples) / 100) * validation_percentage, 0))
    validation_indexes = random.sample([n for n in range(len(all_samples))], k=validation_count)
    training_data = list()
    validation_data = list()
    for index, sample in enumerate(all_samples):
        validation_data.append(sample) if index in validation_indexes else training_data.append(sample)
    return split_features_and_labels(training_data), split_features_and_labels(validation_data)


def training_dataset(validation_split: bool = False, validation_percentage: float = 20.0) -> tuple[list, list] | tuple[tuple[list, list], tuple[list, list]]:
    """
    Creates a training dataset from the database and returns the relevant data split by features and label.

    If validation is set to True it divides the training set into two with the division split equal to the validation
    percentage value and returns two sets of data split by features and labels.

    :param validation_split: bool
    :param validation_percentage: float
    :return:  tuple[list, list] | tuple[tuple[list, list], tuple[list, list]]
    """
    if not validation_split:
        training_students = get_students(filters={"training_data": True})
        return split_features_and_labels(training_students)

    # Split training data into training and validation datasets
    training_count = students.count_documents({"training_data": True})
    validation_count = (training_count / 100) * validation_percentage
    validation_data = [Student(student) for student in list(students.aggregate([
            {"$match": {"training_data": True}},
            {"$sample": {"size": validation_count}}
        ]))]
    validation_ids = list(map(lambda x: x._id, validation_data))
    training_data = get_students(filters={"training_data": True, "_id": {"$nin": validation_ids}})
    return split_features_and_labels(training_data), split_features_and_labels(validation_data)


def test_dataset() -> tuple[list, list]:
    """
    Creates a test dataset from the database and returns the relevant data split by features and label.

    :return:  tuple[list, list]
    """
    test_students = get_students(filters={"test_data": True})
    return split_features_and_labels(test_students)


def create_training_test_datasets(training_percentage: float = 80.0) -> bool:
    """
    Takes all students in the database and splits them into two datasets by updating the relevant attributes.

    Number of training samples is determined by training_percentage value. The training samples are selected using the
    pseudo-random method provided by MongoDB. Once the training samples have been identified and updated the remainder
    of the samples are classed as test samples and are updated accordingly.

    :param training_percentage: float
    :return: bool
    """

    # Create training dataset
    try:
        all_students = get_students()
        classes = set(map(lambda x: x.target, all_students))
        for i in classes:
            relevant_students = (list(map(lambda x: x._id, filter(lambda x: x.target == i, all_students))))
            training_count = int((len(relevant_students) / 100) * training_percentage)
            training_samples = [Student(student) for student in list(students.aggregate([
                {"$match": {"_id": {"$in": relevant_students}}},
                {"$sample": {"size": training_count}}
            ]))]
            for sample in training_samples:
                sample.set_training_status()
        logging.info('Training dataset created')
    except Exception as e:
        logging.error('Error: could not create training dataset', e)
        return False

    # Create test dataset
    try:
        remaining_students = list(map(lambda x: Student(x), students.find({"training_data": False})))
        for student in remaining_students:
            student.set_training_status(training=False)
        logging.info('Test dataset created')
    except Exception as e:
        logging.error('Error: could not create test dataset', e)
        return False

    return True


def student_min_max(category: str, training: bool = True) -> tuple[int | float, int | float]:
    """
    Returns the minimum and maximum value for a given category on the training or full dataset.

    :param category: str
    :param training: bool
    :return: tuple[int | float, int | float]
    """
    filters = {"training_data": True} if training else {}
    min_c = list(students.find(filters, student_info_projection).sort(category).limit(1))[0][category]
    max_c = list(students.find(filters, student_info_projection).sort(category, DESCENDING).limit(1))[0][category]
    return min_c, max_c


def student_iqr_percentiles(category: str) -> list[float | int]:
    """
    Calculates the iter-quartile range for a specified category and returns a list of values within the range.

    :param category: str
    :return: list[float | int]
    """
    min_c, max_c = student_min_max(category)
    samples_range = max_c - min_c
    samples_iqr = (((samples_range / 100) * 60) - ((samples_range / 100) * 40)) / 10
    return [(min_c + ((samples_range / 100) * 40)) + (i * samples_iqr) for i in range(11)]
