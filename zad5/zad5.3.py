import polys
import unittest

class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [1, 2, 3]      
        self.p2 = [4, 5]   

    def test_add_poly(self):
        self.assertEqual(polys.add_poly(self.p1, self.p2), [5, 7, 3])

    def test_sub_poly(self): 
        self.assertEqual(polys.sub_poly(self.p1, self.p2), [-3, -3, 3])

    def test_mul_poly(self): 
        self.assertEqual(polys.mul_poly(self.p1, self.p2), [4, 13, 22, 15])

    def test_is_zero(self): 
        self.assertFalse(polys.is_zero(self.p1))
        self.assertTrue(polys.is_zero([0, 0, 0, 0]))

    def test_eq_poly(self): 
        self.assertFalse(polys.eq_poly(self.p1, self.p2))
        self.assertTrue(polys.eq_poly([1, 0, 1, 0],[1, 0, 1]))

    def test_eval_poly(self): 
        self.assertEqual(polys.eval_poly(self.p1,2), 17)

    def test_combine_poly(self): 
        self.assertEqual(polys.combine_poly(self.p1, self.p2), [57, 130, 75])

    def test_pow_poly(self): 
        self.assertEqual(polys.pow_poly(self.p1, 2), [1, 4, 10, 12, 9])

    def test_diff_poly(self): 
        self.assertEqual(polys.diff_poly(self.p1), [2, 6])

    def tearDown(self): 
        self.assertEqual(polys.remove_trailing_zeros([1, 0, 0, 1, 0, 0]), [1, 0, 0, 1])

if __name__ == '__main__':
    unittest.main()

