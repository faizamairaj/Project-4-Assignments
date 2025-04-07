def main():
    # Get the two numbers
    num1 = int(input('Enter an integer: '))
    num2 = int(input('Enter another integer: '))

    # Calculate the remainder & quotient
    quotient = num1 // num2
    remainder = num1 % num2

    # Display the result
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))

# Call the main function
main()


