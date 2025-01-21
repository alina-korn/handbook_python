N = int(input())  # Часы
M = int(input())  # Минуты
T = int(input())  # Минуты доставки

total_minutes = N * 60 + M

total_minutes += T

new_hours = (total_minutes // 60) % 24 
new_minutes = total_minutes % 60 

print(f"{new_hours:02}:{new_minutes:02}")