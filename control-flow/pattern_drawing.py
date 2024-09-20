# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks side by side for the current row
    for _ in range(size):
        print("*", end="")
    
    # Print a newline character after completing each row
    print()

    # Move to the next row
    row += 1

