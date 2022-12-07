# Вариант 4
# Дан словарь с четным количеством элементов.
# Найти суммы значений элементов первой и второй половин с использованием функции. Результаты вывести на экран.
import random

slovar = {}
while True:
    a = random.randint(1, 50)
    if a % 2 == 0:
        break
for i in range(a):
    slovar[i] = i
print(f"Сам словарь: {slovar}")
print(f"Случайное сгенерированное четное число: {a}")


def summ_slovar(a):
    sum_1 = 0
    sum_2 = 0
    for i in range(a // 2):
        sum_1 += slovar[i]

    for i in range(a // 2, a):
        sum_2 += slovar[i]
    return f"Сумма первых элементов: {sum_1}\nСумма вторых элементов: {sum_2}"


print(summ_slovar(a))


