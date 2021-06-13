# Functions go here

# Checks input is a number more than zero
def num_check(question):
    valid = False
    while not valid:

        error = "Please enter a number that is more than zero"

        try:

            # Ask user to enter a number
            response = float(input(question))

            # Checks number is more than zero
            if response > 0:
                return response

            # Outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)
            print()

        
# Main routine goes here
width = num_check("Width: ")
height = num_check("Height: ")

# Calculate area (width x height)
area = width * height

# Calculate perimeter ()
perimeter = 2 * (width + height)

#Output area and perimeter
print("Area: {} square units" .format(area))
print("Perimeter: {} units" .format(perimeter))
print()