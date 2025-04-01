# Get user input for the list of numbers and the sublist indices
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
start = int(input("Enter the starting index of the sublist: "))
end = int(input("Enter the ending index of the sublist: "))

# Extract the sublist and find the minimum element
sublist = numbers[start:end+1]
min_element = min(sublist)

# Display the result
print(f"The minimum element in the sublist is: {min_element}")
