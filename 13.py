from math import sqrt

class Shape:
    def __init__(self, x, y, fill_color='black'):
        self.x = x
        self.y = y
        self.fill_color = 1
    def square(self):
        raise NotImplementedError("Этот метод должен быть реализован в подклассах.")

    def perimeter(self):
        raise NotImplementedError("Этот метод должен быть реализован в подклассах.")

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

    def fill(self, color):
        self.fill_color = color

    @staticmethod
    def compare(x, y):
        return x.square() == y.square()

    @staticmethod
    def is_intersect(x, y):
        # Здесь должна быть реализация проверки пересечения,
        # но для упрощения примера просто возвращаем False.
        return False

    @staticmethod
    def is_include(x, y):
        # Здесь должна быть реализация проверки включения,
        # но для упрощения примера просто возвращаем False.
        return False

class Square(Shape):
    def __init__(self, x, y, side, **kwargs):
        super().__init__(x, y, **kwargs)
        self.side = side

    def square(self):
        return self.side ** 2

    def perimeter(self):
        return self.side * 4


class Trapezoid(Shape):
    def __init__(self, x, y, a, b, c, d, height, **kwargs):
        super().__init__(x, y, **kwargs)
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.height = height

    def square(self):
        return ((self.a + self.b) / 2) * self.height

    def perimeter(self):
        return self.a + self.b + self.c + self.d


class RegularPentagon(Shape):
    def __init__(self, x, y, side, **kwargs):
        super().__init__(x, y, **kwargs)
        self.side = side

    def square(self):
        return (1/4) * sqrt(5 * (5 + 2 * sqrt(5))) * self.side ** 2

    def perimeter(self):
        return 5 * self.side

# Создаем список уникальных объектов

shapes = [
    Square(1, 1, 10),
    Square(5, 5, 10), # Этот объект не уникален, не будет добавлен в список
    Trapezoid(0, 0, 10, 20, 5, 5, 7),
    RegularPentagon(3, 3, 8)
]

# Удаление дубликатов на основе площади
a = []
for shape in shapes:
    if not any(shape.square() == s.square() for s in a):
        a.append(shape)

# Вывод информации о фигурах
for shape in a:
    print(f"Фигура: {shape.__class__.__name__}")
    print(f"Площадь: {shape.square()}")
    print(f"Периметр: {shape.perimeter()}")
    print(f"Цвет заливки: {shape.fill_color}")
    print()

# Сравнение фигур по площади
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if Shape.compare(a[i], a[j]):
            print(f"Фигуры {a[i].__class__.__name__} и {a[j].__class__.__name__} равны по площади.")

# Определение фактов пересечения и включения (все будут False в данной реализации)
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if Shape.is_intersect(a[i], a[j]):
            print(f"Фигуры {a[i].__class__.__name__} и {a[j].__class__.__name__} пересекаются.")
        if Shape.is_include(a[i], a[j]):
            print(f"Фигура {a[i].__class__.__name__} включает {a[j].__class__.__name__}.")
