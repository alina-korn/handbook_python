petya_speed = int(input())
vasya_speed = int(input())
tolya_speed = int(input())

participants = [("Петя", petya_speed), ("Вася", vasya_speed), ("Толя", tolya_speed)]

sorted_participants = sorted(participants, key=lambda x: x[1], reverse=True)

first = sorted_participants[0][0]
second = sorted_participants[1][0]
third = sorted_participants[2][0]

print(f"          {first}          ")
print(f"  {second}  ")
print(f"                  {third}  ")
print("   II      I      III   ")