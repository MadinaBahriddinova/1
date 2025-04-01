# Get user input for the list and element to count
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
element = int(input("Enter the element to count: "))

# Count occurrences of the element
count = numbers.count(element)

# Display the result
print(f"The element {element} appears {count} times in the list.")
