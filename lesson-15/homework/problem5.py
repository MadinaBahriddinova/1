import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 random values from a normal distribution (mean=0, std=1)
data = np.random.normal(loc=0, scale=1, size=1000)

# Create the histogram
plt.figure(figsize=(7, 5))
plt.hist(data, bins=30, color='blue', alpha=0.7, edgecolor='black')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Normally Distributed Data')

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Show the plot
plt.show()
