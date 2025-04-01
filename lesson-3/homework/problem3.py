# Get user input for the list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Find the maximum element
max_element = max(numbers)

# Display the result
print(f"The largest element in the list is: {max_element}")