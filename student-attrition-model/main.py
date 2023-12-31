from initialise_data import initialise_database
from db import student_overview
from quart import Quart
from routes import classifier_routes
from system_tools import logger_config
import logging

logging.getLogger(__name__)

app = Quart(__name__)
app.register_blueprint(classifier_routes, url_prefix='/api/')


def create_app() -> None:
    """
    Initialises quart app

    :return: None
    """
    try:
        logger_config.create_logger()
    except Exception as e:
        print(f"Logger could not be created... proceeding without logging: {e}")
    finally:
        logging.info("Server initialised")
        initialise_database()
        logging.info(f'Student Database Overview: {student_overview()}')
        app.run(host='0.0.0.0', port=8000)


if __name__ == '__main__':
    create_app()
