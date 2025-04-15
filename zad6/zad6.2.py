import points
import unittest

class TestPoints(unittest.TestCase):

    def setUp(self):
        self.p1 = points.Point(3, 4)   
        self.p2 = points.Point(-3, -8)  
        self.p3 = points.Point(3.5 , 2.1) 
        self.p4 = points.Point(3.0, 4.0)
        self.p5 = points.Point(1.4, -4)


    def test__str__point(self):
        self.assertEqual(points.Point.__str__(self.p1), "(3, 4)" )
        self.assertEqual(points.Point.__str__(self.p2), "(-3, -8)" )
        self.assertEqual(points.Point.__str__(self.p3), "(3.5, 2.1)" )

    def test__repr__point(self):
        self.assertEqual(points.Point.__repr__(self.p1), "Point(3, 4)")
        self.assertEqual(points.Point.__repr__(self.p2), "Point(-3, -8)")
        self.assertEqual(points.Point.__repr__(self.p3), "Point(3.5, 2.1)")

    def test__eq__point(self):
        self.assertFalse(self.p1.__eq__(self.p2))
        self.assertTrue(self.p1 == self.p4)

    def test__ne__point(self):
        self.assertTrue(self.p1 != self.p2)
        self.assertTrue(points.Point.__ne__(self.p2, self.p3))
        self.assertFalse(points.Point.__ne__(self.p1, self.p4))

    def test__add__point(self):
        self.assertEqual(self.p1 + self.p2, points.Point(0, -4))
        self.assertEqual(points.Point.__add__(self.p1, self.p3), points.Point(6.5, 6.1))
        self.assertEqual(points.Point.__add__(self.p3, self.p4), points.Point(6.5, 6.1))
        self.assertEqual(points.Point.__add__(self.p2, self.p3), points.Point(0.5, -5.9))

    def test__sub__point(self):
        self.assertEqual(points.Point.__sub__(self.p2, self.p1), points.Point(-6, -12))
        self.assertEqual(points.Point.__sub__(self.p4, self.p1), points.Point(0, 0))
        self.assertEqual(points.Point.__sub__(self.p3, self.p2), points.Point(6.5, 10.1))
        self.assertEqual(points.Point.__sub__(self.p1, self.p5), points.Point(1.6, 8))

    def test__mul__point(self):
        self.assertEqual(points.Point.__mul__(self.p1, self.p5), -11.8)
        self.assertEqual(points.Point.__mul__(self.p2, self.p4), -41)
        self.assertEqual(points.Point.__mul__(self.p2, self.p5), 27.8)
        self.assertEqual(points.Point.__mul__(self.p3, self.p2), -27.3)

    def test_cross_point(self):
        self.assertAlmostEqual(points.Point.cross(self.p1, self.p3), -7.7)   #assertAlmostEqual z uwagi na błąd zaokrąglenia
        self.assertEqual(points.Point.cross(self.p2, self.p5), 23.2)
        self.assertEqual(points.Point.cross(self.p3, self.p3), 0)
        self.assertEqual(points.Point.cross(self.p4, self.p5), -17.6)

    def test_lenght_point(self):
        self.assertEqual(points.Point.length(self.p1), 5)
        self.assertEqual(points.Point.length(self.p2), 73 ** 0.5)
        self.assertEqual(points.Point.length(self.p3), 16.66 ** 0.5)
        self.assertEqual(points.Point.length(self.p4), 25 ** 0.5)
        self.assertEqual(points.Point.length(self.p5), 17.96 ** 0.5)

    def test_hash_point(self):
        self.assertEqual(points.Point.__hash__(self.p1), points.Point.__hash__(self.p4))


if __name__ == '__main__':
    unittest.main()
