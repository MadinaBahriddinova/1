# Ask the user for a sentence
sentence = input("Enter a sentence: ")

# Generate an acronym by taking the first letter of each word and converting to uppercase
acronym = "".join(word[0].upper() for word in sentence.split())

# Print the acronym
print("Acronym:", acronym)
