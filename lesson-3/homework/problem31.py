# Get user input for the list of numbers and the number of repetitions
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
repeat_count = int(input("Enter the number of times to repeat each element: "))

# Create a new list with each element repeated the specified number of times
repeated_list = [num for num in numbers for _ in range(repeat_count)]

# Display the result
print(f"The new list with repeated elements is: {repeated_list}")
