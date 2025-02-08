a = float(input())
b = float(input())
c = float(input())

# Обработка разных случаев
if a == 0 and b == 0:
    if c == 0:
        print("Infinite solutions")
    else:
        print("No solution")
elif a == 0:
    # Линейное уравнение bx + c = 0
    x = -c / b
    print(f"{x:.2f}")
else:
    # Квадратное уравнение ax^2 + bx + c = 0
    D = b**2 - 4 * a * c
    if D < 0:
        print("No solution")
    elif D == 0:
        x = -b / (2 * a)
        print(f"{x:.2f}")
    else:
        # Два корня
        x1 = (-b + D**0.5) / (2 * a)
        x2 = (-b - D**0.5) / (2 * a)
        # Выводим корни в порядке возрастания
        x1, x2 = sorted([x1, x2])
        print(f"{x1:.2f} {x2:.2f}")