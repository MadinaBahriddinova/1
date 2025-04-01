# Get user input for the main list and sublist
main_list = list(map(int, input("Enter the main list of numbers separated by spaces: ").split()))
sublist = list(map(int, input("Enter the sublist of numbers separated by spaces: ").split()))

# Check if the sublist exists within the main list
if any(main_list[i:i+len(sublist)] == sublist for i in range(len(main_list) - len(sublist) + 1)):
    print("The sublist exists within the main list.")
else:
    print("The sublist does not exist within the main list.")
