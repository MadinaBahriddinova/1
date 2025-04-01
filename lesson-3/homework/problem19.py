# Get user input for the list, the element to replace, and the new element
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
old_element = int(input("Enter the element to replace: "))
new_element = int(input("Enter the new element: "))

# Replace the first occurrence of the specified element
if old_element in numbers:
    numbers[numbers.index(old_element)] = new_element
    print(f"The list after replacing the element is: {numbers}")
else:
    print(f"The element {old_element} was not found in the list.")
