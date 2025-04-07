voting_ages = {
 "Peturksbouipo": 16,
 "Stanlau": 25,
 "Mayengua": 48
}

def main():
    user_age = int(input("How old are you?"))

    for country, age in voting_ages.items():
        if user_age >= age:
            print(f"You can vote in {country} where the voting age is {age}.")
        else:
            print(f"cannot vote in {country} where the voting age is {age}.")

main()

