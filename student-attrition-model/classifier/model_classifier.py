from db import training_dataset, student_iqr_percentiles
from feature_translation import features_hr, features_update, get_dataset_schema, get_dict_key_by_value
import logging
from model_development import class_stats
import os
import pickle
import pandas as pd
from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

logging.getLogger(__name__)


def model_pickle_location() -> str:
    """
    Returns path of pickle file containing model or path of the file to be created.

    :return: str
    """
    current_file = 'model_classifier.py'
    root = os.path.realpath(current_file).split('student-attrition-model')[0]
    return os.path.join(root, 'student-attrition-model', 'classifier', 'classifier_models.pickle')


def list_averages(*args) -> list:
    """
    Takes a set of lists and calculates the mean of them element wise then, Returns a list with the results

    :return: list
    """
    return [sum(i) / len(i) for i in list(zip(*args))]


model_location = model_pickle_location()


class Classifier:
    """
        This class contains all properties and methods for the classifier.


        Attributes

        name: str - Name of the classifier

        rfc: RandomForestClassifier - Random Forest Classifier model

        svc: SVC - Support Vector Classifier model

        knn: KNeighborsClassifier - K-Nearest Neighbours model

        adb: AdaBoostClassifier - ADABoost Classifier

        classes: list - Complete list of all possible label for the dataset

        trained: bool - An indication of whether the classifier has been trained yet

        average_accuracy: float | None - Calculates accuracy of the model by using the mean class precision

        error_rate: float | None - Calculates the error rate of the model by averaging the error rate per class

        precision_micro: float | None - Calculates the precision of the model by using per class metrics

        recall_micro: float | None - Calculates the recall of the model by using per class metrics

        precision_macro: float | None - Calculates the precision of the model by using total values for metrics

        recall_macro: float | None - Calculates the recall of the model by using total values for metrics

        f_score_macro: float | None - Calculates the f-score of thr model using total values for metrics


        Methods

        info: dict - Returns a dictionary containing the relevant information for this Classifier class instance.

        train: None - Trains the individual models using the training dataset.

        save_model: None - Creates a pickle file which saves the individual models in their current state.

        load_model: None - Attempts to load the individual models from the specified pickle file.

        evaluate: None - Sets the evaluation metric variables.

        evaluate_individual_models: DataFrame - Generates evaluation statistics on an individual class basis.

        predict: tuple[str, float] - Calculates the prediction for the given data.

        feature_difference: float - Calculate the impact of changing a feature.

        feature_analysis: dict - Calculates the impact of each feature for an individual data sample.

    """
    def __init__(self):
        self.name = "classifier"
        self.rfc = RandomForestClassifier(max_depth=10, min_samples_leaf=1, n_estimators=90)
        self.svc = SVC(probability=True, class_weight={"Graduate": 1, "Dropout": 1, "Enrolled": 1}, kernel='linear', C=1)
        self.knn = KNeighborsClassifier(n_neighbors=10, algorithm='ball_tree', leaf_size=1)
        self.adb = AdaBoostClassifier(algorithm='SAMME.R', learning_rate=0.5, n_estimators=80)
        self.classes = list()
        self.trained = False

        # Evaluation
        self.average_accuracy = None
        self.error_rate = None
        self.precision_micro = None
        self.recall_micro = None
        self.precision_macro = None
        self.recall_macro = None
        self.f_score_macro = None

        self.load_model()
        if not self.trained:
            self.train()
        self.evaluate()

    def info(self) -> dict:
        """
        Returns a dictionary containing the relevant information for this Classifier class instance.

        :return: dict
        """
        return {
            "name": self.name,
            "classes": self.classes,
            "trained": self.trained,
            "average_accuracy": self.average_accuracy,
            "error_rate": self.error_rate,
            "precision_micro": self.precision_micro,
            "recall_micro": self.recall_micro,
            "precision_macro": self.precision_macro,
            "recall_macro": self.recall_macro,
            "f_score_macro": self.f_score_macro,
        }

    def train(self) -> None:
        """
        Trains the individual models using the training dataset. Also sets the classes and trained variables.

        :return: None
        """
        logging.info("training model from dataset ...")
        [x_train, y_train], _ = training_dataset(True)
        if len(x_train) == 0 or len(y_train) == 0:
            return
        self.rfc.fit(x_train, y_train)
        self.svc.fit(x_train, y_train)
        self.knn.fit(x_train, y_train)
        self.adb.fit(x_train, y_train)
        self.classes = list(self.rfc.classes_)
        self.trained = True

    def save_model(self) -> None:
        """
        Creates a pickle file which saves the individual models in their current state.

        If a pickle file already exists this file is deleted and replaced with a new file.

        :return: None
        """
        try:
            if os.path.exists(model_location):
                os.remove(model_location)
        except Exception as e:
            logging.error(f"Could not save model: {e}")
            return
        with open(model_location, "wb") as f:
            pickle.dump([self.rfc, self.svc, self.knn, self.adb], f)
            f.close()

    def load_model(self) -> None:
        """
        Attempts to load the individual models from the specified pickle file and if successful set trained to true.

        :return: None
        """
        try:
            with open(model_location, "rb") as f:
                self.rfc, self.svc, self.knn, self.adb = pickle.load(f)
            self.classes = list(self.rfc.classes_)
            self.trained = True
        except Exception as e:
            self.trained = False
            logging.error(f"Failed to load model: {e}")

    def evaluate(self, training: bool = False) -> None:
        """
        Sets the various evaluation metrics by applying them to the predictions for the evaluation dataset.

        If training is set to True then the metrics are applied to the training predictions and the results are logged.

        :param training: bool
        :return: None
        """
        if not self.trained:
            return
        [x_train, y_train], [x_val, y_val] = training_dataset(True)
        if training:
            training_predictions = [self.predict(i)[0] for i in x_train]
            training_cs = class_stats("Training Model", self.classes, training_predictions, y_train)
            logging.info(f"class stats for classifier: {training_cs}")
        eval_predictions = [self.predict(i)[0] for i in x_val]
        cs = class_stats("classifier", self.classes, eval_predictions, y_val)
        for k, v in cs.items():
            setattr(self, k, v)

    def evaluate_individual_models(self, save=False) -> DataFrame:
        """
        Generates evaluation statistics on an individual class basis, returns a pandas DataFrame.

        The save variable determines whether the evaluation data is exported to a csv file or not.

        :param save: bool
        :return: DataFrame
        """
        evaluation_df = pd.DataFrame()
        [_, _], [x_val, y_val] = training_dataset(True)
        for k, v in {"Random Forest": self.rfc, "SVC": self.svc, "KNN": self.knn, "Adaboost": self.adb}.items():
            predictions_raw = [v.predict_proba([i])[0] for i in x_val]
            predictions = [self.classes[list(prediction).index(max(prediction))] for prediction in predictions_raw]
            cs = class_stats(k, list(v.classes_), predictions, y_val)
            cs_dict = {k: [v] for k, v in cs.items()}
            evaluation_df = pd.concat([pd.DataFrame.from_dict(cs_dict, orient="columns"), evaluation_df], join='outer')
        if save:
            evaluation_df.to_csv("model_evaluation.csv")
        return evaluation_df

    def predict(self, data: list[float | int]) -> tuple[str, float]:
        """
        Calculates the prediction for the given data and returns the relevant label and probability score.

        :param data: list[float | int]
        :return: tuple[str, float]

        """
        if not self.trained:
            self.train()
        assert self.trained
        rfc_prediction = self.rfc.predict_proba([data])[0]
        svc_prediction = self.svc.predict_proba([data])[0]
        knn_prediction = self.knn.predict_proba([data])[0]
        adb_prediction = self.adb.predict_proba([data])[0]
        prediction = list_averages(rfc_prediction, svc_prediction, knn_prediction, adb_prediction)
        return self.classes[list(prediction).index(max(prediction))], max(prediction)

    def feature_difference(self, data: list, feature: str, new_value: str | int | float | bool) -> float:
        """
        Calculate the impact of changing a feature by measuring the difference in the probability score.

        Take the data and predict a score, then alter the data by updating the selected feature with the new chosen
        value. Generate an updated prediction and then calculate the difference.

        :param data: list
        :param feature: str
        :param new_value: str | int | float | bool
        :return: float
        """
        _, prediction_score = self.predict(data)
        data_updated = features_update(data, feature, new_value)
        _, edited_score = self.predict(data_updated)
        return edited_score - prediction_score

    def feature_analysis(self, data: list) -> dict:
        """
        Calculates the impact of each feature for an individual data sample. Returns a dict of the results.

        Each feature is analysed independently to ascertain the difference that altering the value of that feature
        makes. The features are also grouped by meta-categories, so the analysis also explores the combined effect of
        each of these meta-categories to determine which one have the greatest impressing on the overall score.

        :param data: list
        :return: dict
        """
        feature_dict = dict()
        feature_strength = 0
        feature_main = ""
        schema = get_dataset_schema()
        prediction_class, prediction_score = self.predict(data)
        graduate = prediction_class == "Graduate"
        for key, value in features_hr(data).items():
            if schema["variable_categories"][key] == "static":
                continue
            if schema["variable_types"][key] == "binary":
                difference = self.feature_difference(data, key, not value)
            elif schema["variable_types"][key] == "boolean":
                categories = list(schema[key].values())
                categories.remove(value)
                difference = self.feature_difference(data, key, categories[0])
            elif schema["variable_types"][key] == "one_hot_encoded":
                diff_final = 0
                meta_key = f"parental_{key.split('_')[1]}_categories" if "mother" in key or "father" in key else key
                for v in schema[meta_key].values():
                    diff_temp = self.feature_difference(data, key, v)
                    if (graduate and diff_temp > diff_final) or (not graduate and diff_temp < diff_final):
                        diff_final = diff_temp
                difference = diff_final
            elif schema["variable_types"][key] == "numeric":
                diff_final = 0
                for v in student_iqr_percentiles(key):
                    diff_temp = self.feature_difference(data, key, v)
                    if (graduate and diff_temp > diff_final) or (not graduate and diff_temp < diff_final):
                        diff_final = diff_temp
                difference = diff_final
            else:
                continue

            if (graduate and difference > feature_strength) or (not graduate and difference < feature_strength):
                feature_strength = difference
                feature_main = key

            if (graduate and difference < 0) or (not graduate and difference > 0):
                continue

            category = schema["variable_categories"][key]
            if feature_dict.get(category):
                feature_dict[category] = feature_dict.get(category) + difference
            else:
                feature_dict[category] = difference

        for key, value in feature_dict.items():
            count = len(list(filter(lambda x: x == key, schema["variable_categories"].values())))
            feature_dict[key] = value / count

        optimum_category_value = max(feature_dict.values()) if graduate else min(feature_dict.values())
        optimum_category = get_dict_key_by_value(feature_dict, optimum_category_value)

        return {
            "label": prediction_class,
            "score": prediction_score,
            "feature_main": feature_main,
            "feature_strength": feature_strength,
            "optimum_category": optimum_category,
            "optimum_category_value": optimum_category_value,
            "feature_dict": feature_dict
        }
