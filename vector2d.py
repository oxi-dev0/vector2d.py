import math
import random
class Vector2D(object):

    ZERO = Vector2D(0,0)
    ONE = Vector2D(1,1)

    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
    
    @staticmethod
    def UnitRandom():
        return Vector2D(random.random(), random.random())
    
    def __add__(self, other):
        newX = 0
        newY = 0
        if isinstance(other, Vector2D):
            newX = self.x + other.x
            newY = self.y + other.y
        elif isinstance(other, (int, float)):
            newX = self.x + other
            newY = self.y + other
        else:
            raise RuntimeError(f"Vector2D '+' requires Vector2D, int or float as parameter.")
        return Vector2D(newX, newY)
    
    def __iadd__(self, other):
        if isinstance(other, Vector2D):
            self.x += other.x
            self.y += other.y
        elif isinstance(other, (int, float)):
            self.x += other
            self.y += other
        else:
            raise RuntimeError(f"Vector2D '+=' requires Vector2D, int or float as parameter.")
        return self
    
    def __sub__(self, other):
        newX = 0
        newY = 0
        if isinstance(other, Vector2D):
            newX = self.x - other.x
            newY = self.y - other.y
        elif isinstance(other, (int, float)):
            newX = self.x - other
            newY = self.y - other
        else:
            raise RuntimeError(f"Vector2D '-' requires Vector2D, int or float as parameter.")
        return Vector2D(newX, newY)
    
    def __isub__(self, other):
        if isinstance(other, Vector2D):
            self.x -= other.x
            self.y -= other.y
        elif isinstance(other, (int, float)):
            self.x -= other
            self.y -= other
        else:
            raise RuntimeError(f"Vector2D '-=' requires Vector2D, int or float as parameter.")
        return self
    
    def __mul__(self, other):
        newX = 0
        newY = 0
        if isinstance(other, Vector2D):
            newX = self.x * other.x
            newY = self.y * other.y
        elif isinstance(other, (int, float)):
            newX = self.x * other
            newY = self.y * other
        else:
            raise RuntimeError(f"Vector2D '*' requires Vector2D, int or float as parameter.")
        return Vector2D(newX, newY)
    
    def __imul__(self, other):
        if isinstance(other, Vector2D):
            self.x *= other.x
            self.y *= other.y
        elif isinstance(other, (int, float)):
            self.x *= other
            self.y *= other
        else:
            raise RuntimeError(f"Vector2D '*=' requires Vector2D, int or float as parameter.")
        return self
    
    def __truediv__(self, other):
        newX = 0
        newY = 0
        if isinstance(other, Vector2D):
            newX = self.x / other.x
            newY = self.y / other.y
        elif isinstance(other, (int, float)):
            newX = self.x / other
            newY = self.y / other
        else:
            raise RuntimeError(f"Vector2D '/' requires Vector2D, int or float as parameter.")
        return Vector2D(newX, newY)
    
    def __floordiv__(self, other):
        newX = 0
        newY = 0
        if isinstance(other, Vector2D):
            newX = self.x // other.x
            newY = self.y // other.y
        elif isinstance(other, (int, float)):
            newX = self.x // other
            newY = self.y // other
        else:
            raise RuntimeError(f"Vector2D '//' requires Vector2D, int or float as parameter.")
        return Vector2D(newX, newY)
    
    def __itruediv__(self, other):
        if isinstance(other, Vector2D):
            self.x /= other.x
            self.y /= other.y
        elif isinstance(other, (int, float)):
            self.x /= other
            self.y /= other
        else:
            raise RuntimeError(f"Vector2D '/=' requires Vector2D, int or float as parameter.")
        return self
    
    def __ifloordiv__(self, other):
        if isinstance(other, Vector2D):
            self.x //= other.x
            self.y //= other.y
        elif isinstance(other, (int, float)):
            self.x //= other
            self.y //= other
        else:
            raise RuntimeError(f"Vector2D '//=' requires Vector2D, int or float as parameter.")
        return self
    
    def __pow__(self, other):
        newX = 0
        newY = 0
        if isinstance(other, (int, float)):
            newX = self.x ** other
            newY = self.y ** other
        else:
            raise RuntimeError(f"Vector2D '**' requires int or float as parameter.")
        return Vector2D(newX, newY)
    
    def __neg__(self):
        return Vector2D(-self.x, -self.y)
    
    def __eq__(self, other):
        if isinstance(other, Vector2D):
            return self.x == other.x and self.y == other.y
        else:
            raise RuntimeError(f"Vector2D '==' requires Vector2D as parameter.")
    
    def __str__(self):
        return "Vector {X:" + str(self.x) + ", Y:" + str(self.y) + "}"

    @property
    def length(self):
        return math.sqrt((self.x ** 2) + (self.y ** 2))
    
    def getNormalised(self):
        length = self.length

        # Prevent DBZ error
        if length == 0:
            return Vector2D.ZERO

        return Vector2D(self.x/length, self.y/length)
    
    @staticmethod
    def DotProduct(a, b):
        if (not isinstance(a, Vector2D)) or (not isinstance(b, Vector2D)):
            raise RuntimeError(f"FVector2D.DotProduct() requires Vector2D as parameters.")
        else:
            return a.x * b.x + a.y * b.y
    
    @staticmethod
    def Project(a, b):
        if (not isinstance(a, Vector2D)) or (not isinstance(b, Vector2D)):
            raise RuntimeError(f"Vector2D.Project() requires Vector2D as parameters.")
        else:
            normB = b.Normalise()
            return normB * Vector2D.DotProduct(a, normB)

    def AsInt(self):
        return Vector2D(int(self.x), int(self.y))
    
    @staticmethod
    def isPointOnSegment(p1, p2, p):
        if (not isinstance(p1, Vector2D)) or (not isinstance(p2, Vector2D)) or (not isinstance(p, Vector2D)):
            raise RuntimeError(f"Vector2D.isPointOnSegment() requires Vector2D as parameters.")
        else:
            return min(p1.x, p2.x) <= p.x <= max(p1.x, p2.x) and min(p1.y, p2.y) <= p.y <= max(p1.y, p2.y)
    
    @staticmethod
    def CrossProduct(a, b):
        if (not isinstance(a, Vector2D)) or (not isinstance(b, Vector2D)):
            raise RuntimeError(f"Vector2D.CrossProduct() requires Vector2D as parameters.")
        else:
            return a.x*b.y - a.y*b.x
    
    @staticmethod
    def Direction(p1, p2, p3):
        if (not isinstance(p1, Vector2D)) or (not isinstance(p2, Vector2D)) or (not isinstance(p3, Vector2D)):
            raise RuntimeError(f"Vector2D.Direction() requires Vector2D as parameters.")
        else:
            return Vector2D.CrossProduct(p3 - p1, p2 - p1)
    
    @staticmethod
    def isIntersecting(p1, p2, p3, p4):
        if (not isinstance(p1, Vector2D)) or (not isinstance(p2, Vector2D)) or (not isinstance(p3, Vector2D)) or (not isinstance(p4, Vector2D)):
            raise RuntimeError(f"Vector2D.isIntersecting() requires Vector2D as parameters.")
        else: 
            d1 = Vector2D.Direction(p3, p4, p1)
            d2 = Vector2D.Direction(p3, p4, p2)
            d3 = Vector2D.Direction(p1, p2, p3)
            d4 = Vector2D.Direction(p1, p2, p4)

            if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
                return True

            elif d1 == 0 and Vector2D.isPointOnSegment(p3, p4, p1):
                return True
            elif d2 == 0 and Vector2D.isPointOnSegment(p3, p4, p2):
                return True
            elif d3 == 0 and Vector2D.isPointOnSegment(p1, p2, p3):
                return True
            elif d4 == 0 and Vector2D.isPointOnSegment(p1, p2, p4):
                return True
            else:
                return False
