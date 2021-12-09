class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return self.base * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


if __name__ == '__main__':
    rec1 = Rectangle(4, 6)
    print(rec1.area())

    sq1 = Square(5)
    print(sq1.area())