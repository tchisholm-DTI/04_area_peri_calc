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

# Introduction?Heading prin statements
print()
print("**** Area Perimeter Calculator ****")
print()

# Start of calculator loop
keep_going = ""
while keep_going == "":

    width = num_check("Width: ")
    height = num_check("Height: ")

    # Calculate area (width x height)
    area = width * height

    # Calculate perimeter ()
    perimeter = 2 * (width + height)

    #Output area and perimeter to 2dp
    print("Area: {:.2f} square units" .format(area))
    print("Perimeter: {:.2f} units" .format(perimeter))
    print()

    keep_going = input("Press <enter> to keep going or any key to quit")

print()
print("Thanks for using the area/perimeter calculator")