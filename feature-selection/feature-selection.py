import traceback
from itertools import combinations
from math import ceil, log2

import weka.core.jvm as jvm
from weka.classifiers import Classifier, Evaluation
from weka.core.classes import Random
from weka.core.converters import Loader
from weka.filters import Filter


def read_dataset(dataset_name):
    loader = Loader("weka.core.converters.ArffLoader")
    dataset = loader.load_file(f"data/{dataset_name}.arff", class_index="last")
    return dataset


def search(dataset):
    classifiers = [
        ("IBk KNN", Classifier(classname="weka.classifiers.lazy.IBk")),
        ("Naive Bayes", Classifier(classname="weka.classifiers.bayes.NaiveBayes")),
        ("J48 Decision Tree", Classifier(classname="weka.classifiers.trees.J48")),
    ]

    n_columns = dataset.num_attributes - 1
    column_combinations = []
    for r in range(1, n_columns + 1):
        column_combinations.extend(list(combinations(range(n_columns), r)))

    results = {classifier[0]: [] for classifier in classifiers}
    for selected_columns in column_combinations:
        to_remove = set(range(n_columns)) - set(selected_columns)
        remove = Filter(
            classname="weka.filters.unsupervised.attribute.Remove",
            options=["-R", ",".join(map(lambda x: str(x + 1), to_remove))],
        )
        remove.inputformat(dataset)
        filtered = remove.filter(dataset)

        for classifier_name, classifier in classifiers:
            classifier.build_classifier(filtered)
            evaluation = Evaluation(filtered)
            evaluation.crossvalidate_model(classifier, filtered, 5, Random(42))
            results[classifier_name].append(
                (filtered.attribute_names()[:-1], evaluation.percent_correct)
            )

    for classifier, result in results.items():
        results[classifier] = sorted(result, key=lambda x: x[1], reverse=True)
    return results


def main():
    for dataset_name in ("iris", "glass", "diabetes"):
        print("\n", dataset_name.upper(), sep="")
        print("=" * len(dataset_name))

        dataset = read_dataset(dataset_name)
        columns = dataset.attribute_names()[:-1]
        print(f"Columns: {columns}")

        results = search(dataset)
        cols_performance = dict.fromkeys(columns, 0)
        for classifier, result in results.items():
            print(classifier)
            n = ceil(log2(len(result))) + 1
            print_results("Best", result[:n])
            print_results("Worst", result[-n:])

            for selected_columns, accuracy in result:
                n_selected = len(selected_columns)
                for column in columns:
                    if column in selected_columns:
                        cols_performance[column] += accuracy / n_selected
        cols_performance = dict(
            sorted(cols_performance.items(), key=lambda item: item[1], reverse=True)
        )
        print("\nAttribute importance (heuristic):")
        for col, performance in cols_performance.items():
            print(f"\t{col}: {performance:.4f}")


def print_results(result_type, result):
    print(f"\t{result_type}")
    for columns, accuracy in result:
        print(f"\t\t{columns}: {accuracy:.4f}%")


if __name__ == "__main__":
    try:
        jvm.start()
        main()
    except Exception as e:
        print(traceback.format_exc())
    finally:
        jvm.stop()
