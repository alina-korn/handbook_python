number = input()  # Ввод как строки
hundreds = int(number[0])
tens = int(number[1])
units = int(number[2])

sum_lower = tens + units
sum_upper = hundreds + tens

encrypted_number = str(max(sum_upper, sum_lower)) + str(min(sum_upper, sum_lower))
print(encrypted_number)