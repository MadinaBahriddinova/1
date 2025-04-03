# Ask the user for a string
user_string = input("Enter a string: ")
start_word = input("Starts with: ")
end_word = input("Ends with: ")

# Check if the string starts and ends with the given words
starts = user_string.startswith(start_word)
ends = user_string.endswith(end_word)

# Print the results
if starts and ends:
    print("The string starts with", start_word, "and ends with", end_word)
elif starts:
    print("The string starts with", start_word, "but does not end with", end_word)
elif ends:
    print("The string does not start with", start_word, "but ends with", end_word)
else:
    print("The string neither starts with", start_word, "nor ends with", end_word)
