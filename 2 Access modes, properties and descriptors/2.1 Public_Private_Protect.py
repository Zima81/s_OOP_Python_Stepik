# 2.1 Режимы доступа public, private, protected. Сеттеры и геттеры

# Приватные значения
class Point:
    def set_coord(self, x, y):
        if type(x) in (int, float) and type(y) in (int, float):  # Проверка на допустимые значения
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числамию")

    def get_coord(self):
        return self.__x, self.__y

pt = Point()
pt.set_coord(10, 20)  # СЕТТЕР устанавливает значения
pt.get_coord()   # ГЕТТЕР выдаёт приватные значения
# (10, 20)


# (9:10) Приватные методы
class Point2:
    def prot(self, a, b):
        self._a = a
        self._b = b

    # приватный метод
    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Координаты должны быть числами')

    def get_coord(self):
        return self.__x, self.__y

pt2 = Point2()
pt2.set_coord('1', 20)
pt2.get_coord()
# ValueError('Координаты должны быть числами')

pt2.set_coord(10, 20)
# показывает ВСЕ методы класса, да же приватные
print(dir(pt2))
# [..., '_Point__x', '_Point__y', ...]
print(pt2._Point__x)   # Обход защиты приват (Так лучше не делать)
# 10


# Модуль accessity дополнительно защищает приватные методы
# 13:20
from accessify import private, protected
class Point3:
    def prot(self, a, b):
        self._a = a
        self._b = b

    # Защита accessity
    @private
    @classmethod
    def check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y):
        self.__x = self.__y = 0
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Координаты должны быть числами')

    def get_coord(self):
        return self.__x, self.__y

pt3 = Point3()
print(pt3.check_value(5))
# Error

# Если закомментировать @private
class Point3:
    # Защита accessity
    #@private
    @classmethod
    def check_value(cls, x):
        return type(x) in (int, float)

pt3 = Point3()
print(pt3.check_value(5))
# True

