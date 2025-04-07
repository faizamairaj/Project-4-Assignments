def main():
    fruits = {'apple': 1, 'banana': 2, 'cherry': 3, 'date': 4, 'elderberry': 5}

    total_cost = 0
    for fruit_name in fruits:
        price = fruits[fruit_name]
        amount =  int(input("How many (" + fruit_name + ") do you want to buy?: "))
        total_cost += price * amount
   
    print("The total cost is: " + str(total_cost))

main()
