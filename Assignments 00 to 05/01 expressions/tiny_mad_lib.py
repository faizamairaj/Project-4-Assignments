sentence_start: str = "Hello, Faiza! Welcome to Python programming." # noun verb adjective

def main():
    noun : str = input("Please type a noun: ")
    verb = input("Please type a verb: ")
    adjective = input("Please type an adjective: ")

    print(sentence_start + noun + " " + verb + " " + adjective + "!")

main()

