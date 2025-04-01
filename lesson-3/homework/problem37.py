# Get user input for the list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Calculate the sum of negative numbers
negative_sum = sum(num for num in numbers if num < 0)

# Display the result
print(f"The sum of negative numbers is: {negative_sum}")
