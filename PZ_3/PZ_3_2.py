# Программ определяет цвет по введенной длине волны
try:  # Обработчик исключений
    a = int(input('Введите определенную длину волны: '))
    # Условия для проверки вхождения числа в диапазон
    if a <= 450:
        print('Фиолетовый')
    elif 450 < a <= 480:
        print('Синий')
    elif 480 < a <= 510:
        print('Сине-зеленый')
    elif 510 < a <= 550:
        print('Зеленый')
    elif 550 < a <= 570:
        print('Желто-зеленый')
    elif 570 < a <= 590:
        print('Желтый')
    elif 590 < a <= 630:
        print('Оранжевый')
    else:
        print('Красный')
except ValueError:
    print('Введен неверный тип данных!')