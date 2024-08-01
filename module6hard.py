class Figure:
    sides_count = 0
    def __init__(self, _color, _sides):
        self._color = _color
        self._sides = _sides
    filled = bool
    def get_color(self):
        return list(self._color)
    def __is_valid_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        if (self.r >= 0 and self.r <= 255
        and self.g >= 0 and self.g <= 255
        and self.b >= 0 and self.b <= 255):
            return True
        else:
            return False
    def set_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        if self.__is_valid_color(self.r, self.g, self.b) == True:
            self._color = [self.r, self.g, self.b]
        else:
            self.get_color()
    def __is_valid_sides(self, _sides):
        self._sides = _sides
        if self._sides == self.sides_count and type(self._sides) == int and self._sides > 0:
            return True
        else:
            return False
    def get_sides(self):
        return self._sides
    def __len__(self):
        return sum(self._sides)
    def set_sides(self, *new_sides):
        self.new_sides = new_sides
        self.new_sides2 = ()
        self.sides = (self._sides, )
        for i in self.new_sides:
            self.new_sides2 = self.new_sides2 + (i, )
        if len(self.new_sides2) != len(self.sides):
            self._sides = self.sides[0]
        else:
            self._sides = [self.new_sides2[0]]
class Circle(Figure):
    def __init__(self, _color, _sides):
        self.sides_count = 1
        super().__init__(_color, _sides)
        self._radius = self._sides / 2
    def get_square(self):
        import math
        return math.pi * self._radius * self._radius
class Triangle(Figure):
    def __init__(self, _color, _sides):
        self.sides_count = 3
        super().__init__(_color, _sides)
        import math
        self.p = sum(self._sides) / 2   # Полупериметр
        self.hA = (2 * math.sqrt(self.p * (self.p - self._sides[0]) * (self.p - self._sides[1]) * (self.p - self._sides[2]))) / self._sides[0]
        self.hB = (2 * math.sqrt(self.p * (self.p - self._sides[0]) * (self.p - self._sides[1]) * (self.p - self._sides[2]))) / self._sides[1]
        self.hC = (2 * math.sqrt(self.p * (self.p - self._sides[0]) * (self.p - self._sides[1]) * (self.p - self._sides[2]))) / self._sides[2]
    def get_square(self):
        return (self.p * (self.p - self._sides[0]) * (self.p - self._sides[1]) * (self.p - self._sides[2])) ** 0.5
class Cube(Figure):
    def __init__(self, _color, _sides):
        self.sides_count = 12
        super().__init__(_color, _sides)
        self._sides_new = []
        for i in range(12):
            self._sides_new.append(self._sides)
        self._sides = self._sides_new
    def get_volume(self):
        return self._sides[0] ** 3

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