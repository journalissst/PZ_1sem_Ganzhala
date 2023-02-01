# Вариант 4
# в последовательности на n целых чисел умножить элементы до n-1 на элемент n
from random import randint
n = int(input("Введите длину последовательности: "))
nick = []
for i in range(n):
    nick.append(randint(0, 100))
nick_1 = [i*n for i in nick[:n-1]]
print(nick)
print(nick_1)
