# Get user input for the list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Check if the list is empty
if numbers:
    # Access the last element
    last_element = numbers[-1]
    print(f"The last element in the list is: {last_element}")
else:
    print("The list is empty, no last element.")
