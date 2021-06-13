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
    


# Main Routine goes here

# Introduction / Heading print statements
print()
print("**** Fence Cost Calculator *****")
print()

# Start of calculator loop
keep_going = ""
while keep_going == "":

    # call your number checker function three times to get the 
    # width, length and cost_per_m of the fencing
    width = num_check("Width: ")
    length = num_check("Length: ")
    cost_per_m = num_check("Cost per metre: $")
    print()

    # Calulate perimeter (width + height) x 2
    perimeter = 2 * (width + length)
    
    # Calculate the cost of the fencing (perimeter x price / meter)
    cost_of_fencing = (perimeter * cost_per_m)
    
    # Output the perimeter and cost of the fencing
    print("The perimeter is {:.2f} units" .format(perimeter))
    print("The cost of the fencing is ${:.2f} " .format(cost_of_fencing))
    print()
    
    keep_going = input("Press <enter> to keep going or any key to quit")

    print()
    print("-" * 30)    
    print()


print("Thanks for using the Fencing cost calculator")

        
    
    