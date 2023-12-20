# Write a program to reduce the number of Dimensions using principal component analysis (PCA)

import random


def mean(values):
    return sum(values) / len(values)


def covariance_matrix(data):
    n_features = len(data[0])
    means = [mean([row[i] for row in data]) for i in range(n_features)]
    centered_data = [[entry - means[i]
                      for i, entry in enumerate(row)] for row in data]
    cov_matrix = [[0] * n_features for _ in range(n_features)]
    for i in range(n_features):
        for j in range(n_features):
            cov_matrix[i][j] = sum(
                centered_data[k][i] * centered_data[k][j] for k in range(len(data))
            )
    return cov_matrix


def power_iteration(matrix, max_iterations=1000, epsilon=1e-6):
    n = len(matrix)
    b = [random.random() for _ in range(n)]
    for _ in range(max_iterations):
        b_next = [0] * n
        for i in range(n):
            for j in range(n):
                b_next[i] += matrix[i][j] * b[j]
        norm = sum(x**2 for x in b_next) ** 0.5
        b_next = [x / norm for x in b_next]
        if sum((x - y) ** 2 for x, y in zip(b_next, b)) < epsilon:
            return b_next
        b = b_next
    return b


def pca(data, num_components):
    cov_matrix = covariance_matrix(data)
    eigenvectors = [power_iteration(cov_matrix) for _ in range(num_components)]
    projected_data = [
        [
            sum(eigenvector[i] * row[i] for i in range(len(row)))
            for eigenvector in eigenvectors
        ]
        for row in data
    ]
    return projected_data


# Example usage:
data_points = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

num_components = 2
projected_data = pca(data_points, num_components)

# Print projected data
for row in projected_data:
    print(row)

# Sample Output:
# [3.4641016151377544, 3.4641016151377544]
# [8.660254037844386, 8.660254037844386]
# [13.856406460551018, 13.856406460551018]
