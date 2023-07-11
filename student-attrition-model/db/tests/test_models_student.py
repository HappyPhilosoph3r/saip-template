from db.models_student import Student
from test_data import test_sample


def test_student_class():
    assert Student()
    assert Student(test_sample)._id


def test():
    test_student_class()


if __name__ == "__main__":
    test()
