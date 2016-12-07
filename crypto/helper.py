from copy import copy
import os, numpy as np
from scipy import misc

class Point:

    a = 1389283738186319173918291937L
    b = 5930497892831938828372773728L

    def __init__(self, x='inf', y='inf'):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def __copy__(self):
        return Point(self.x, self.y)

    def __eq__(self, obj):
        if isinstance(obj, int) and obj == 0:
            return self.x > 1e302 or self.x < -1e302
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
                if self == 0:
                    return copy(self)
                try:
                    l = (3 * self.x**2 + Point.a)/(2 * self.y)
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
    def getGenerator():
        return Point(0, long(Point.b**0.5))

class Base:

    @staticmethod
    def toBase(arr, base):
        arr = np.array(arr, dtype='object')
        big = np.array([base**e for e in range(len(arr)-1, -1, -1)])
        return sum(arr * big)

    @staticmethod
    def fromBase(val, base):
        res = np.array([], dtype='object')
        while val >= base:
            res = np.concatenate((res, [val%base]))
            val /= base
        res = np.concatenate((res, [val]))
        return res[::-1]

class Image:

    @staticmethod
    def read(imageName):
        return misc.imread(os.path.join('.//image//', imageName))

    @staticmethod
    def save(imageName, imageArray):
        misc.imsave(os.path.join('.//image//', imageName), imageArray)