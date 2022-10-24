import re
import string

amount = input('Введите числа через запятую:')
var = (amount == re.split('string', '[ , : / ]'), amount)
amount = set(amount)
amount.remove(',')

answer = input('Введите числа через запятую:')
var = (answer == re.split('string', '[ , : / ]'), answer)
answer = set(answer)
answer.remove(',')
print(amount-answer)