# Write a program to implement K-nearest neighbours classification

def euclidean_distance(point1, point2):
    return sum((x - y) ** 2 for x, y in zip(point1, point2)) ** 0.5

def majority_vote(labels):
    label_counts = {}
    for label in labels:
        label_counts[label] = label_counts.get(label, 0) + 1
    sorted_labels = sorted(label_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_labels[0][0]

def knn_predict(training_data, training_labels, new_data, k):
    distances_and_labels = [
        (euclidean_distance(new_data, data), label)
        for data, label in zip(training_data, training_labels)
    ]
    sorted_distances_and_labels = sorted(distances_and_labels, key=lambda x: x[0])
    k_nearest_neighbors = sorted_distances_and_labels[:k]

    # Extract labels of the k-nearest neighbors
    k_nearest_labels = [label for _, label in k_nearest_neighbors]

    # Make a prediction based on majority vote
    prediction = majority_vote(k_nearest_labels)

    return prediction

def main():
    # Sample data
    training_data = [[2, 3], [1, 2], [3, 4], [5, 6]]
    training_labels = [0, 0, 1, 1]

    # New data point to classify
    new_data_point = [4, 5]

    # Hyperparameter: Number of neighbors (k)
    k = 3

    # Make a prediction
    prediction = knn_predict(training_data, training_labels, new_data_point, k)

    print(f"Predicted label for {new_data_point}: {prediction}")

if __name__ == "__main__":
    main()

# Sample Output:
# Predicted label for [4, 5]: 1
