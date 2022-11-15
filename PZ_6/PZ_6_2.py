# Вариант 4
# Дан список размера N.
# Найти номер его последнего локального максимума
import random

n = int(input("Введите размер списка: "))


def chiselky(n):
    list_2 = [random.randint(1, 100) for i in range(n)]
    if list_2[-3] > list_2[-2] and list_2[-3] > list_2[-4]:
        print(f"Номер элемента: {len(list_2) - 3}")
    elif list_2[-2] > list_2[-1] and list_2[-2] > list_2[-3]:
        print(f"Номер элемента: {len(list_2) - 2}")
    else:
        print(f"Номер элемента: {len(list_2) - 1}")
    print(list_2)


chiselky(n)
