# Get user input for the list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Check if the list is empty
if numbers:
    # Access the first element
    first_element = numbers[0]
    print(f"The first element in the list is: {first_element}")
else:
    print("The list is empty, no first element.")
