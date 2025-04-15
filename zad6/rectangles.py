from points import Point

class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self): 
        return "[(" + str(self.pt1.x) + ", " + str(self.pt1.y) + "), (" + str(self.pt2.x) + ", " + str(self.pt2.y) + ")]"          # "[(x1, y1), (x2, y2)]"

    def __repr__(self): 
        return "Rectangle[(" + str(self.pt1.x) + ", " + str(self.pt1.y) + "), (" + str(self.pt2.x) + ", " + str(self.pt2.y) + ")]"        # "Rectangle(x1, y1, x2, y2)"

    def __eq__(self, other): 
        return (self.pt1==other.pt1 and self.pt2==other.pt2) or (self.pt1==other.pt2 and self.pt2==other.pt1)   # obsługa rect1 == rect2

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self==other

    def center(self): 
        result = Point(0,0)
        result.x = (self.pt1.x + self.pt2.x) /2
        result.y = (self.pt1.y + self.pt2.y) /2
        return result

    def area(self): 
        return abs((self.pt1.x - self.pt2.x) * (self.pt1.y - self.pt2.y))            # pole powierzchni

    def move(self, x, y): 
        self.pt1 = self.pt1 + Point(x,y)  
        self.pt2 = self.pt2 + Point(x,y)     # przesunięcie o (x, y)
        return self

        