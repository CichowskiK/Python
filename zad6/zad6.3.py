import rectangles
from points import Point
import unittest

class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.r1 = rectangles.Rectangle(3, 4 , 8, 8)   
        self.r2 = rectangles.Rectangle(-3, -8, 0 ,2.5)  
        self.r3 = rectangles.Rectangle(3.5 , 2.1, 4, 5.7) 
        self.r4 = rectangles.Rectangle(8, 8, 3, 4)

    def test__str__rectangle(self):
        self.assertEqual(str(self.r1), "[(3, 4), (8, 8)]")
        self.assertEqual(str(self.r2), "[(-3, -8), (0, 2.5)]")
        self.assertEqual(self.r3.__str__(), "[(3.5, 2.1), (4, 5.7)]")

    def test__repr__rectangle(self):
        self.assertEqual(self.r1.__repr__(), "Rectangle[(3, 4), (8, 8)]")
        self.assertEqual(self.r2.__repr__(), "Rectangle[(-3, -8), (0, 2.5)]")
        self.assertEqual(self.r3.__repr__(), "Rectangle[(3.5, 2.1), (4, 5.7)]")

    def test__eq__rectangle(self):
        self.assertTrue(self.r1 == self.r4)
        self.assertFalse(self.r2 == self.r3)

    def test__ne__rectangle(self):
        self.assertFalse(self.r1 != self.r4)
        self.assertTrue(self.r2 != self.r3)

    def test_center_rectangle(self): 
        self.assertEqual(self.r1.center(), Point(5.5, 6))
        self.assertEqual(self.r2.center(), Point(-1.5, -2.75))
        self.assertEqual(self.r4.center(), Point(5.5, 6))

    def test_area_rectangle(self):
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r2.area(), 31.5)
        self.assertEqual(self.r3.area(), 1.8)
        self.assertEqual(self.r4.area(), 20)

    def test_move_rectangle(self):
        self.assertEqual(self.r1.move(1, 1), rectangles.Rectangle(4, 5, 9 ,9))
        self.assertEqual(self.r1.move(2.2, 1.5), rectangles.Rectangle(6.2, 6.5, 11.2, 10.5))
        self.assertEqual(self.r1.move(-3.1, -2.5), rectangles.Rectangle(3.1, 4 , 8.1, 8))

    


if __name__ == '__main__':
    unittest.main()