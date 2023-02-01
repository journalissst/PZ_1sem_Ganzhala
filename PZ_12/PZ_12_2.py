# Вариант 4
# Составить генератор (yield), который выводит из строки только буквы

# Функция, которая принимает аргумент
def get_string(strin):
    yield [i for i in strin if i.isalpha()]

# Ввод данных от пользователя, а именно строки
st = input("Введите данные: ")
answer = get_string(st)
print(*list(answer))
