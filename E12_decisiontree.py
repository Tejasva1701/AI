# Write a program to implement Deicision Tree Classification Algorithm

class Node:
    def __init__(
        self, data=None, feature=None, value=None, left=None, right=None, label=None
    ):
        self.data = data  # Subset of the dataset at this node
        self.feature = feature  # Feature index for splitting
        self.value = value  # Threshold value for splitting
        self.left = left  # Left child node
        self.right = right  # Right child node
        self.label = label  # Predicted label (for leaf nodes)


def gini_impurity(labels):
    total_samples = len(labels)
    if total_samples == 0:
        return 0

    counts = {label: labels.count(label) for label in set(labels)}
    impurity = 1 - sum((count / total_samples) **
                       2 for count in counts.values())
    return impurity


def split_dataset(dataset, feature, value):
    left_data = [
        instance for instance in dataset if instance[feature] <= value]
    right_data = [
        instance for instance in dataset if instance[feature] > value]
    return left_data, right_data


def find_best_split(dataset):
    features = len(dataset[0]) - 1
    total_samples = len(dataset)
    initial_impurity = gini_impurity([instance[-1] for instance in dataset])
    best_gain = 0
    best_split = None

    for feature in range(features):
        feature_values = set(instance[feature] for instance in dataset)
        for value in feature_values:
            left_data, right_data = split_dataset(dataset, feature, value)
            if len(left_data) == 0 or len(right_data) == 0:
                continue

            left_impurity = gini_impurity(
                [instance[-1] for instance in left_data])
            right_impurity = gini_impurity(
                [instance[-1] for instance in right_data])

            weighted_impurity = (len(left_data) / total_samples) * left_impurity + (
                len(right_data) / total_samples
            ) * right_impurity

            information_gain = initial_impurity - weighted_impurity

            if information_gain > best_gain:
                best_gain = information_gain
                best_split = (feature, value)

    return best_split


def build_tree(dataset, depth=0, max_depth=None):
    labels = [instance[-1] for instance in dataset]

    # Check for pure node or max depth reached
    if len(set(labels)) == 1 or (max_depth is not None and depth == max_depth):
        return Node(label=labels[0])

    # Find the best split
    best_split = find_best_split(dataset)
    if best_split is None:
        return Node(label=max(set(labels), key=labels.count))

    feature, value = best_split
    left_data, right_data = split_dataset(dataset, feature, value)

    # Recursive call for left and right subtrees
    left_child = build_tree(left_data, depth + 1, max_depth)
    right_child = build_tree(right_data, depth + 1, max_depth)

    return Node(
        data=dataset, feature=feature, value=value, left=left_child, right=right_child
    )


def predict(node, instance):
    if node.label is not None:
        return node.label

    if instance[node.feature] <= node.value:
        return predict(node.left, instance)
    else:
        return predict(node.right, instance)


def decision_tree_classification(train_data, test_data, max_depth=None):
    root = build_tree(train_data, max_depth=max_depth)
    predictions = [predict(root, instance) for instance in test_data]
    return predictions


# Example usage:
train_data = [[2, 3, 0], [1, 2, 0], [3, 4, 1], [5, 6, 1]]

test_data = [[4, 5], [6, 7]]

predictions = decision_tree_classification(train_data, test_data, max_depth=2)
print("Predictions:", predictions)


#Sample Output:
# Predictions: [1, 1]