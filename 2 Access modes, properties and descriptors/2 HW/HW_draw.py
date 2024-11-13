class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        if self.__check(x):
            self.__x = x
        if self.__check(y):
            self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @classmethod
    def __check(cls, data):
        if isinstance(data, (int, float)) and cls.MIN_COORD <= data <= cls.MAX_COORD:
            return data

    @staticmethod
    def norm2(vector):
        return vector.x * vector.x + vector.y * vector.y


r1 = RadiusVector2D()
print(r1.x)
