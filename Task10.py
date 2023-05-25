# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть


from random import randint

count_overturn1 = 0
count_overturn2 = 0
count_coins = int(input("Введите количество монет:"))
for i in range(count_coins):
    side_coins = randint(0,1)
    if side_coins>0:
        count_overturn1=count_overturn1+1
    else:
        count_overturn2=count_overturn2+1
if count_overturn1<=count_overturn2:
    print(f'Необходимо перевернуть {count_overturn1} монет')
else:
    print(f'Необходимо перевернуть {count_overturn2} монет')
