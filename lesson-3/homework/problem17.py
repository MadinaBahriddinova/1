# Get user input for the two lists
list1 = list(map(int, input("Enter the first list of numbers separated by spaces: ").split()))
list2 = list(map(int, input("Enter the second list of numbers separated by spaces: ").split()))

# Concatenate the two lists
combined_list = list1 + list2

# Display the result
print(f"The combined list is: {combined_list}")
