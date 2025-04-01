# Get user input for the list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Find the second smallest element
unique_numbers = list(set(numbers))  # Remove duplicates
unique_numbers.sort()  # Sort the list
if len(unique_numbers) > 1:
    second_smallest = unique_numbers[1]  # The second element
    print(f"The second smallest element is: {second_smallest}")
else:
    print("There is no second smallest element.")
