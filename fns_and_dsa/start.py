def calculate_area(length, width):
    """Calculates the area of a rectangle."""
    area = length * width
    return area

# Get user input outside the function
length = int(input("Enter a Length: "))
width = int(input("Enter a Width: "))

# Call the function with the user's inputs
rectangle_area = calculate_area(length, width)

# Print the result
print(f"The area of the rectangle is {rectangle_area}")

