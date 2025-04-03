# Ask the user for a string and a character to remove
user_string = input("Enter a string: ")
char_to_remove = input("Enter a character to remove: ")

# Remove all occurrences of the character
modified_string = user_string.replace(char_to_remove, "")

# Print the result
print("String after removal:", modified_string)
