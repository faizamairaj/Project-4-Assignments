def read_phone_numbers():
    phonebook = {}
    while (name := input("Name: ")):
        phonebook[name] = input("Number: ")
    return phonebook


def print_phonebook(phonebook):
    for name, number in phonebook.items():
        print(f"{name} -> {number}")


def lookup_numbers(phonebook):
    while (name := input("Enter name to lookup: ")):
        print(phonebook.get(name, f"{name} is not in the phonebook"))


def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)

main()

