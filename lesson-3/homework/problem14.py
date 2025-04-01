# Get user input for the list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Check if the list is empty
is_empty = len(numbers) == 0

# Display the result
print(f"Is the list empty? {is_empty}")
