# Вариант 4
# Создайте класс "Животное", который содержит информацию о виде и возрасте
# животного. Создайте классы "Собака" и "Кошка", которые наследуются от класса
# "Животное" и содержат информацию о породе.


class Animals:
    def __init__(self, vid, age):
        self.vid = vid
        self.age = age


class Dog(Animals):
    def __init__(self, vid, age, poroda):
        super().__init__(vid, age)
        self.poroda = poroda

    def print(self):
        return f"Вид животного: {self.vid}\nВозраст: {self.age}\nПорода животного: {self.poroda}"


class Cat(Animals):
    def __init__(self, vid, age, poroda):
        super().__init__(vid, age)
        self.poroda = poroda

    def print(self):
        return f"Вид животного: {self.vid}\nВозраст: {self.age}\nПорода животного: {self.poroda}"


animal_one = Dog("Собака", 7, "Немецкая овчарка")
print(animal_one.print())

print()

animal_two = Cat("Кошка", 12, 'Сиамская')
print(animal_two.print())
