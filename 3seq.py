import re
import string

amount = str(input('Введите числа через запятую:'))
amount = re.split('[ ,:/]', amount)


answer = str(input('Введите числа через запятую:'))
answer = re.split('[ ,:/]', answer)
for key in answer:
    if answer[+1] in amount:
        amount.remove(key)
print(amount)
