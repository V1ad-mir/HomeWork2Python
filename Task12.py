# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

# sum = num_first + num_second
# multiplication = num_first * num_second
# num_second = sum - num_first
# multiplication = num_first* (sum - num_first) => multiplication = num_first*sum - num_first*num_first =>
# -num_first*num_first+num_first*sum+multiplication=0
# num_first *  num_first - num_first * sum - multiplication=0


import math

sum = int(input('Введите сумму задуманых чисех:'))
multiplication = int(input('Введите произведение задуманых чисех:'))

discriminant = math.pow((sum),2) -(4 * 1 * multiplication)

if discriminant>=0:
   num_first = (sum + math.sqrt(discriminant))/2
   if num_first%1==0:
      num_second = sum - num_first
      print (f'Задуманные числа {int(num_first), int(num_second)}')
   else:
      print('Нет решения с натуральными числами, проверте исходные данные')
else:
    print('Нет решения проверте исходные данные')


