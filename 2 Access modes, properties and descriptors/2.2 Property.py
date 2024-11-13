class Point:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_old(self):
        return self.__old

    def set_old(self, old):
        self.__old = old

    old_prop = property(get_old, set_old)


pt = Point('Tom', 10)
# при вызове property получаем 1-й метод, при присвоении 2-ю
print(pt.old_prop, '\n', pt.__dict__, '\n\n')  # Вызов метода property (get_old), и показ методов экз. класса
pt.old_prop = 20                               # Изменить значение property (вызов set_old)
pt.olds = 25                                   # Если имя отличается, от метода property, то создаст метод экз. класса
print(pt.old_prop, '\n', pt.__dict__)          # Вызов метода property (get_old), и показ методов экз. класса

"""=========================================================================================="""
# time 3:11
class Point2:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_old(self):
        return self.__old

    def set_old(self, old):
        self.__old = old

    """
    old = property(get_old, set_old)
    Переписать с использованиям декораторов
    """
    old = property()
    old = old.getter(get_old)
    old = old.setter(set_old)

pt = Point2('Tom', 10)
print(pt.old)
pt.old = 20
print(pt.old)

"""=========================================================================================="""
"""
    old = property()
    old = old.getter(get_old)
    old = old.setter(set_old)

    т.к. данная запись представляет дублирование её переписывают ...
"""


class Point3:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property  # создаётся property.getter()
    def get_old(self):
        return self.__old

    @get_old.setter  # создаётся property.setter()
    def get_old(self, old):
        self.__old = old

    @get_old.deleter  # создаётся property.deleter()
    def get_old(self):
        del self.__old

    """
    Именно так и записывается property
    """
pt3 = Point('Tom', 10)
print(pt3.get_old, '\n', pt3.__dict__, '\n\n')
pt3.get_old = 20
print(pt3.get_old, '\n', pt3.__dict__, '\n\n')
del pt3.get_old
print(pt3.__dict__)