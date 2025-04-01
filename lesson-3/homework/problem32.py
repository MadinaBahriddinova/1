# Get user input for the two lists of numbers
list1 = list(map(int, input("Enter the first list of numbers separated by spaces: ").split()))
list2 = list(map(int, input("Enter the second list of numbers separated by spaces: ").split()))

# Merge the two lists and sort them
merged_sorted_list = sorted(list1 + list2)

# Display the result
print(f"The merged and sorted list is: {merged_sorted_list}")
