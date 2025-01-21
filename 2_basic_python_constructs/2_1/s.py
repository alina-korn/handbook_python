a = input()  # Название товара
b = int(input())  # Цена товара за кг
c = int(input())  # Вес товара
d = int(input())  # Сумма, которую внес покупатель

# Формирование чека с выравниванием
line_len = 35

# Заголовок
print(f'{"================Чек================":^35}')

# Товар
print(f"Товар: {a.rjust(line_len - len('Товар: '))}")

# Цена
price_str = f"{c}кг * {b}руб/кг"
print(f"Цена: {price_str.rjust(line_len - len('Цена: '))}")

# Итого
total_str = f"{b * c}руб"
print(f"Итого: {total_str.rjust(line_len - len('Итого: '))}")

# Внесено
payment_str = f"{d}руб"
print(f"Внесено: {payment_str.rjust(line_len - len('Внесено: '))}")

# Сдача
change_str = f"{d - b * c}руб"
print(f"Сдача: {change_str.rjust(line_len - len('Сдача: '))}")

# Нижняя линия
print("=" * line_len)