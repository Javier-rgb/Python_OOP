class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dinstance(self, another_coord):
        x_diff = (self.x - another_coord.x)**2
        y_diff = (self.y - another_coord.y)**2

        return (x_diff + y_diff)**.5

if __name__ == '__main__':
    coord_1 = Coord(3, 30)
    coord_2 = Coord(4, 8)

    print(coord_1.dinstance(coord_2))