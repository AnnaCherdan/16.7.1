# начальные координаты x, y, width и height. x = 5, y = 10, width = 50, height = 100


class MyRectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle: {self.x}, {self.y}, {self.width}, {self.height}.'


rec = MyRectangle(5, 10, 50, 100)
print(rec)
print('-' * 20)


class MyRectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle: {self.x}, {self.y}, {self.width}, {self.height}.'

    def get_area(self):
        return self.width * self.height


rec = MyRectangle(5, 10, 50, 100)
print(rec.get_area())
print('-' * 20)
