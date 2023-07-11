from bson import ObjectId
from db.services_pymongo import controls
import logging

logging.getLogger(__name__)


class Controls:
    """
        This class contains all properties and methods for the controls that determine platform functionality


        Attributes

        _id: ObjectId | str | None - Database id value for each individual instance of the class (unique)

        name: str - Label for each individual instance of the class (unique)

        feature_translation: list - A list of all encoded feature labels in a specified order

        meta_translation: list - A list of all encoded feature categories in a specified order


        Methods

        info: dict - Returns a dictionary containing the relevant information for the class instance.

        info_db: dict - Returns all relevant class variables as a dict for the purpose of creating / updating the
                        database.

        create_document: bool - Adds the document to the database.

        update_document: bool - Updates the relevant document in the database.
    """
    def __init__(self, attributes: dict | None = None):
        self._id: ObjectId | str | None = None
        self.name = "control"
        self.feature_translation: list | None = None
        self.meta_translation: list | None = None

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
            "name": self.name,
            "feature_translation": self.feature_translation,
            "meta_translation": self.meta_translation
        }

    def info_db(self) -> dict:
        """
         Return all class variables (excluding self._id) as a dict for the purpose of creating / updating the database.

        :return: dict
        """
        info = self.info()
        del info["_id"]

        return info

    def create_document(self) -> bool:
        """
        Adds the document to the database.

        :return: bool
        """
        try:
            inserted = controls.insert_one(self.info_db())
            self._id = ObjectId(inserted.inserted_id)
            logging.info('Controls successfully created')
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
            assert self.name
            controls.update_one({"name": self.name}, {"$set": self.info_db()})
            logging.info('Controls successfully updated')
            return True
        except Exception as e:
            logging.error(f'Document with id {self.name} could not be updated', e)
            return False
