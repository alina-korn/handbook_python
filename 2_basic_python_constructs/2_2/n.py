n = input().strip()

digits = list(n)

two_digit_numbers = {int(d1 + d2) for i, d1 in enumerate(digits) for j, d2 in enumerate(digits) if i != j}

print(min(two_digit_numbers), max(two_digit_numbers))