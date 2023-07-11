import os
from db.controllers_student import *
from test_raw_data import test_sample
from pandas import DataFrame


def schema() -> dict:
    """
    Returns the json file containing all information to understand the dataset as a dictionary representation.

    :return: dict
    """
    current_file = 'test_controllers_student.py'
    root = os.path.realpath(current_file).split('student-attrition-model')[0]
    path = os.path.join(root, 'student-attrition-model', 'data', 'dataset_legend.json')
    assert os.path.exists(path)
    with open(path, 'rb') as f:
        schema_info = json.load(f)
    return schema_info


def test_training_dataset_resampled():
    assert type(training_dataset_resampled()) is tuple
    assert type(training_dataset_resampled(validation_split=True)) is tuple
    [train_data, _], [eval_data, _] = training_dataset_resampled(validation_split=True)
    print(list(filter(lambda x: None in x, train_data)))
    assert (len(train_data) / 80) * 100 == (len(eval_data) / 20) * 100


def test_generate_new_student():
    assert generate_new_student(test_sample, schema())
    # student = generate_new_student(test_sample, schema())
    # print(student.info())
    # print(student.features)


def test_generate_student_dataframe():
    assert type(generate_student_dataframe(schema())) == DataFrame


def test_student_priors():
    print(student_priors('debtor', True))
    print(student_priors('debtor', False))
    print(student_priors('tuition_fees_up_to_date', True))
    print(student_priors('scholarship_holder', True))
    print(student_priors('international', True))


def test_student_iqr_percentiles():
    print(student_iqr_percentiles("gdp"))


def test():
    print(schema())
    # test_training_dataset_resampled()
    # test_generate_new_student()  # generates new data in the database if initialisation is set to true so be careful.
    # test_generate_student_dataframe()
    # test_student_priors()
    # test_student_iqr_percentiles()


test()
