amount = []
answer = int(input('Введите количество чисел списка:'))
for i in range(0, answer, +1):
    answer = input('Введите число:')
    amount.append(answer)
amount.sort()
print(amount)