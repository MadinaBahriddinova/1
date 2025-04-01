# Get user input for the list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Check if the list is sorted in ascending order
is_sorted = numbers == sorted(numbers)

# Display the result
print(f"Is the list sorted in ascending order? {is_sorted}")
