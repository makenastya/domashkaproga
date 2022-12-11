import math


class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def __str__(self):
        return "[" + str(self._x) + ", " + str(self._y) + "]"


def dist(a, b):
    return ((b.get_y() - a.get_y()) ** 2 + (b.get_x() - a.get_x()) ** 2) ** 0.5


class Shape:
    def __init__(self, type="Shape"):
        self._type = type

    def __str__(self):
        return str(self._type)

    def area(self):
        pass

    def perimeter(self):
        pass


class Triangle(Shape):
    def __init__(self, p1, p2, p3, type="Triangle"):
        super().__init__(type)
        self._point_1 = p1
        self._point_2 = p2
        self._point_3 = p3

    def area(self):
        x1 = self._point_1.get_x()
        x2 = self._point_2.get_x()
        x3 = self._point_3.get_x()

        y1 = self._point_1.get_y()
        y2 = self._point_2.get_y()
        y3 = self._point_3.get_y()
        return abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2

    def perimeter(self):
        return (dist(self._point_1, self._point_2) +
                dist(self._point_2, self._point_3) +
                dist(self._point_3, self._point_1))

    # def __str__(self):
    #     return " ".join([super().__str__(), self._point_1.__str__(), self._point_2.__str__(),


#                      self._point_3.__str__()])


class Circle(Shape):
    def __init__(self, c, r, type="Circle"):
        super().__init__(type)
        self._c = c
        self._r = r

    def get_r(self):
        return self._r

    def set_r(self, r):
        self._r = r

    def get_c(self):
        return self._r

    def set_c(self, c):
        self._c = c

    def area(self):
        return (math.pi * self._r ** 2) / 2

    def perimeter(self):
        return 2 * math.pi * self._r


class Tetragon(Shape):
    def __init__(self, p1, p2, p3, p4, type="Tetragon"):
        super().__init__(type)
        self._point_1 = p1
        self._point_2 = p2
        self._point_3 = p3
        self._point_4 = p4

    def perimeter(self):
        return (dist(self._point_1, self._point_2) +
                dist(self._point_2, self._point_3) +
                dist(self._point_3, self._point_4) +
                dist(self._point_4, self._point_1))


class Rectangle(Tetragon):
    def __init__(self, p1, p2, p3, p4, type="Rectangle"):
        super().__init__(p1, p2, p3, p4, type)

    def get_a(self):
        return dist(self._point_1, self._point_4)

    def get_b(self):
        return dist(self._point_1, self._point_2)

    def area(self):
        return self.get_a() * self.get_b()


class Diamond(Tetragon):
    def __init__(self, p1, p2, p3, p4, type="Diamond"):
        super().__init__(p1, p2, p3, p4, type)

    def get_a(self):
        return dist(self._point_1, self._point_2)

    def area(self):
        return dist(self._point_1, self._point_3) * dist(self._point_2, self._point_4) / 2


class Square(Diamond):
    def __init__(self, p1, p2, p3, p4, type="Square"):
        super().__init__(p1, p2, p3, p4, type)

