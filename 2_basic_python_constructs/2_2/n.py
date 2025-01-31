number = input().strip()

digits = list(number)

two_digit_numbers = []
for i in range(3):
    for j in range(3):
        if i != j and digits[i] != '0':
            two_digit_numbers.append(int(digits[i] + digits[j]))


min_number = min(two_digit_numbers)
max_number = max(two_digit_numbers)

print(min_number, max_number)
