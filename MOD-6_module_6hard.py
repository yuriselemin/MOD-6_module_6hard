import math


class Figure:
    def __init__(self, sides_count=0, color=(0, 0, 0)):
        self._sides = []
        self._color = color
        self.filled = False
        self.sides_count = sides_count

    def get_color(self):
        return self._color

    def is_valid_color(self, r, g, b):
        return all(0 <= c <= 255 for c in (r, g, b))

    def set_color(self, r, g, b):
        if self.is_valid_color(r, g, b):
            self._color = (r, g, b)

    def _is_valid_sides(self, new_sides):
        return len(new_sides) == self.sides_count and all(side > 0 for side in new_sides)

    def get_sides(self):
        return self._sides

    def __len__(self):
        return sum(self._sides)

    def set_sides(self, *new_sides):
        if not self._is_valid_sides(new_sides):
            return
        self._sides = list(new_sides)


class Circle(Figure):
    def __init__(self, color=(0, 0, 0), radius=0):
        super().__init__(sides_count=1, color=color)
        self._radius = radius

    def get_square(self):
        # Формула площади круга: π * r^2
        return self._radius ** 2 * math.pi

    def get_radius(self):
        return self._radius

    def set_radius(self, value):
        self._radius = value


class Triangle(Figure):
    def __init__(self, sides_count=3, color=(0, 0, 0)):
        super().__init__(sides_count=sides_count, color=color)
        self.__height = None

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def get_square(self):
        return 0.5 * self.get_sides()[0] * self.__height


class Cube(Figure):
    def __init__(self, *args, sides=1):
        super().__init__(*args)
        self.sides_count = sides
        self.__sides = [sides] * self.sides_count

    def set_sides(self, *new_sides):
        if self._is_valid_sides(new_sides) and len(new_sides) == self.sides_count:
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