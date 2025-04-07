def get_user_numbers():
    nums = []
    while (num := input("Enter a number: ")):
        nums.append(int(num))
    return nums


def count_nums(nums):
    num_dict = {}
    for num in nums:
        num_dict[num] = num_dict.get(num, 0) + 1
    return num_dict


def main():
    num_dict = count_nums(get_user_numbers())
    for num, count in num_dict.items():
        print(f"{num} appears {count} times.")

main()

