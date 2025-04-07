import random

numbers: int = 10
min_value: int = 1
max_value: int = 100

def main():
    random_numbers: list[int] = [random.randint(min_value, max_value) for _ in range(numbers)]
    print(f"Random numbers: {random_numbers}")
    print(f"Sum of random numbers: {sum(random_numbers)}")

main()


