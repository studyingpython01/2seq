import re
import string

amount = input('Введите числа через запятую:')
amount = re.split('[ ,:/]', amount)
print(amount)
