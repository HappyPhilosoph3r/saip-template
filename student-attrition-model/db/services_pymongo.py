from pymongo import MongoClient, ASCENDING
from pymongo.collection import Collection

# Connect to mongoDB
client = MongoClient('mongodb://localhost:27017/')

# Connect to specific database
db = client.student_attrition_intervention

# Connect to specific collection in database
students: Collection = db.students
controls: Collection = db.controls


def create_index(collection: Collection, attribute: str) -> str:
    """
    Create indexes to ensure that no duplicates are added to database.

    :param collection: Collection
    :param attribute: str
    :return: str

    """
    return collection.create_index([(attribute, ASCENDING)], unique=True)


def create_all_indexes() -> None:
    """
    Create all relevant indexes required by the database.

    :return: None
    """
    create_index(controls, "name")

