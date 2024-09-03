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
