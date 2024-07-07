class Figure:
    def __init__(self, sides_count=0, *args):
        self.sides_count = sides_count
        self.__sides = []
        self.__color = []
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(0 <= c <= 255 for c in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(side > 0 for side in new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        pass

    def set_sides(self, *new_sides):
        if self.is_valid_sides(*new_sides) and len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)


class Circle(Figure):
    def __init__(self, *args, radius):
        super().__init__(*args)
        self.sides_count = 1
        self.__radius = radius

    def __len__(self):
        return 2 * 3.14 * self.__radius

    def get_square(self):
        return self.__radius ** 2 * 3.14


class Triangle(Figure):
    def __init__(self, *args):
        super().__init__(*args)
        self.sides_count = 3

    def __len__(self):
        pass

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5


class Cube(Figure):
    def __init__(self, *args, sides=1):
        super().__init__(*args)
        self.sides_count = sides
        self.__sides = [sides] * self.sides_count

    def set_sides(self, *new_sides):
        if self.is_valid_sides(*new_sides) and len(new_sides) == self.sides_count:
            self.__sides = new_sides

    def get_volume(self):
        side_length = self.__sides[0]
        return side_length ** 3


if __name__ == '__main__':
    
    circle1 = Circle((200, 200, 100), radius=10)
    cube1 = Cube((222, 35, 130), 6)

    circle1.set_color(55, 66, 77)
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)
    print(cube1.get_color())

    cube1.set_sides(5, 3, 12, 4, 5)
    print(cube1.get_sides())
    circle1.set_sides(15)
    print(circle1.get_sides())

    print(len(circle1))
    print(cube1.get_volume())




