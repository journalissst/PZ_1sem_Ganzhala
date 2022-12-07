# Вариант 4
# Дана строка-предложение.
# Зашифровать ее, поместив вначале все символы, расположенные на четных позициях строки, а затем, в обратном порядке,
# все символы, расположенные на нечетных позициях
stringg = input("Введите строку: ")
answer_string = ''
for i in range(0, len(stringg)):
    if i % 2 != 0:
        answer_string += stringg[i]
b = len(stringg)
while b >= 0:
    if b % 2 == 0:
        answer_string += stringg[b]
    b -= 1

print(answer_string)
