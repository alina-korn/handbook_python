a = int(input())
b = int(input())
c = int(input())

# Проверка условия возможности построения треугольника
if (a + b > c) and (a + c > b) and (b + c > a):
    print("YES")
else:
    print("NO")