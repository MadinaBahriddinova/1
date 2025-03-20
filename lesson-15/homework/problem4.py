import numpy as np
import matplotlib.pyplot as plt

# Generate 100 random points from a uniform distribution between 0 and 10
x_scatter = np.random.uniform(0, 10, 100)
y_scatter = np.random.uniform(0, 10, 100)

# Create the scatter plot
plt.figure(figsize=(7, 5))
plt.scatter(x_scatter, y_scatter, c=np.random.rand(100), marker='o', edgecolors='black')

# Add labels and title
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Scatter Plot of 100 Random Points')

# Add grid
plt.grid(True, linestyle='--', alpha=0.6)

# Add color bar to indicate the intensity of the color
plt.colorbar(label='Color Intensity')

# Show the plot
plt.show()
