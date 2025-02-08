a = float(input())
b = float(input())
c = float(input())

max_side = max(a, b, c)


if max_side ** 2 == a ** 2 + b ** 2 + c ** 2 - max_side ** 2:
    print("100%")
elif max_side ** 2 > a ** 2 + b ** 2 + c ** 2 - max_side ** 2:
    print("велика")
else:
    print("крайне мала")