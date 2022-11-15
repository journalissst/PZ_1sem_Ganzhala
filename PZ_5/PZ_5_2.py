# вариант 4
# Описать функцию RectPS(x1,y1,x2,y2,P,S), вычисляющую периметр Р и площадь S прямоугольника со сторонами,
# параллельными осям координат, по координатам (x1,y1), (x2,y2) его противоположных вершин (x1, y1, x2, y2 - входные,
# P и S - выходные параметры вещественного типа). С помощью этой функции найти периметры и площади трех
# прямоугольников с данными противоположными вершинами.
def RectPS(x1, y1, x2, y2, P=None, S=None):
    x = abs(x1 - x2)
    y = abs(y1 - y2)
    print(f'x -> {x}')
    print(f'y -> {y}')
    P = 2 * (x + y)
    S = x * y
    print(f"Периметр равен: {P}")
    print(f"Площадь равна: {S}")

try:
    x_1 = int(input('Введите число для x1 координаты: '))
    x_2 = int(input('Введите число для x2 координаты: '))
    y_1 = int(input('Введите число для y1 координаты: '))
    y_2 = int(input('Введите число для y2 координаты: '))
except ValueError:
    print('Ошибка')
else:
    RectPS(x_1, y_1, x_2, y_2)