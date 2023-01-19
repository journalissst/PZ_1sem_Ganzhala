# Второе создание
digit = 0
for i in open("text18-4.txt", "r", encoding="UTF-8"):  # Чтение содержимого
    print(i, end='')
    for j in i:
        if j.isalpha():
            digit += 1
print(f"\nКоличество символов (букв): {digit}")


# Создание второго файла
f1 = open("file_3.txt", "w", encoding="UTF-8")
for i in open("text18-4.txt", "r", encoding="UTF-8"):
    f1.write(i.lower())
f1.close()
