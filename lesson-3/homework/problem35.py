# Get user input for the start and end of the range
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Create a list of numbers in the specified range
range_list = list(range(start, end + 1))

# Display the result
print(f"The list of numbers in the range is: {range_list}")
