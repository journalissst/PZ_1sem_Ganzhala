# Вариант 4
# Если в матрице имеются положительные элементы, то вывести TRUE, иначе FALSE.

# Импортирование библиотеки
import random


# Генерация квадратной матрицы
def generate_matrix():
    number = random.randint(1, 8)
    lst = [[random.randint(-50, 90) for _ in range(number)] for _ in range(number)]

    # Обозначение итерируемого объекта
    answer = iter(lst)

    # Вывод матрицы
    print("Вывод изначальной матрицы")
    flag = False
    while True:
        try:
            one = next(answer)
            for i in one:
                if i > 0:
                    flag = True
            print(*one)
        except StopIteration:
            print("Все! Итерации закончились. .\n")
            break
    print(f"В матрице имеются положительные элементы: {flag}")


# Вызов функции
generate_matrix()
