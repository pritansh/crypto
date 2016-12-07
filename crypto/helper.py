from copy import copy

class Point:

    def __init__(self, x='inf', y='inf'):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return '(' + str(round(self.x, 6)) + ',' + str(round(self.y, 6)) + ')'

    def __copy__(self):
        return Point(self.x, self.y)

    def __eq__(self, obj):
        if isinstance(obj, int) and obj == 0:
            return self.x > 1e20 or self.x < -1e20
        elif isinstance(obj, Point):
            if self.x == obj.x and self.y == obj.y:
                return True
            else:
                return False
    
    def __add__(self, obj):
        if self == obj:
            return self * 2
        if self == 0:
            return copy(obj)
        if obj == 0:
            return copy(self)
        try:
            l = (obj.y - self.y)/(obj.x - self.x)
        except ZeroDivisionError:
            return Point()
        x = l**2 - self.x - obj.x
        return Point(x, l*(self.x - x) - self.y)

    def __sub__(self, obj):
        return self + Point(obj.x, -obj.y)

    def __mul__(self, obj):
        if isinstance(obj, int):
            if obj == 2:
                try:
                    l = (3 * self.x**2)/(2 * self.y)
                except ZeroDivisionError:
                    return Point()
                x = l**2 - 2*self.x
                return Point(x, l*(self.x - x) - self.y)
            else:
                i = 1
                a = copy(self)
                b = Point()
                while i <= obj:
                    if i & obj:
                        b = b + a
                    a = a * 2
                    i <<= 1
                return b

    @staticmethod
    def toPoint(y):
        n = y**2 - 7
        return Point(n**(1./3) if n>=0 else -((-n)**(1./3)), y) 