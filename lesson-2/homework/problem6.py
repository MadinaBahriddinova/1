# Get user input for a number
num = int(input("Enter a number: "))

# Extract the last digit
last_digit = abs(num) % 10

# Display the result
print(f"The last digit of {num} is {last_digit}")
