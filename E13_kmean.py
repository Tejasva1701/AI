# Write a program to implement K-mean Clustering

import random

def euclidean_distance(point1, point2):
    return sum((x - y) ** 2 for x, y in zip(point1, point2)) ** 0.5

def assign_to_clusters(data, centroids):
    clusters = {i: [] for i in range(len(centroids))}

    for point in data:
        distances = [euclidean_distance(point, centroid) for centroid in centroids]
        cluster_index = distances.index(min(distances))
        clusters[cluster_index].append(point)

    return clusters

def update_centroids(clusters):
    centroids = [
        list(map(lambda x: sum(x) / len(x), zip(*cluster)))
        for cluster in clusters.values()
    ]
    return centroids

def k_means(data, k, max_iterations=100):
    # Randomly initialize centroids
    centroids = random.sample(data, k)

    for _ in range(max_iterations):
        # Assign data points to clusters
        clusters = assign_to_clusters(data, centroids)

        # Update centroids
        new_centroids = update_centroids(clusters)

        # Check for convergence
        if new_centroids == centroids:
            break

        centroids = new_centroids

    return clusters

# Example usage:
data_points = [[1, 2], [2, 3], [5, 6], [7, 8], [8, 7], [3, 2]]

k = 2
clusters_result = k_means(data_points, k)

# Print clusters
for i, cluster in clusters_result.items():
    print(f"Cluster {i + 1}: {cluster}")

#Sample output
# Cluster 1: [[1, 2], [2, 3], [3, 2]]
# Cluster 2: [[5, 6], [7, 8], [8, 7]]