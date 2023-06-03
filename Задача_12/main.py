# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

import random

number_1 = random.randint(1, 1001)
number_2 = random.randint(1, 1001)

summa = number_1 + number_2
product = number_1 * number_2

print(f'Сумма = {summa}; Произведение = {product}')

divider = 2
dividerRes = 0
result_1 = 0
result_2 = 0
flag = True

while flag:
    if product % divider == 0:
        dividerRes = product // divider
        if (summa - dividerRes) * dividerRes == product:
            result_1 = product // divider
            flag = False
    divider += 1

result_2 = summa - result_1

print(f'Загаданы числа: {result_1} и {result_2}')