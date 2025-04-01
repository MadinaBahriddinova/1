# Get user input for the list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Filter even numbers
even_numbers = [num for num in numbers if num % 2 == 0]

# Display the result
print(f"The even numbers in the list are: {even_numbers}")
