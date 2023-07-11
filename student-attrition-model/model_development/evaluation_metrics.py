import pandas as pd
from pandas import DataFrame
import logging

logging.getLogger(__name__)


def confusion_matrix(classes: list, predictions: list, ground_truth: list, dataframe: bool = False) -> DataFrame | list:
    """
    Takes a set of predictions and actual labels and returns a content matrix in either list or DataFrame format.

    :param classes: list
    :param predictions: list
    :param ground_truth: list
    :param dataframe: bool
    :return: DataFrame | list
    """
    legend = {label: index for index, label in enumerate(classes)}
    cm = []

    for i in range(len(classes)):
        cm.append([0 for _ in range(len(classes))])

    for i in zip(predictions, ground_truth):
        cm[legend.get(i[0])][legend.get(i[1])] += 1

    if not dataframe:
        return cm
    df = pd.DataFrame(cm)

    return df


def list_division(list_a: list, list_b: list) -> list:
    """Takes two lists and divides the first by the second element wise. Returns a list with the results.

    :param list_a: list
    :param list_b: list
    :return: list
    """
    assert len(list_a) == len(list_b)
    results = list()
    for i in zip(list_a, list_b):
        if i[0] == 0 and i[1] == 0:
            results.append(1)
            continue
        if i[1] == 0:
            results.append(0)
            continue
        results.append(i[0] / i[1])
    return results


def list_sum(*args) -> list:
    """
    Takes a set of lists and sums them element wise, Returns a list with the results

    :params: *args: list
    :return: list
    """
    return [sum(i) for i in list(zip(*args))]


def list_averages(*args) -> list:
    """
    Takes a set of lists and calculates the mean of them element wise then, Returns a list with the results.

    :return: list
    """
    return [sum(i) / len(i) for i in list(zip(*args))]


def class_stats(name: str, classes: list, predictions: list, ground_truth: list, debug: bool = False):
    """
    Takes a set of predictions and actual values. Calculates various performance metrics and returns a dictionary.

    The measures used are detailed in Sokolova, M. and Lapalme, G. (2009) ‘A systematic analysis of performance measures
    for classification tasks’, Information Processing & Management, 45(4), pp. 427–437.
    Available at: https://doi.org/10.1016/j.ipm.2009.03.002.

    :param name: str
    :param classes: list
    :param predictions: list
    :param ground_truth: list
    :param debug: bool
    :return: dict
    """

    cm = confusion_matrix(classes, predictions, ground_truth)
    class_count = len(classes)

    counts = {k: len(list(filter(lambda x: x == k, ground_truth))) for k in ground_truth}

    true_positives = [cm[n][n] for n in range(class_count)]
    false_positives = [sum(value) - cm[index][index] for index, value in enumerate(cm)]
    true_negatives = [sum(true_positives) - tp for tp in true_positives]
    false_negatives = [sum(value) - true_positives[index] for index, value in enumerate(list(zip(*cm)))]

    # Precision = true_positives / (true_positives + false_positives)
    tp_fp = list_sum(true_positives, false_positives)
    precision = list_division(true_positives, tp_fp)

    # recall ( sensitivity ) = true_positives / (true_positives + false_negatives)
    tp_fn = list_sum(true_positives, false_negatives)
    recall = list_division(true_positives, tp_fn)

    # specificity = true_negatives / ( true_negatives + false_positives )
    tn_fp = list_sum(true_negatives, false_positives)
    specificity = list_division(true_negatives, tn_fp)

    # Averages
    average_accuracy = sum(list_division(list_sum(true_positives, true_negatives), list_sum(true_positives, true_negatives, false_negatives, false_positives))) / class_count
    error_rate = sum(list_division(list_sum(false_positives, false_negatives), list_sum(true_positives, true_negatives, false_negatives, false_positives))) / class_count

    # Micro averages
    precision_micro = sum(true_positives) / sum(list_sum(true_positives + false_positives))
    recall_micro = sum(true_positives) / sum(list_sum(true_positives + false_negatives))

    # Macro averages
    precision_macro = sum(precision) / len(precision)
    recall_macro = sum(recall) / len(recall)
    f_score_macro = (2 * (precision_macro * recall_macro)) / (precision_macro + recall_macro)

    if debug:
        logging.debug(f'Class statistics for {name}')
        logging.debug('label counts:', counts)
        logging.debug(f"precision: {precision}")
        logging.debug(f"recall (sensitivity): {recall}")
        logging.debug(f"specificity: {specificity}")
        logging.debug('average accuracy:', average_accuracy)
        logging.debug('error rate:', error_rate)
        logging.debug("precision_micro:", precision_micro)
        logging.debug("recall_micro:", recall_micro)
        logging.debug("precision_macro:", precision_macro)
        logging.debug("recall_macro:", recall_macro)
        logging.debug("f_score_macro:", f_score_macro)

    return {
        "model": name,
        "average_accuracy": average_accuracy,
        "error rate": error_rate,
        "precision_micro": precision_micro,
        "recall_micro": recall_micro,
        "precision_macro": precision_macro,
        "recall_macro": recall_macro,
        "f_score_macro": f_score_macro
    }
