try:
    cost = float(input('Введите цену за 1 кг: '))
    a = 0
    while a < 0.9:
        a += 0.1
        print(f'Цена {round(a, 2)} кг - {cost*a} рублей')
except ValueError:
    print('Введите число!!!')
