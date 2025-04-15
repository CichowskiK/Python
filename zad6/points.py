class Point:

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self): 
        return "(" + str(self.x) + ", " + str(self.y) + ")"         # zwraca string "(x, y)"

    def __repr__(self):
        return "Point(" + str(self.x) + ", " + str(self.y) + ")"         # zwraca string "Point(x, y)"

    def __eq__(self, other): 
        return self.x == other.x and self.y == other.y   # obsługa point1 == point2

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other): 
          result = Point(0, 0)   
          result.x = self.x + other.x
          result.y = self.y + other.y
          return result

    def __sub__(self, other): 
        result = Point(0, 0)   
        result.x = self.x - other.x
        result.y = self.y - other.y
        return result

    def __mul__(self, other): 
        return self.x*other.x + self.y*other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self): 
        return (self.x ** 2 + self.y ** 2) ** 0.5        # długość wektora

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points