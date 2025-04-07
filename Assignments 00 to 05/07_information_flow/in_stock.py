def main():
    fruit :str = (input("Enter the fruit name: "))
    stock = num_in_stock(fruit)
    if stock == 0:
        print("This fruit is not in stock.")
    else:
        print("This fruit is in stock! Here is how many:")
        print(stock)

def num_in_stock(fruit):
    if fruit == "apple":
        return 500
    if fruit == "banana":
        return 500
    if fruit == "orange":
        return 800
    if fruit == "grape":
        return 700
    if fruit == "kiwi":
        return 1000
    else:
        return 0
    
main()


    
