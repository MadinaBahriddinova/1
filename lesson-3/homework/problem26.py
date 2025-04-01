# Get user input for the list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Find the middle element(s)
length = len(numbers)
if length % 2 == 1:
    middle_element = numbers[length // 2]
    print(f"The middle element is: {middle_element}")
else:
    middle_elements = numbers[(length // 2) - 1: (length // 2) + 1]
    print(f"The two middle elements are: {middle_elements}")
