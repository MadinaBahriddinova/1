# Get user input for the list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Find the second largest element
unique_numbers = list(set(numbers))  # Remove duplicates
unique_numbers.sort()  # Sort the list
if len(unique_numbers) > 1:
    second_largest = unique_numbers[-2]  # The second last element
    print(f"The second largest element is: {second_largest}")
else:
    print("There is no second largest element.")
