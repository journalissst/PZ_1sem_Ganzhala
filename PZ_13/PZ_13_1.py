# Вариант 4
# В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в 2 раза.

# Импортирование библиотеки
import random


# Генерация квадратной матрицы
def generate_matrix():
    number = random.randint(1, 8)
    lst = [[random.randint(1, 9) for _ in range(number)] for _ in range(number)]

    # Обозначение итерируемого объекта
    answer = iter(lst)

    # Вывод матрицы
    print("Вывод изначальной матрицы")
    while True:
        try:
            one = next(answer)
            print(*one)
        except StopIteration:
            print("Все! Итерации закончились. .\n")
            break

    print("Вывод изменений матрицы:")
    answer_two = iter(lst)
    chet = 0  # Счетчик
    while True:
        try:
            two = next(answer_two)
            for k in range(number):
                if k != chet:
                    two[k] *= 2
            print(*two)
            chet += 1
        except StopIteration:
            print("Конец.")
            break


# Вызов функции
generate_matrix()
