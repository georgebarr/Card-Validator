card_number = input("Enter a card number: ")

card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")

reversed_card_num = card_number[::-1]

sum_odd_nums = 0
sum_even_nums = 0


for i in reversed_card_num[::2]:
    sum_odd_nums += int(i)

for i in reversed_card_num[1::2]:
    i = int(i) * 2

    if i >= 10:
        sum_even_nums += 1 + (i % 10)
    else:
        sum_even_nums += i

if (sum_odd_nums + sum_even_nums) % 10 == 0:
    print(f"CARD {card_number} VALID.")
else:
    print(f"CARD {card_number} INVALID.")