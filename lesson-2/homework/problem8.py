# Ask the user for a string
user_input = input("Enter a string: ")

# Check if the string is not empty
if user_input:
    first_char = user_input[0]
    last_char = user_input[-1]
    print(f"First character: {first_char}")
    print(f"Last character: {last_char}")
else:
    print("You entered an empty string!")
