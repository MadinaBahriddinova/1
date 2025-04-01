# Get user input for the list of numbers and the element to find
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
element = int(input("Enter the element to find all indices for: "))

# Find all indices of the element
indices = [i for i, num in enumerate(numbers) if num == element]

# Display the result
if indices:
    print(f"The indices of the element {element} are: {indices}")
else:
    print(f"The element {element} is not in the list.")
