"""Calculate the factorial for the given positive number"""
def factorial(number):
    # If the number is 0 or 1 ... return 1
    if number <= 1:
        return 1
    # Vars for while loop and to store the calculation
    count = 1
    total = 1
    #Loop through to find the factorial
    while count <= number:
        total = total * count
        count += 1
    return total

if __name__ == '__main__':    
    # Display what the program is/does
    print ("\nCalculate the Factorial of a Non-Negative Integer")
    # Get the number the user wants the factorial of
    number = input('\nEnter a number: ')
    # Checks to make sure the number is not negative
    while number < 0:
        # Ask the user for another number
        print('\nPlease enter a positive integer ')
        number = input('Enter a number: ')
    else:
        # Call the function and display the answer
        total = factorial(number)
        print '\nThe Factorial of',number,'is',total


