from math import sqrt

class Figure:
    sides_count = 0

    def __init__(self, color=(0, 0, 0), *sides):
        self.__color = list(color)
        self.__sides = list(sides) if self.__is_valid_sides(*sides) else [*sides] * self.sides_count
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides) and len(sides) == self.sides_count

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            self.__sides = list(new_sides)
        else:
            self.__sides = self.__sides

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = sides[0] / (2 * 3.14159)

    def get_square(self):
        return 3.14159 * self.__radius ** 2

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.side = sides[0]
        self.square = round((sqrt(3) * self.side ** 2) / 4, 1)
        __height = (2 * self.square) / self.side

    def get_square(self):
        return self.square

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if sides:
            __sides = [sides[0]] * self.sides_count
        else:
            __sides = [1] * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        length_side = self.get_sides()[0]
        return length_side ** 3

if __name__ == "__main__":


    circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77) # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15) # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15) # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())

