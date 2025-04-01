# Get user input for the list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Get user input for the element to insert and the index
element = int(input("Enter the element to insert: "))
index = int(input("Enter the index to insert the element at: "))

# Insert the element at the specified index
numbers.insert(index, element)

# Display the result
print(f"The list after inserting the element is: {numbers}")
