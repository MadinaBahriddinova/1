# Get user input for the list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Check if the list is a palindrome
is_palindrome = numbers == numbers[::-1]

# Display the result
print(f"Is the list a palindrome? {is_palindrome}")
