# Get user input for the list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Find the minimum element
min_element = min(numbers)

# Display the result
print(f"The smallest element in the list is: {min_element}")