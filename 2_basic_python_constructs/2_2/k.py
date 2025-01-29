number = int(input())

digit1 = number // 100
digit2 = (number // 10) % 10
digit3 = number % 10

min_digit = min(digit1, digit2, digit3)
max_digit = max(digit1, digit2, digit3)

if digit1 != min_digit and digit1 != max_digit:
    remaining_digit = digit1
elif digit2 != min_digit and digit2 != max_digit:
    remaining_digit = digit2
else:
    remaining_digit = digit3

if (min_digit + max_digit) == (remaining_digit * 2):
    print("YES")
else:
    print("NO")