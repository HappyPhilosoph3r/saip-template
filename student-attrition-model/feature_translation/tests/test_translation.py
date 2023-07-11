from feature_translation import *
from db import generate_new_student, students, Student
import pandas
import os
import json


def schema():
    path = os.path.realpath('test_dataset_legend.json')
    with open(path, 'rb') as f:
        schema_info = json.load(f)
    return schema_info


def test_create_translator():
    dataframe = pandas.read_csv('test_dataset.csv')
    print(create_translator(dataframe))


def test_dataset():
    dataframe = pandas.read_csv('test_dataset.csv')
    dataset = dataframe.to_dict('records')
    return generate_new_student(dataset[0], schema())


def test_features_hr():
    student = test_dataset()
    print('ground_truth', student.info())
    print('translation', features_hr(student.features))


def test_features_n():
    student = test_dataset()
    print('ground_truth', student.features)
    print('translation ', features_n(features_hr(student.features)))


def test_features_update():
    student = test_dataset()
    student_dict = features_hr(student.features)
    print('ground_truth', student.info())
    print('translation', features_hr(student.features))
    updated_dict = features_update(student_dict, 'course', 'Biofuel Production Technologies', 'dict')
    print('updated', updated_dict)
    print('ground_truth  ', student.features)
    updated_list = features_update(student_dict, 'course', 'Biofuel Production Technologies')
    print('updated       ', updated_list)
    print('ground_truth 2', student.features)
    updated_list = features_update(student.features, 'debtor', True)
    print('updated 2     ', updated_list)


def data_integrity_check():
    print("Data integrity check initiated...")
    student_list = [Student(i) for i in list(students.find())]
    for student in student_list:
        translated = features_n(features_hr(student.features))
        for i, v in enumerate(student.features):
            assert v == translated[i]
    print("Data integrity check successfully completed")


def tests():
    data_integrity_check()
    # test_create_translator()
    # test_dataset()
    # test_features_hr()
    # test_features_n()
    # test_features_update()

if __name__ == "__main__":
    tests()
