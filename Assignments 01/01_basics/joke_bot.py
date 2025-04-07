prompt: str = "what do you want: "
joke: str = "I want eat or tell me something else"
sorry: str = "Sorry I only tell jokes."

def main():
    user_input = input(prompt).strip().lower()
    if "joke" in user_input:
        print(joke)
    else:
        print(sorry)
main()
