from dataclasses import dataclass
from pprint import pprint
import traceback
from typing import Dict

import numpy as np
from weka.attribute_selection import ASSearch, ASEvaluation, AttributeSelection
import weka.core.jvm as jvm
from weka.classifiers import Classifier, Evaluation
from weka.core.converters import Loader
from weka.core.classes import Random
from weka.filters import Filter


@dataclass
class ClassificationResult:
    classifier: str
    accuracy: float
    confusion_matrix: np.ndarray
    summary: str

    def print(self):
        print(self.classifier)
        print(self.accuracy)
        pprint(self.confusion_matrix)
        print(self.summary)


@dataclass
class AttributeSelectionResult:
    classification_result: Dict[str, ClassificationResult]
    overall_accuracy: float
    attribute_evaluator: str
    n_important: int
    results_string: str
    search_method: str = "weka.attributeSelection.Ranker"

    def print(self):
        for result in self.classification_result:
            result.print()
        print(self.overall_accuracy, self.attribute_evaluator, self.n_important)
        print(self.results_string)


def read_dataset():
    loader = Loader("weka.core.converters.ArffLoader")
    dataset = loader.load_file(
        "data/chronic_kidney_disease_full.arff", class_index="last"
    )
    return dataset


def classify(dataset):
    classifiers = [
        ("KNN", Classifier(classname="weka.classifiers.lazy.IBk")),
        ("J48", Classifier(classname="weka.classifiers.trees.J48")),
        (
            "MLP",
            Classifier(classname="weka.classifiers.functions.MultilayerPerceptron"),
        ),
    ]

    results = []
    total = 0
    for classifier_name, classifier in classifiers:
        classifier.build_classifier(dataset)
        evaluation = Evaluation(dataset)
        evaluation.evaluate_train_test_split(classifier, dataset, 70.0, Random(42))
        results.append(
            ClassificationResult(
                classifier_name,
                evaluation.percent_correct,
                evaluation.confusion_matrix,
                evaluation.summary(),
            )
        )
        total += evaluation.percent_correct

    return results, total / len(classifiers)


def select_features(dataset):
    attribute_evaluators = [
        "weka.attributeSelection.InfoGainAttributeEval",
        "weka.attributeSelection.GainRatioAttributeEval",
        "weka.attributeSelection.CorrelationAttributeEval",
        "weka.attributeSelection.OneRAttributeEval",
    ]

    best = None
    for n_important in range(1, 24):
        for attribute_evaluator in attribute_evaluators:
            search = ASSearch("weka.attributeSelection.Ranker")
            evaluation = ASEvaluation(attribute_evaluator)
            attsel = AttributeSelection()
            attsel.ranking(True)
            attsel.folds(10)
            attsel.crossvalidation(True)
            attsel.seed(42)
            attsel.search(search)
            attsel.evaluator(evaluation)
            attsel.select_attributes(dataset)

            to_remove = attsel.ranked_attributes[n_important:, 0]

            remove = Filter(
                classname="weka.filters.unsupervised.attribute.Remove",
                options=["-R", ",".join(map(lambda x: str(int(x + 1)), to_remove))],
            )
            remove.inputformat(dataset)
            filtered = remove.filter(dataset)

            results, overall_accuracy = classify(filtered)
            if best is None or overall_accuracy > best.overall_accuracy:
                best = AttributeSelectionResult(
                    results,
                    overall_accuracy,
                    attribute_evaluator,
                    n_important,
                    attsel.results_string,
                )
                print("==================================================")
                best.print()


def main():
    dataset = read_dataset()

    # Step 2: Perform classification
    overall_classification, overall_accuracy = classify(dataset)
    print(overall_accuracy)
    for result in overall_classification:
        result.print()

    # Step 3: Find attributes with strong correlation to class
    search = ASSearch(classname="weka.attributeSelection.Ranker")
    evaluation = ASEvaluation(classname="weka.attributeSelection.PrincipalComponents")
    attsel = AttributeSelection()
    attsel.search(search)
    attsel.evaluator(evaluation)
    attsel.select_attributes(dataset)
    print(attsel.results_string)

    # Step 4: Identify the most important attributes
    select_features(dataset)



if __name__ == "__main__":
    try:
        jvm.start()
        main()
    except Exception as e:
        print(traceback.format_exc())
    finally:
        jvm.stop()
