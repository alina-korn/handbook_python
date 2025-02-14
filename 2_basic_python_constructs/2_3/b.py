counter = 0

while (string := input()) != "Приехали!":
    if "зайка" in string:
        counter += 1

print(counter)