# Программ проверяет истинность высказывания A > 2 u B < 3
try:  # Обработчик исключений
    a = int(input('Введите целое число А: '))
    b = int(input('Введите целое число B: '))
    if (a > 2) and (b < 3):  # Проверка условий A > 2 u B < 3
        print('Истина')
    else:
        print('Ложь')
except ValueError:
    print('Введен неверный тип данных!')
