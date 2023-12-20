import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate some random data for demonstration purposes
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Create a DataFrame using pandas
data = pd.DataFrame({'X': X.flatten(), 'y': y.flatten()})

# Split the data into training and testing sets
train_data = data.sample(frac=0.8, random_state=42)
test_data = data.drop(train_data.index)

# Calculate the coefficients using the normal equation
X_train = train_data[['X']].values
y_train = train_data['y'].values
X_train = np.c_[np.ones((X_train.shape[0], 1)), X_train]  # Add a bias term
theta = np.linalg.inv(X_train.T.dot(X_train)).dot(X_train.T).dot(y_train)

# Make predictions on the test data
X_test = test_data[['X']].values
X_test = np.c_[np.ones((X_test.shape[0], 1)), X_test]  # Add a bias term
y_pred = X_test.dot(theta)

# Calculate the mean squared error
mse = ((y_pred - test_data['y'].values) ** 2).mean()

# Print the model coefficients and evaluation metrics
print("Coefficients:", theta)
print("Mean Squared Error:", mse)

# Plot the data and the regression line
plt.scatter(data['X'], data['y'], s=20, label="Data")
plt.plot(test_data['X'], y_pred, color='red', linewidth=2, label="Linear Regression")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()