# Get user input for the list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Create a new list with the first three elements
first_three_elements = numbers[:3]

# Display the result
print(f"The first three elements of the list are: {first_three_elements}")
