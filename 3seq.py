import re
import string

amount = str(input('Введите числа через запятую:'))
amount = re.split('[ ,:/]', amount)


answer = str(input('Введите числа через запятую:'))
answer = re.split('[ ,:/]', answer)
for element in amount[:]:
    if element in answer:
        amount.remove(element)
print(amount)
