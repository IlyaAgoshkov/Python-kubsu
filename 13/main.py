from shape import Shape
from c1 import Square
from c2 import Trapezoid
from c3 import RegularPentagon
import random


shapes = [
    Square(1, 1, 10),
    Trapezoid(0, 0, 10, 20, 5, 5, 7),
    RegularPentagon(3, 3, 8),
    Square(1, 1, 10),
    Trapezoid(0, 0, 10, 20, 5, 5, 7),
    RegularPentagon(3, 3, 8),
    Square(1, 1, 10),
    Trapezoid(0, 0, 10, 20, 5, 5, 7),
    RegularPentagon(3, 3, 8),
    Square(1, 1, 10),
    Trapezoid(0, 0, 10, 20, 5, 5, 7),
    RegularPentagon(3, 3, 8),
    Square(1, 1, 10),
    Trapezoid(0, 0, 10, 20, 5, 5, 7),
    RegularPentagon(3, 3, 8)
]

print(shapes)
# Вывод информации о фигурах
for shape in shapes:
    print(f"Фигура: {shape.__class__.__name__}")
    print(f"Площадь: {shape.square()}")
    print(f"Периметр: {shape.perimeter()}")
    print(f"Цвет заливки: {shape.fill_color}")
    print()

# Сравниваем фигуры по площади, определяем пересечения и включения
for i in range(len(shapes)):
    for j in range(i + 1, len(shapes)):
        if shapes[i].compare(shapes[j]):
            print(f"Фигура {i+1} и фигура {j+1} имеют одинаковую площадь")
        if shapes[i].is_intersect(shapes[j]):
            print(f"Фигура {i+1} и фигура {j+1} пересекаются")
        if shapes[i].is_include(shapes[j]):
            print(f"Фигура {j+1} включена в фигуру {i+1}")