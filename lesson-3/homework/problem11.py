# Get user input for the list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Create a new list with unique elements using a set
unique_elements = list(set(numbers))

# Display the result
print(f"The list with unique elements is: {unique_elements}")
