# Get user input for three numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Find the largest and smallest numbers
largest = max(num1, num2, num3)
smallest = min(num1, num2, num3)

# Display the results
print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")
