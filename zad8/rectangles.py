from points import Point

class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        if (x1 >= x2 or y1 >= y2):
            raise ValueError("nieprawidłowe punkty")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    @classmethod
    def from_points(cls, p1, p2):
        new_rectangle = cls(p1.x, p1.y, p2.x, p2.y)
        return new_rectangle


    def __str__(self): 
        return "[(" + str(self.pt1.x) + ", " + str(self.pt1.y) + "), (" + str(self.pt2.x) + ", " + str(self.pt2.y) + ")]"          # "[(x1, y1), (x2, y2)]"

    def __repr__(self): 
        return "Rectangle[(" + str(self.pt1.x) + ", " + str(self.pt1.y) + "), (" + str(self.pt2.x) + ", " + str(self.pt2.y) + ")]"        # "Rectangle(x1, y1, x2, y2)"

    def __eq__(self, other): 
        return (self.pt1==other.pt1 and self.pt2==other.pt2) or (self.pt1==other.pt2 and self.pt2==other.pt1)   # obsługa rect1 == rect2

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self==other

    @property
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
    
    @property
    def top(self):
        return self.pt2.y
    
    @property
    def left(self):
        return self.pt1.x
    
    @property
    def bottom(self):
        return self.pt1.y
    
    @property
    def right(self):
        return self.pt2.x
    
    @property
    def width(self):
        return self.pt2.x - self.pt1.x
    
    @property
    def height(self):
        return self.pt2.y - self.pt1.y
    
    @property
    def bottomleft(self):
        return self.pt1
    
    @property
    def topright(self):
        return self.pt2
    
    @property
    def topleft(self):
        return Point(self.pt1.x, self.pt2.y)
    
    @property
    def bottomright(self):
        return Point(self.pt2.x, self.pt1.y)
    


    

        