from shape import Shape

class Square(Shape):
    def __init__(self, x, y, side):
        super().__init__(x, y)
        self.side = side

    def square(self):
        return self.side ** 2

    def perimeter(self):
        return self.side * 4