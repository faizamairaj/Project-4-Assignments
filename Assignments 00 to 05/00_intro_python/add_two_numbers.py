def main():
    try:
     num1 = (input("Enter first number: "))
     num1 = int(num1)
     num2 = (input("Enter second number: "))
     num2 = int(num2)
     total = num1 + num2
     print("The sum of the two numbers is: ", total ) 
    except ValueError:
     print("Please enter a valid number 😡")
    finally:
     print("End of program 😊")
main()
