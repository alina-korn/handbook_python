number = input()

# Проверяем, является ли число палиндромом
if number == number[::-1]:
    print("YES")
else:
    print("NO")