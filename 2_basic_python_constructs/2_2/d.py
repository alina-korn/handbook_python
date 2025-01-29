petya = int(input())  # Считываем скорость Пети
vasya = int(input())  # Считываем скорость Васи
tolya = int(input())  # Считываем скорость Толи

# Создаем список из кортежей (имя, скорость)
racers = [("Петя", petya), ("Вася", vasya), ("Толя", tolya)]

# Сортируем список по скорости в порядке убывания (по второму элементу в кортежах)
racers_sorted = sorted(racers, key=lambda x: x[1], reverse=True)

# Выводим результаты вручную, так как мы уже отсортировали список
print(f"1. {racers_sorted[0][0]}")
print(f"2. {racers_sorted[1][0]}")
print(f"3. {racers_sorted[2][0]}")