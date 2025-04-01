# Get user input for the list of numbers and the size of each sublist
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
sublist_size = int(input("Enter the size of each sublist: "))

# Create a nested list with sublists containing the specified number of elements
nested_list = [numbers[i:i + sublist_size] for i in range(0, len(numbers), sublist_size)]

# Display the result
print(f"The nested list is: {nested_list}")
