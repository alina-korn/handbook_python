name = input()
question = input()

if question == "хорошо":
    answer = "Я за вас рада!"
elif question == "плохо":
    answer = "Всё наладится!"
else:
    answer = "Я не поняла ваш ответ."

print("Как Вас зовут?")
print(f"Здравствуйте, {name}!")
print("Как дела?")
print(answer)