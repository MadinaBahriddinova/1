# Get user input for the list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Create a new list with the elements sorted
sorted_list = sorted(numbers)

# Display the result
print(f"The sorted list is: {sorted_list}")
