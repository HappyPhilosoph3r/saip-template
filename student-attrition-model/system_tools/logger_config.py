import logging
import os


def log_file_exists() -> bool:
    """
    Ensures that the relevant log directory and file exist. Otherwise, create them.

    :return: bool
    """
    current_file = 'logger_config.py'
    root = os.path.realpath(current_file).split('student-attrition-model')[0]
    dir_path = os.path.join(root, 'student-attrition-model', 'logs')
    file_path = os.path.join(dir_path, 'model_logs.log')
    if os.path.exists(file_path):
        return True
    if not os.path.exists(dir_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
    try:
        with open(file_path, "w") as f:
            pass
        return True
    except Exception as e:
        print(f"Logging file could not be created {e}")
        return False


def create_logger():
    """
    Initialises all logs for the project.

    :return: None
    """

    if not log_file_exists():
        return

    logging.basicConfig(filename="logs/model_logs.log",  level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

