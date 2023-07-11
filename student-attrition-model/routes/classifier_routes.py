from quart import Blueprint, request
from initialise_classifier import classifier_model
from feature_translation import features_n
import json


classifier_routes = Blueprint("classifier_routes", __name__)


@classifier_routes.route("/test")
def hello_world_test():
    """
    Returns a html str for test purposes.

    :return: str
    """
    return "<p>Hello, World!</p>"


@classifier_routes.route("/performance_analysis", methods=["POST"])
async def analyse_user_data():
    """
    Take the data provided by the user and return the relevant feature analysis.

    :return: JSON str
    """
    try:
        data = await request.data
        data_dict = json.loads(data.decode("utf-8"))
        features = features_n(data_dict)
        results = classifier_model.feature_analysis(features)
        return json.dumps(results), 200, {'ContentType': 'application/json'}
    except Exception as e:
        return json.dumps({'error': e}), 500, {'ContentType': 'application/json'}
