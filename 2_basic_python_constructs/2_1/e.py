price = int (input())
weight = int (input())
money = int (input())

# Рассчитываем сдачу
change = money - (price * weight)

# Выводим результат
print(int(change))