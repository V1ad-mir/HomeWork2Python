# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.

import math
num = int(input('Введите число'))
i = 0;
while math.pow(2,i)<=num:
    print ( int(math.pow(2,i)))
    i=i+1