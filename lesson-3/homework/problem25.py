# Get user input for the list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Create a copy of the original list
copied_list = numbers.copy()

# Display the result
print(f"The copied list is: {copied_list}")
