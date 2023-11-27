
class Shape:
    def __init__(self, x, y, fill_color='black'):
        self.x = x
        self.y = y
        self.fill_color = 1

    def square(self):
        pass

    def perimeter(self):
        pass

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
        return False

    @staticmethod
    def is_include(x, y):
        return False

