import math  # Import the math library so we can use the sqrt function

def main():
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))

    # Calculate the hypotenuse using the two sides and print it out
    c = math.sqrt(a**2 + b**2)
    print("The length of the hypotenuse is", c)
  
main()
