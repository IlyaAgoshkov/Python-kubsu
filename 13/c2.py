from shape import Shape
class Trapezoid(Shape):
    def __init__(self, x, y, a, b, c, d, height):
        super().__init__(x, y)
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.height = height

    def square(self):
        return ((self.a + self.b) / 2) * self.height

    def perimeter(self):
        return self.a + self.b + self.c + self.d