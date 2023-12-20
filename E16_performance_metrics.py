# Write a program to evaluate the performance of any classification model using metrics like accuracy, precision, recall, F1-score, etc.

def evaluate_classification_model(true_labels, predicted_labels):
    if len(true_labels) != len(predicted_labels):
        raise ValueError("Input lists must have the same length.")

    true_positive = true_negative = false_positive = false_negative = 0

    for true_label, predicted_label in zip(true_labels, predicted_labels):
        if true_label == 1 and predicted_label == 1:
            true_positive += 1
        elif true_label == 0 and predicted_label == 0:
            true_negative += 1
        elif true_label == 0 and predicted_label == 1:
            false_positive += 1
        elif true_label == 1 and predicted_label == 0:
            false_negative += 1

    accuracy = (
        (true_positive + true_negative) / len(true_labels)
        if len(true_labels) > 0
        else 0
    )
    precision = (
        true_positive / (true_positive + false_positive)
        if (true_positive + false_positive) > 0
        else 0
    )
    recall = (
        true_positive / (true_positive + false_negative)
        if (true_positive + false_negative) > 0
        else 0
    )
    f1_score = (
        2 * (precision * recall) / (precision + recall)
        if (precision + recall) > 0
        else 0
    )

    return accuracy, precision, recall, f1_score


# Example usage:
true_labels = [1, 0, 1, 0, 1, 1, 0, 0]
predicted_labels = [1, 0, 1, 0, 1, 0, 1, 1]

accuracy, precision, recall, f1_score = evaluate_classification_model(
    true_labels, predicted_labels
)

print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-Score: {f1_score:.2f}")

# Sample output: 
# Accuracy: 0.62
# Precision: 0.60
# Recall: 0.75
# F1-Score: 0.67

