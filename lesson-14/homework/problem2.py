import numpy as np

# Task 2: Compute power of numbers
def power_function(base, exp):
    return base ** exp

vectorized_power = np.vectorize(power_function)
bases = np.array([2, 3, 4, 5])
exponents = np.array([1, 2, 3, 4])
powers = vectorized_power(bases, exponents)

print("Powers:", powers)