import numpy as np
import matplotlib.pyplot as plt

# Define x values for different functions
x1 = np.linspace(-2, 2, 400)  # For x^3
x2 = np.linspace(0, 2*np.pi, 400)  # For sin(x)
x3 = np.linspace(-2, 2, 400)  # For e^x
x4 = np.linspace(0, 5, 400)  # For log(x+1), ensuring x >= 0

# Compute function values
y1 = x1**3
y2 = np.sin(x2)
y3 = np.exp(x3)
y4 = np.log(x4 + 1)

# Create a figure with 2x2 subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Top-left: f(x) = x^3
axs[0, 0].plot(x1, y1, color='red')
axs[0, 0].set_title(r'$f(x) = x^3$')
axs[0, 0].set_xlabel('x')
axs[0, 0].set_ylabel('f(x)')
axs[0, 0].grid(True, linestyle='--', alpha=0.6)

# Top-right: f(x) = sin(x)
axs[0, 1].plot(x2, y2, color='blue')
axs[0, 1].set_title(r'$f(x) = \sin(x)$')
axs[0, 1].set_xlabel('x')
axs[0, 1].set_ylabel('f(x)')
axs[0, 1].grid(True, linestyle='--', alpha=0.6)

# Bottom-left: f(x) = e^x
axs[1, 0].plot(x3, y3, color='green')
axs[1, 0].set_title(r'$f(x) = e^x$')
axs[1, 0].set_xlabel('x')
axs[1, 0].set_ylabel('f(x)')
axs[1, 0].grid(True, linestyle='--', alpha=0.6)

# Bottom-right: f(x) = log(x+1)
axs[1, 1].plot(x4, y4, color='purple')
axs[1, 1].set_title(r'$f(x) = \log(x+1)$')
axs[1, 1].set_xlabel('x')
axs[1, 1].set_ylabel('f(x)')
axs[1, 1].grid(True, linestyle='--', alpha=0.6)

# Adjust layout for clarity
plt.tight_layout()
plt.show()
