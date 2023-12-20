import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calculate_statistics(data):
    # Mean
    mean_value = np.mean(data)

    # Median
    median_value = np.median(data)

    # Mode
    unique_elements, counts = np.unique(data, return_counts=True)
    mode_indices = np.where(counts == np.max(counts))
    mode_value = unique_elements[mode_indices][0]

    # Standard Deviation
    std_deviation = np.std(data)

    return mean_value, median_value, mode_value, std_deviation

def plot_data(data):
    plt.hist(data, bins=10, color='blue', edgecolor='black')
    plt.title('Histogram of Data')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()

def main():
    # Sample data (replace this with your dataset)
    data = np.array([23, 45, 67, 12, 89, 34, 56, 78, 23, 56, 12, 67])

    # Calculate statistics
    mean, median, mode, std_dev = calculate_statistics(data)

    # Print the results
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Standard Deviation: {std_dev}")

    # Plot the data
    plot_data(data)

if __name__ == "__main__":
    main()