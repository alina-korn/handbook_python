start = int(input())
finish = int(input())

step = 1 if start <= finish else -1

for number in range(start, finish + step, step):
    print(number, end=" ")