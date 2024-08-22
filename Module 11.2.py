class Figure:
    sides_count = 0

    def __init__(self, color, sides, filled=False):
        if self.__is_valid_sides(*sides):
            if isinstance(self, Cube):
                self.__sides = list(sides) * self.sides_count
            else:
                self.__sides = [1] * self.sides_count
        self.__color = list(color)
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        for color in [r, g, b]:
            if not (isinstance(color, int) and 0 <= color <= 255):
                return False
        return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        if isinstance(self, Cube):
            cond1 = len(sides) == 1
        else:
            cond1 = len(sides) == self.sides_count

        cond2 = all([isinstance(side, int) and side > 0 for side in sides])
        return cond1 and cond2

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: tuple, *sides):
        super().__init__(color, sides)

    def get_sides(self):
        return [*self.__sides]

    def get_volume(self):
        return self.__sides[1] ** 3


def introspection_info(obj):
    print(f'Тип Объекта: {type(obj)}')
    print(f'Пространство имен: {dir(obj)}')
    print(f'Атрибут: {getattr(obj, 'set_color')}')
    print(f'Наличие атрибута: {hasattr(obj, 'sides_count')}')
    print(f'Модуль {obj.__name__}')


introspection_info(Figure)

