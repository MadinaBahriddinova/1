# Get user input for the list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Calculate the sum of elements
total = sum(numbers)

# Display the result
print(f"The sum of all elements is: {total}")