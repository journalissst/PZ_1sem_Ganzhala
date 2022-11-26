# Вариант 4
# Дано целое число (1 < N < 26)
# Вывести N первых прописных (то есть заглавных) букв латинского алфавита
import random

list_2 = []
list_1 = ['A ', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']
number = random.randint(1, 26)
for i in range(0, number+1):
    list_2.append(list_1[i])
print(list_2)
