def main():
    name:str = input("Whats's your name? ")
    print(greet(name))

def greet(name):
    return "Greetings " + name + "!"

main()
