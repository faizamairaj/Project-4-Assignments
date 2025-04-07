def count_even():
    lst = []
    
    while True:
        num = input("Enter an integer or press enter to stop: ")
        if num == "": 
            break
        lst.append(int(num))  

    even_count = sum(1 for x in lst if x % 2 == 0) 
    print("Number of even numbers:", even_count)

count_even()

