# 1.4
class Point:
    color = 'red'
    circle = 2

    def set_coords(self, x, y):  # self - ссылка на экземпляр класса (pt)
        print("вызов метода set_coords. ссылка - " + str(self))

# 6:51
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)


pt1 = Point()
print(pt1.set_coords(1, 2))

pt2 = Point()
print(pt2.set_coords(11, 22))

#======================================================================================================================
# 1.5  Инициализатор __init__ и финализатор __del__
# out __init__
class Point1:
    def set(self, x, y):
        self.x = x
        self.y = y

pt1 = Point1()
pt1.set(1, 2)
print(pt1.__dict__)
# {'x': 1, 'y': 2}


# with __init__
class Point2:
    def __init__(self, x=0, y=0):  # используются значения по умолчанию
        self.x = x
        self.y = y

pt2 = Point2(1, 2)
print(pt2.__dict__)
# {'x': 1, 'y': 2}


# with __del__
class Point3:
    def __init__(self, x=0, y=0):  # используются значения по умолчанию
        print(f'создание экземпляра {self}')
        self.x = x
        self.y = y
    def __del__(self):
        print(f'удаление экземпляра {self}')

pt3 = Point3(1, 2)
# создание экземпляра <__main__.Point3 object at 0x0000024861383950>
pt3 = 2
# удаление экземпляра <__main__.Point3 object at 0x0000024861383950>


#======================================================================================================================
"""
# 1.6 Магический метод __new__. 
"""
class Point:
    def __new__(cls, *args, **kwargs):
        print("вызов метода __new__ для" + str(cls))
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        print("вызов метода __init__ для " + str(self))
        self.x = x
        self.y = y


pt = Point(1, 2)

""" Пример паттерна Singleton """
class DataBase:
    __isntase = None
    def __new__(cls, *args, **kwargs):
        if cls.__isntase == None:
            cls.__isntase = super().__new__(cls)
        return cls.__isntase
    def __del__(self):
        DataBase.__isntase = None
