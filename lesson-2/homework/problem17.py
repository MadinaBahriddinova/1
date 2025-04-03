# Ask the user for a string
user_string = input("Enter a string: ")

# Define vowels
vowels = "aeiouAEIOU"

# Replace vowels with a symbol (* in this case)
modified_string = "".join("*" if char in vowels else char for char in user_string)

# Print the result
print("String after replacing vowels:", modified_string)
