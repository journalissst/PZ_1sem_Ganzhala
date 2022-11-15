# Вариант 4
# Дан список размера N.
# Переставить в обратном порядке элементы список, расположенные между его мин и макс элементами,
# включая мин и макс элементы.
import random
a = []
try:
    N = int(input('Введите размер списка: '))
    while N != 0:
        a.append(random.randint(0, 100))
        N -= 1
    a.sort(reverse=True)
    print(a)
except TypeError:
    print('Ошибка')
