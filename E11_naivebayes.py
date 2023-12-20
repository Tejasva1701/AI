# Write a program to show Naive Bayes Classifier Algorithm

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)


def calculate_variance(numbers, mean):
    return sum((x - mean) ** 2 for x in numbers) / (len(numbers) - 1)


def calculate_standard_deviation(variance):
    if variance == 0:
        return 0
    return variance**0.5


def summarize(attribute):
    mean_val = calculate_mean(attribute)
    variance_val = calculate_variance(attribute, mean_val)
    stdev_val = calculate_standard_deviation(variance_val)
    return mean_val, stdev_val


def separate_by_class(dataset):
    separated = {}
    for instance in dataset:
        class_value = instance[-1]
        if class_value not in separated:
            separated[class_value] = []
        separated[class_value].append(instance)
    return separated


def summarize_by_class(dataset):
    summaries = {}
    separated = separate_by_class(dataset)
    for class_value, instances in separated.items():
        summaries[class_value] = [
            summarize(attribute) for attribute in zip(*instances)]
    return summaries


def calculate_probability(x, mean, stdev):
    epsilon = 1e-10  # Small constant to avoid division by zero
    exponent = -((x - mean) ** 2) / (2 * (stdev**2 + epsilon))
    return (1 / ((2 * 3.14159265358979323846) ** 0.5 * (stdev + epsilon))) * (
        2.71828**exponent
    )


def calculate_class_probabilities(summaries, input_vector):
    probabilities = {}
    for class_value, class_summaries in summaries.items():
        probabilities[class_value] = 1
        for i in range(len(class_summaries)):
            mean, stdev = class_summaries[i]
            x = input_vector[i]
            probabilities[class_value] *= calculate_probability(x, mean, stdev)
    return probabilities


def predict(summaries, input_vector):
    probabilities = calculate_class_probabilities(summaries, input_vector)
    best_label, best_prob = None, -1
    for class_value, probability in probabilities.items():
        if best_label is None or probability > best_prob:
            best_prob = probability
            best_label = class_value
    return best_label


def naive_bayes(train, test):
    summaries = summarize_by_class(train)
    predictions = [predict(summaries, instance) for instance in test]
    return predictions


# Example usage:
dataset = [
    [3.393533211, 2.331273381, 0],
    [3.110073483, 1.781539638, 0],
    [1.343808831, 3.368360954, 0],
    [3.582294042, 4.67917911, 0],
    [2.280362439, 2.866990263, 0],
    [7.423436942, 4.696522875, 1],
    [5.745051997, 3.533989803, 1],
    [9.172168622, 2.511101045, 1],
    [7.792783481, 3.424088941, 1],
    [7.939820817, 0.791637231, 1],
]

predictions = naive_bayes(dataset, dataset)
print(predictions)



#Sample Output:
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]