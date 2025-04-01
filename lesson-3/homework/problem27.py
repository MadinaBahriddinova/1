# Get user input for the list of numbers and the sublist indices
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
start = int(input("Enter the starting index of the sublist: "))
end = int(input("Enter the ending index of the sublist: "))

# Extract the sublist and find the maximum element
sublist = numbers[start:end+1]
max_element = max(sublist)

# Display the result
print(f"The maximum element in the sublist is: {max_element}")
