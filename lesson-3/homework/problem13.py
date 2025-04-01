# Get user input for the list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Get user input for the element to find
element = int(input("Enter the element to find the index of: "))

# Find the index of the first occurrence of the element
if element in numbers:
    index = numbers.index(element)
    print(f"The index of the first occurrence of {element} is: {index}")
else:
    print(f"The element {element} is not in the list.")
