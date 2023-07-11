from db.models_controls import Controls
from db.services_pymongo import controls
import logging

logging.getLogger(__name__)


def get_controls() -> Controls:
    """
    Retrieves the controls for the intervention platform from the database and returns them.

    :return: Controls
    """
    return Controls(controls.find_one({"name": "control"}))


def create_controls(attributes: dict) -> bool:
    """
    Creates an instance of controls for the intervention platform. Returns boolean depending on success of creation.

    There should only be one instance of controls in the database, which contains all variables used to set default
    values or variables required for the running of the platform.

    :param attributes: dict
    :return: bool
    """
    try:
        return Controls(attributes).create_document()
    except Exception as e:
        logging.error("Controls could not be created", e)
        return False


def update_controls(attributes: dict) -> bool:
    """
        Updates the instance of controls for the intervention platform. Returns boolean depending on success of update.

        There should only be one instance of controls in the database, which contains all variables used to set default
        values or variables required for the running of the platform.

        :param attributes: dict
        :return: bool
    """
    try:
        return Controls(attributes).update_document()
    except Exception as e:
        logging.error("Controls could not be updated", e)
        return False
