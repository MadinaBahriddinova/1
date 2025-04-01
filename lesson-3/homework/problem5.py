# Get user input for the list and element
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
element = int(input("Enter the element to check: "))

# Check if the element is in the list
if element in numbers:
    print(f"The element {element} is present in the list.")
else:
    print(f"The element {element} is not present in the list.")
