# Get user input for the list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Determine the length of the list
length = len(numbers)

# Display the result
print(f"The number of elements in the list is: {length}")
