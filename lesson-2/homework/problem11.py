# Ask the user for a string
user_input = input("Enter a string: ")

# Check if any character is a digit
contains_digit = any(char.isdigit() for char in user_input)

# Print the result
if contains_digit:
    print("The string contains at least one digit.")
else:
    print("The string does not contain any digits.")
