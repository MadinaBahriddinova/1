import numpy as np
import matplotlib.pyplot as plt

# Define x values from -10 to 10
x = np.linspace(-10, 10, 400)

# Define the function f(x) = x^2 - 4x + 4
y = x**2 - 4*x + 4

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(x, y, label=r'$f(x) = x^2 - 4x + 4$', color='blue')

# Add labels and title
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of $f(x) = x^2 - 4x + 4$')

# Add grid and axes lines
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.6)

# Add a legend
plt.legend()

# Show the plot
plt.show()
