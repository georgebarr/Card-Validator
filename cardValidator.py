card_number = input("Enter a card number: ")

card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")

sum_odd_nums = 0
sum_even_nums = 0


def check_validity(card_num):

    card_num = card_num[::-1]

    for num in card_num[::2]:
        global sum_odd_nums
        sum_odd_nums += int(num)

    for i in card_num[1::2]:
        i = int(i) * 2

        if i >= 10:
            global sum_even_nums
            sum_even_nums += (1 + (i % 10))
        else:
            sum_even_nums += i

    if (sum_odd_nums + sum_even_nums) % 10 == 0:
        return True
    else:
        return False


if check_validity(card_number):
    print(f"{card_number} VALID.")
else:
    print(f"{card_number} INVALID.")
