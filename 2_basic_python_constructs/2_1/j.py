child_name = input()
locker_number = int(input())

group_number = locker_number // 100  
bed_number = (locker_number % 100) // 10 
child_number = locker_number % 10

print(f"Группа №{group_number}.")
print(f"{child_number}. {child_name}.")
print(f"Шкафчик: {locker_number}.")
print(f"Кроватка: {bed_number}.")