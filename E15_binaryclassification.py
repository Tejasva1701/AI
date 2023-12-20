# Write a program to implement a simple feedforward neural network for a basic task like binary classification

import random


def sigmoid(x):
    return 1 / (1 + pow(2.71828, -x))


def initialize_weights(input_size, hidden_size, output_size):
    hidden_weights = [
        [random.uniform(-1, 1) for _ in range(input_size)] for _ in range(hidden_size)
    ]
    output_weights = [random.uniform(-1, 1) for _ in range(hidden_size)]
    hidden_biases = [random.uniform(-1, 1) for _ in range(hidden_size)]
    output_bias = random.uniform(-1, 1)
    return hidden_weights, output_weights, hidden_biases, output_bias


def forward_pass(inputs, hidden_weights, output_weights, hidden_biases, output_bias):
    # Hidden layer
    hidden_layer = [
        sum(w * x for w, x in zip(hidden_weights[i], inputs)) + b
        for i, b in enumerate(hidden_biases)
    ]
    hidden_activations = [sigmoid(x) for x in hidden_layer]

    # Output layer
    output = (
        sum(w * a for w, a in zip(output_weights, hidden_activations)) + output_bias
    )
    output_activation = sigmoid(output)

    return hidden_activations, output_activation


def backpropagation(
    inputs,
    target,
    hidden_activations,
    output_activation,
    hidden_weights,
    output_weights,
    hidden_biases,
    output_bias,
    learning_rate=0.1,
):
    # Compute output layer error
    output_error = (
        output_activation * (1 - output_activation) *
        (target - output_activation)
    )

    # Update output layer weights and bias
    output_weights = [
        weight + learning_rate * output_error * hidden_activation
        for weight, hidden_activation in zip(output_weights, hidden_activations)
    ]
    output_bias += learning_rate * output_error

    # Compute hidden layer errors
    hidden_errors = [
        output_error * output_weights[i] *
        hidden_activation * (1 - hidden_activation)
        for i, hidden_activation in enumerate(hidden_activations)
    ]

    # Update hidden layer weights and biases
    for i in range(len(hidden_weights)):
        hidden_weights[i] = [
            weight + learning_rate * hidden_errors[i] * inputs[j]
            for j, weight in enumerate(hidden_weights[i])
        ]
        hidden_biases[i] += learning_rate * hidden_errors[i]

    return hidden_weights, output_weights, hidden_biases, output_bias


def train_neural_network(
    data, labels, input_size, hidden_size, output_size, epochs=1000, learning_rate=0.1
):
    hidden_weights, output_weights, hidden_biases, output_bias = initialize_weights(
        input_size, hidden_size, output_size
    )

    for epoch in range(epochs):
        total_loss = 0
        for inputs, target in zip(data, labels):
            hidden_activations, output_activation = forward_pass(
                inputs, hidden_weights, output_weights, hidden_biases, output_bias
            )
            (
                hidden_weights,
                output_weights,
                hidden_biases,
                output_bias,
            ) = backpropagation(
                inputs,
                target,
                hidden_activations,
                output_activation,
                hidden_weights,
                output_weights,
                hidden_biases,
                output_bias,
                learning_rate,
            )
            total_loss += 0.5 * (target - output_activation) ** 2

        if epoch % 100 == 0:
            print(f"Epoch {epoch}, Loss: {total_loss}")

    return hidden_weights, output_weights, hidden_biases, output_bias


def predict_neural_network(
    inputs, hidden_weights, output_weights, hidden_biases, output_bias
):
    _, output_activation = forward_pass(
        inputs, hidden_weights, output_weights, hidden_biases, output_bias
    )
    return round(output_activation)


# Example usage:
data = [[0, 0], [0, 1], [1, 0], [1, 1]]

labels = [0, 1, 1, 0]

input_size = len(data[0])
hidden_size = 2
output_size = 1

trained_weights = train_neural_network(
    data, labels, input_size, hidden_size, output_size, epochs=1000, learning_rate=0.1
)

# Test the trained neural network
for example in data:
    prediction = predict_neural_network(example, *trained_weights)
    print(f"Input: {example}, Prediction: {prediction}")

# Sample output:
# Epoch 0, Loss: 0.5174493738243546
# Epoch 100, Loss: 0.5066162783105652
# Epoch 200, Loss: 0.5064793779306904
# Epoch 300, Loss: 0.5063653216893514
# Epoch 400, Loss: 0.5062656289659638
# Epoch 500, Loss: 0.5061758964004299
# Epoch 600, Loss: 0.5060926789879405
# Epoch 700, Loss: 0.5060131230647507
# Epoch 800, Loss: 0.5059347223448316
# Epoch 900, Loss: 0.5058551386705035
# Input: [0, 0], Prediction: 1
# Input: [0, 1], Prediction: 0
# Input: [1, 0], Prediction: 1
# Input: [1, 1], Prediction: 0
