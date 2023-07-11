from classifier.model_classifier import Classifier
from db import training_dataset

sample_data = training_dataset()
test_label = training_dataset()[1][0]


def test_classifier():
    classifier = Classifier()
    print(classifier.info())
    classifier.evaluate(True)
    print(classifier.info())
    # classifier.save_model()
    classifier.evaluate_individual_models()


def test_classifier_models():
    classifier = Classifier()
    classifier.evaluate_individual_models()


def test_classifier_prediction():
    classifier = Classifier()
    print(classifier.predict(sample_data[0][0]))


def test_classifier_feature_importance():
    classifier = Classifier()
    print(f"label: {sample_data[1][0]}")
    print(classifier.feature_analysis(sample_data[0][0]))
    print(f"label: {sample_data[1][1]}")
    print(classifier.feature_analysis(sample_data[0][1]))
    print(f"label: {sample_data[1][15]}")
    print(classifier.feature_analysis(sample_data[0][15]))
    print(f"label: {sample_data[1][25]}")
    print(classifier.feature_analysis(sample_data[0][25]))


def tests():
    # test_classifier()
    # test_classifier_models()
    test_classifier_prediction()
    test_classifier_feature_importance()


if __name__ == "__main__":
    tests()
