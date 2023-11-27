from math import sqrt
from shape import Shape


class RegularPentagon(Shape):
    def __init__(self, x, y, side):
        super().__init__(x, y)
        self.side = side

    def square(self):
        return (1/4) * sqrt(5 * (5 + 2 * sqrt(5))) * self.side ** 2

    def perimeter(self):
        return 5 * self.side