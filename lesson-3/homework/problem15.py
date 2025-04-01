# Get user input for the list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Count how many numbers are even
even_count = sum(1 for num in numbers if num % 2 == 0)

# Display the result
print(f"The number of even numbers in the list is: {even_count}")
