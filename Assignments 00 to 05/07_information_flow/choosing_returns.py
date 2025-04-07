adult_age: int = 18

def is_adult(age:int):
    if age >= adult_age:
        return True
    else:
        return False

def main():
    age: str = int(input("How old is this person ?"))
    print(is_adult(age))

main()