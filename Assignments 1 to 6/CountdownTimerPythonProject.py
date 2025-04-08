import time

def countdown_timer():
    seconds = 0

    while True:
        try:
            user_input= int(input("Enter the countdown timer in seconds: "))
            if user_input <= 0:
                print("Please enter a positive integer.")
                continue
            seconds += user_input
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

    for i in range(seconds, 0, -1):
        print(f"Time left: {i} seconds", end='\r')
        time.sleep(1)
    print("\nTime's up!")

countdown_timer()

