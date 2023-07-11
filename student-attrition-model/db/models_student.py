from bson import ObjectId
from db.services_pymongo import students
import logging

logging.getLogger(__name__)


class Student:
    """
    This class contains all properties and methods for a student in the dataset

    For a full list of all possible values for the categorical features please see the dataset_legend.json.


    Attributes

    _id: ObjectId | str | None - The human-readable representation of the named feature.

    marital_status: str | None - The human-readable representation of the named feature.

    application_mode: str | None - The human-readable representation of the named feature.

    application_order: int | None - The numeric representation of the named feature.

    course: str | None - The human-readable representation of the named feature.

    attendance_type: str | None - The human-readable representation of the named feature.

    previous_qualification: str | None - The human-readable representation of the named feature.

    nationality: str | None - The human-readable representation of the named feature.

    mothers_qualification: str | None - The human-readable representation of the named feature.

    fathers_qualification: str | None - The human-readable representation of the named feature.

    mothers_occupation: str | None - The human-readable representation of the named feature.

    fathers_occupation: str | None - The human-readable representation of the named feature.

    displaced: bool | None - The human-readable representation of the named feature.

    educational_special_needs: bool | None - The human-readable representation of the named feature.

    debtor: bool | None - The human-readable representation of the named feature.

    tuition_fees_up_to_date: bool | None - The human-readable representation of the named feature.

    gender: str | None - The human-readable representation of the named feature.

    scholarship_holder: bool | None - The human-readable representation of the named feature.

    age_at_enrolment: int | None - The human-readable representation of the named feature.

    international: bool | None - The human-readable representation of the named feature.

    curricular_units_1st_semester_credited: int | float | None - The numeric representation of the named feature.

    curricular_units_1st_semester_enrolled: int | float | None - The numeric representation of the named feature.

    curricular_units_1st_semester_evaluations: int | float | None - The numeric representation of the named feature.

    curricular_units_1st_semester_approved: int | float | None - The numeric representation of the named feature.

    curricular_units_1st_semester_grade: int | float | None - The numeric representation of the named feature.

    curricular_units_1st_semester_without_evaluations: int | float | None - The numeric representation of the named feature.

    curricular_units_2nd_semester_credited: int | float | None - The numeric representation of the named feature.

    curricular_units_2nd_semester_enrolled: int | float | None - The numeric representation of the named feature.

    curricular_units_2nd_semester_evaluations: int | float | None - The numeric representation of the named feature.

    curricular_units_2nd_semester_approved: int | float | None - The numeric representation of the named feature.

    curricular_units_2nd_semester_grade: int | float | None - The numeric representation of the named feature.

    curricular_units_2nd_semester_without_evaluations: int | float | None - The numeric representation of the named feature.

    unemployment_rate: int | float | None - The numeric representation of the named feature.

    inflation_rate: int | float | None - The numeric representation of the named feature.

    gdp: int | float | None - The numeric representation of the named feature.

    target: str | None - The ground truth label for the sample.

    features: list[int | float] | None - The numerical representation of the features for the sample.


    Metadata Attributes

    training_data: bool - Determines whether the sample is included in the training dataset.

    test_data: bool -  Determines whether the sample is included in the test dataset.


    Methods

     info: dict - Returns a dictionary containing the relevant information for the class instance.

    info_db: dict - Returns all relevant class variables as a dict for the purpose of creating / updating the
                    database.

    create_document: bool - Adds the document to the database.

    update_document: bool - Updates the relevant document in the database.

    set_training_status: None - Set the training_data and test_data status and update the document in the database.


    """
    def __init__(self, attributes: dict | None = None):
        self._id: ObjectId | str | None = None
        self.marital_status: str | None = None
        self.application_mode: str | None = None
        self.application_order: int | None = None
        self.course: str | None = None
        self.attendance_type: str | None = None
        self.previous_qualification: str | None = None
        self.nationality: str | None = None
        self.mothers_qualification: str | None = None
        self.fathers_qualification: str | None = None
        self.mothers_occupation: str | None = None
        self.fathers_occupation: str | None = None
        self.displaced: bool | None = None
        self.educational_special_needs: bool | None = None
        self.debtor: bool | None = None
        self.tuition_fees_up_to_date: bool | None = None
        self.gender: str | None = None
        self.scholarship_holder: bool | None = None
        self.age_at_enrolment: int | None = None
        self.international: bool | None = None
        self.curricular_units_1st_semester_credited: int | float | None = None
        self.curricular_units_1st_semester_enrolled: int | float | None = None
        self.curricular_units_1st_semester_evaluations: int | float | None = None
        self.curricular_units_1st_semester_approved: int | float | None = None
        self.curricular_units_1st_semester_grade: int | float | None = None
        self.curricular_units_1st_semester_without_evaluations: int | float | None = None
        self.curricular_units_2nd_semester_credited: int | float | None = None
        self.curricular_units_2nd_semester_enrolled: int | float | None = None
        self.curricular_units_2nd_semester_evaluations: int | float | None = None
        self.curricular_units_2nd_semester_approved: int | float | None = None
        self.curricular_units_2nd_semester_grade: int | float | None = None
        self.curricular_units_2nd_semester_without_evaluations: int | float | None = None
        self.unemployment_rate: int | float | None = None
        self.inflation_rate: int | float | None = None
        self.gdp: int | float | None = None
        self.target: str | None = None

        # feature vector
        self.features: list | None = None

        # metadata
        self.training_data: bool = False
        self.test_data: bool = False

        if attributes:
            for k, v in attributes.items():
                setattr(self, k, v)

    def info(self) -> dict:
        """
         Returns a dictionary containing the relevant information for the class instance.

        :return: dict
        """
        return {
            "_id": str(self._id),
            "marital_status": self.marital_status,
            "application_mode": self.application_mode,
            "application_order": self.application_order,
            "course": self.course,
            "attendance_type": self.attendance_type,
            "previous_qualification": self.previous_qualification,
            "nationality": self.nationality,
            "mothers_qualification": self.mothers_qualification,
            "fathers_qualification": self.fathers_qualification,
            "mothers_occupation": self.mothers_occupation,
            "fathers_occupation": self.fathers_occupation,
            "displaced": self.displaced,
            "educational_special_needs": self.educational_special_needs,
            "debtor": self.debtor,
            "tuition_fees_up_to_date": self.tuition_fees_up_to_date,
            "gender": self.gender,
            "scholarship_holder": self.scholarship_holder,
            "age_at_enrolment": self.age_at_enrolment,
            "international": self.international,
            "curricular_units_1st_semester_credited": self.curricular_units_1st_semester_credited,
            "curricular_units_1st_semester_enrolled": self.curricular_units_1st_semester_enrolled,
            "curricular_units_1st_semester_evaluations": self.curricular_units_1st_semester_evaluations,
            "curricular_units_1st_semester_approved": self.curricular_units_1st_semester_approved,
            "curricular_units_1st_semester_grade": self.curricular_units_1st_semester_grade,
            "curricular_units_1st_semester_without_evaluations": self.curricular_units_1st_semester_without_evaluations,
            "curricular_units_2nd_semester_credited": self.curricular_units_2nd_semester_credited,
            "curricular_units_2nd_semester_enrolled": self.curricular_units_2nd_semester_enrolled,
            "curricular_units_2nd_semester_evaluations": self.curricular_units_2nd_semester_evaluations,
            "curricular_units_2nd_semester_approved": self.curricular_units_2nd_semester_approved,
            "curricular_units_2nd_semester_grade": self.curricular_units_2nd_semester_grade,
            "curricular_units_2nd_semester_without_evaluations": self.curricular_units_2nd_semester_without_evaluations,
            "unemployment_rate": self.unemployment_rate,
            "inflation_rate": self.inflation_rate,
            "gdp": self.gdp,
            "target": self.target
        }

    def info_db(self) -> dict:
        """
         Return all class variables (excluding self._id) as a dict for the purpose of creating / updating the database

        :return: dict
        """
        info = self.info()
        del info["_id"]

        # add feature vector
        info['features'] = self.features

        # add metadata
        info["training_data"] = self.training_data
        info["test_data"] = self.test_data

        return info

    def create_document(self) -> bool:
        """
        Adds the document to the database.

        :return: bool
        """
        try:
            inserted = students.insert_one(self.info_db())
            self._id = ObjectId(inserted.inserted_id)
        except Exception as e:
            if type(e).__name__ == 'DuplicateKeyError':
                logging.error('Error: A document with these properties already exists')
            else:
                logging.error(f'An error occurred creating a new student', e)
            return False

        return True

    def update_document(self) -> bool:
        """
        Updates the relevant document in the database.

        :return: bool
        """
        try:
            students.update_one({"_id": self._id}, {"$set": self.info_db()})
            return True
        except Exception as e:
            logging.error(f'Document with id {self._id} could not be updated', e)
            return False

    def set_training_status(self, training: bool = True):
        """
        Set the training_data and test_data status and update the document in the database.

        :return: None
        """
        if training:
            self.training_data = True
            self.test_data = False
        else:
            self.training_data = False
            self.test_data = True
        self.update_document()
