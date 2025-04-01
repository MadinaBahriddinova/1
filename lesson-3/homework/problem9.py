# Get user input for the list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Create a new list with the elements in reverse order
reversed_list = numbers[::-1]

# Display the result
print(f"The list in reverse order is: {reversed_list}")
