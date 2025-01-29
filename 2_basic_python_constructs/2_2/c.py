petya = int(input())
vasya = int(input())
tolya = int(input())

winner = max(petya, vasya, tolya)

if winner == petya:
    print("Петя")
elif winner == vasya:
    print("Вася")
elif winner == tolya:
    print("Толя")
else:
    print("Ошибка")