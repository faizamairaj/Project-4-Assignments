def shorten(lst, max_length = 3):
    while len(lst) > max_length:
        print(lst.pop())

def get_lst():
    lst = []
    while (element:= input("Enter element (or press enter to stop): ")):
        lst.append(element)
    return lst

shorten(get_lst())
       

