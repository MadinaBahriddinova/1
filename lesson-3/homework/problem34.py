# Get user input for the list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Get the number of positions to rotate the list to the right
positions = int(input("Enter the number of positions to rotate the list: "))

# Rotate the list by shifting elements to the right
rotated_list = numbers[-positions:] + numbers[:-positions]

# Display the result
print(f"The rotated list is: {rotated_list}")
