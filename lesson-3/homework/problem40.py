# Get user input for the list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Create a list with unique elements while maintaining order
unique_elements = []
for num in numbers:
    if num not in unique_elements:
        unique_elements.append(num)

# Display the result
print(f"The list with unique elements in order is: {unique_elements}")
