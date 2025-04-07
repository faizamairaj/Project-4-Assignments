minimum_height: int = 50

def main():
    height = float(input("How tall are you? "))
    if height >= minimum_height:
        print("You are tall enough to ride.")
    else:
        print("You are not tall enough to ride.")

main()
