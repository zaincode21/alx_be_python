def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

# Main program
try:
    user_input = int(input("Enter a number: "))  # Ask the user for input
    check_even_odd(user_input)  # Call the function with user input
except ValueError:
    print("Please enter a valid integer.")
