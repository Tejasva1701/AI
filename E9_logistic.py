# Write a program to implement Logistic Regression


import math
def sigmoid(z):
    return 1 / (1 + 2.71828 ** (-z))  # Basic implementation of the sigmoid function

def initialize_parameters(num_features):
    theta = [0] * num_features
    bias = 0
    return theta, bias

def hypothesis(X, theta, bias):
    z = sum(xi * ti for xi, ti in zip(X, theta)) + bias
    return sigmoid(z)

def calculate_cost(y, y_pred):
    m = len(y)
    cost = -(1 / m) * sum(
        yi * (2.71828 ** (math.log(ypi))) + (1 - yi) * (2.71828 ** (math.log(1 - ypi)))
        for yi, ypi in zip(y, y_pred)
    )
    return cost

def gradient_descent(X, y, theta, bias, learning_rate, num_iterations):
    m = len(y)

    for i in range(num_iterations):
        y_pred = [hypothesis(xi, theta, bias) for xi in X]
        cost = calculate_cost(y, y_pred)

        # Update parameters
        dz = [ypi - yi for yi, ypi in zip(y, y_pred)]
        dw = [1 / m * sum(dzi * xi for dzi, xi in zip(dz, X)) for X in zip(*X)]
        db = 1 / m * sum(dz)

        theta = [theta_i - learning_rate * dw_i for theta_i, dw_i in zip(theta, dw)]
        bias = bias - learning_rate * db

        if i % 100 == 0:
            print(f"Iteration {i}, Cost: {cost}")

    return theta, bias

def predict(X, theta, bias):
    y_pred = [hypothesis(xi, theta, bias) for xi in X]
    return [(1 if ypi >= 0.5 else 0) for ypi in y_pred]

def main():
    # Sample data
    X = [[2, 3], [1, 2], [3, 4], [5, 6]]
    y = [0, 0, 1, 1]

    # Initialize parameters
    num_features = len(X[0])
    theta, bias = initialize_parameters(num_features)

    # Hyperparameters
    learning_rate = 0.01
    num_iterations = 1000

    # Train the model
    theta, bias = gradient_descent(X, y, theta, bias, learning_rate, num_iterations)

    # Make predictions
    X_new = [[4, 5], [6, 7]]
    predictions = predict(X_new, theta, bias)

    print("Predictions:", predictions)

if __name__ == "__main__":
    main()


# sample output
# Iteration 0, Cost: -0.5000002331237219
# Iteration 100, Cost: -0.5692474598821775
# Iteration 200, Cost: -0.5853758556999756
# Iteration 300, Cost: -0.6004589665373755
# Iteration 400, Cost: -0.6146033052973388
# Iteration 500, Cost: -0.6278255932211684
# Iteration 600, Cost: -0.6401596341557405
# Iteration 700, Cost: -0.6516505496825139
# Iteration 800, Cost: -0.6623499536546487
# Iteration 900, Cost: -0.6723123706889057
# Predictions: [1, 1]