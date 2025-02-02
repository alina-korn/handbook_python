num1 = input().strip()
num2 = input().strip()


digits = list(num1) + list(num2)
digits = [int(d) for d in digits] 

max_digit = max(digits)
min_digit = min(digits)

digits.remove(max_digit)
digits.remove(min_digit)

middle_digit = sum(digits) % 10

magic_number = int(f"{max_digit}{middle_digit}{min_digit}")

print(magic_number)