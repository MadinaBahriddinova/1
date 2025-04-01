# Get user input in kilometers
kilometers = float(input("Enter distance in kilometers: "))

# Convert to meters and centimeters
meters = kilometers * 1000
centimeters = kilometers * 100000

# Display the results
print(f"{kilometers} km is equal to {meters} meters and {centimeters} centimeters.")
