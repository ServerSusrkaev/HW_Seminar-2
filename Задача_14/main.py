#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

number = int(input('Введите число: '))

for i in range(number):
    print(2 ** i, end=" ")