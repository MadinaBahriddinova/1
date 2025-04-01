# Get user input for the list of numbers and the index to remove
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
index = int(input("Enter the index of the element to remove: "))

# Remove the element at the specified index if it exists
if 0 <= index < len(numbers):
    removed_element = numbers.pop(index)
    print(f"Removed element: {removed_element}")
    print(f"The list after removal: {numbers}")
else:
    print("Invalid index. No element was removed.")
