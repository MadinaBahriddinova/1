import numpy as np
import matplotlib.pyplot as plt

# Define x values from 0 to 2π
x = np.linspace(0, 2*np.pi, 400)

# Compute sine and cosine values
sin_x = np.sin(x)
cos_x = np.cos(x)

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(x, sin_x, linestyle='-', color='red', label=r'$\sin(x)$')
plt.plot(x, cos_x, linestyle='--', color='blue', label=r'$\cos(x)$')

# Add labels and title
plt.xlabel('x')
plt.ylabel('Value')
plt.title('Sine and Cosine Functions')

# Add grid and axes lines
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.6)

# Add a legend
plt.legend()

# Show the plot
plt.show()
