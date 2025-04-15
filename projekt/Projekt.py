from itertools import zip_longest
from collections.abc import Iterable

class Poly:

    def __init__(self, poly):
        if not isinstance(poly, Iterable):
            raise TypeError("Argumentem konstruktora musi być iterowalny")
        poly = list(poly) 
        if len(poly) == 0:
            raise ValueError("Nie można utworzyć wielomianu z pustej listy")
        for wsp in poly:
            if not isinstance(poly[0], (int, float)):
                raise TypeError("Niepoprawny typ współczynników")
        self.poly = poly

    @classmethod
    def str_into_poly(cls, string):
        poly = [int(num) for num in string.split()]
        return cls(poly)
    
    @classmethod
    def int_into_poly(cls, c, power):
        size = power + 1   
        poly = size * [0]
        poly[size-1] = c
        return cls(poly)

    def __getitem__(self, index):
        return self.poly[index]
    
    def __setitem__(self, index, value):
        self.poly[index]=value

    def __str__(self):
        if all(coeff == 0 for coeff in self):
            return "0"
        j=1
        if self[0] != 0:
            result = str(self[0])
        else:
            while self[j] == 0 and j < len(self):
                j = j+1
            if j == len(self):
                return "0"
            if self[j] == 1:
                result ="x^" + str(j)
            else:
                result =str(self[j]) + "x^" + str(j)
            j = j + 1
        for i  in range(j, len(self)):
            if self[i] == 1:
                result +="+x^" + str(i)
            elif self[i] < 0:
                result +=str(self[i]) + "x^" + str(i)
            elif self[i] > 0:
                result += "+" + str(self[i]) + "x^" + str(i)
            else:
                continue
        return result
    
    def __repr__(self):
        return "Polynominal= " +str(self)
    
    def pop(self):
        if len(self.poly) == 0:
            raise IndexError("pop from empty poly")
        value = self.poly.pop(-1)
        if not self.poly:
            self.poly.append(0)
        return value
    
    def remove_trailing_zeros(self):
        while self and self[-1] == 0:
            if len(self) == 1:
                break
            self.pop() 
        return self
    
    def __len__(self):
        self.remove_trailing_zeros
        return len(self.poly)

    def __add__(self, other):
        if isinstance(other, Poly):
            result = list(a + b for a, b in zip_longest(self, other, fillvalue=0))
        elif isinstance(other, (int, float)):
            result = self.poly[:]
            result[0] += other
        else: raise TypeError("dodawnie niezdefiniowane")

        return Poly(result)

    __radd__ = __add__


    def __sub__(self, other):
        if isinstance(other, Poly):
            result = list(a - b for a, b in zip_longest(self.poly, other.poly, fillvalue=0))

        elif isinstance(other, (int, float)):
            result = self.poly[:]
            result[0] -= other
        else: raise TypeError("odejmowanie niezdefiniowane")

        return Poly(result)
    
    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            result = -self
            result[0] += other
            return result
        else: raise TypeError("odejmowanie niezdefiniowane")


    def __neg__(self):
        poly = self.poly[:]
        for i in range(len(self)):
            poly[i] = -self[i]
        return Poly(poly)


    def __mul__(self, other):
        if isinstance(other, Poly):
            result=[0]*(len(self)+len(other))
            for i in range(len(self)):
                for j in range(len(other)):
                    result[i+j] += other[j]*self[i]
            return Poly(result).remove_trailing_zeros()
        elif isinstance(other, (int, float)):
            result = [0] * len(self)
            for i in range(len(self)):
                result[i] = self[i] * other
            return Poly(result)
        else : raise TypeError("mnozenie niezdefiniowe")

    __rmul__ = __mul__

    def __abs__(self):
        result =self.poly[:]
        for i in range(len(result)):
            result[i] = abs(result[i])
        return Poly(result)

    def is_zero(self):
        for i in range(len(self)):
            if self[i] !=0:
                return False
        return True

    def __eq__(self,other):
        result = self - other
        return result.is_zero()

    def __nq__(self, other):
        return not self == other

    def eval_poly(self, x0):
        result = 0
        for iteam in reversed(self.poly):
            result = result * x0 + iteam
        return result

    def __pow__(self, n):
        result = self
        if(n==0):
            return [1]
        for i in range(n-1):
            result = result * self
        return result.remove_trailing_zeros()

    def combine_poly(self, other):
        result= Poly([0]*(len(self)*len(other)-1))
        for i in range(len(self)):
            pow_poly2 = other ** i
            for j in range(len(pow_poly2)):
                result[j] += self[i] * pow_poly2[j]
        return result.remove_trailing_zeros()

    def diff_poly(self):
        if len(self) == 1:
            return Poly([0])
        result=Poly([0]*(len(self)-1))
        for i in range(len(self)-1):
            result[i] = self[i+1]*(i+1)
        return result.remove_trailing_zeros()
    
    def integrate_poly(self):
        if self.is_zero():
            return Poly([0])
        else:
            result = [0] * (len(self.poly) + 1)
            for i in range(1, len(result)):
                result[i] = self.poly[i-1] * (1/i)
            return Poly(result)

    def ile_jednomianow(self):
        counter = 0
        for i in range(len(self)):
            if self[i] != 0:
                counter += 1
        return counter
    
    def __call__(self, x):
        if isinstance(x, Poly):
            return self.combine_poly(x)
        elif isinstance(x, (int, float)):
            return self.eval_poly(x)
        else: raise TypeError("dzialanie niezdefiniowane")

    

import unittest

class TestPoly(unittest.TestCase):

    def setUp(self):
        self.poly1 = Poly([1, 2, 3])  
        self.poly2 = Poly([0, -1, 4]) 
        self.poly_zero = Poly([0])    

    def test_init(self):
        p = Poly(x for x in range(3))
        self.assertEqual(p.poly, [0, 1, 2])
        with self.assertRaises(TypeError) : 
            Poly(('a' , 'b', 'c'))

    def test_int_into_poly(self):
        poly1 = Poly.int_into_poly(2, 3)
        self.assertEqual(poly1, Poly([0, 0, 0, 2]))

    def test_str_into_poly(self):
        poly = Poly.str_into_poly("1 2 3")
        self.assertEqual(poly, self.poly1)

    def test_getitem(self):
        self.assertEqual(self.poly1[0], 1)
        self.assertEqual(self.poly1[2], 3)

    def test_setitem(self):
        self.poly1[0] = 5
        self.assertEqual(self.poly1[0], 5)

    def test_remove_trailing_zeros(self):
        p = Poly([1, 0, 0])
        p.remove_trailing_zeros()
        self.assertEqual(p, Poly([1]))

        p = Poly([0, 0])
        p.remove_trailing_zeros()
        self.assertEqual(p.poly, [0])
        self.assertTrue(p.is_zero())

    def test_str(self):
        self.assertEqual(str(self.poly1), "1+2x^1+3x^2")
        self.assertEqual(str(self.poly2), "-1x^1+4x^2")

    def test_repr(self):
        self.assertEqual(repr(self.poly1), "Polynominal= 1+2x^1+3x^2")
        self.assertEqual(repr(self.poly2), "Polynominal= -1x^1+4x^2")

    def test_add(self):
        result = self.poly1 + self.poly2
        self.assertEqual(result.poly, [1, 1, 7])
        self.assertEqual(self.poly1 + Poly([1,2]), Poly([2, 4, 3]))
        self.assertEqual(self.poly1 + 1.5, Poly([2.5, 2, 3]))
        self.assertEqual(1.5 + self.poly1, Poly([2.5, 2, 3]))

    def test_sub(self):
        result = self.poly1 - self.poly2
        self.assertEqual(result.poly, [1, 3, -1])
        self.assertEqual(self.poly1 - 2, Poly([-1, 2, 3]))
        self.assertEqual(2 - self.poly1, Poly([1, -2, -3]))
        self.assertEqual(self.poly1 - 2, Poly([-1, 2, 3]))

    def test_mul(self):
        result = self.poly1 * self.poly2
        self.assertEqual(result.poly, [0, -1, 2, 5, 12])
        self.assertEqual(self.poly1 * 2, Poly([2, 4, 6]))

    def test_is_zero(self):
        self.assertTrue(self.poly_zero.is_zero())
        self.assertFalse(self.poly1.is_zero())

    def test_eq(self):
        self.assertTrue(self.poly1 == Poly([1, 2, 3]))
        self.assertFalse(self.poly1 == self.poly2)

    def test_eval_poly(self):
        self.assertEqual(self.poly1.eval_poly(2), 17)

    def test_pow(self):
        result = self.poly1 ** 2
        self.assertEqual(result.poly, [1, 4, 10, 12, 9])

    def test_combine_poly(self):
        combined = self.poly1.combine_poly(self.poly2)
        self.assertEqual(combined.poly, [1, -2, 11, -24, 48]) 

    def test_diff_poly(self):
        derivative = self.poly1.diff_poly()
        self.assertEqual(derivative.poly, [2, 6]) 

    def test_integrate_poly(self):
        integrate = Poly([1, 1, 3]).integrate_poly()
        result = Poly([0, 1.0, 0.5, 1.0])
        self.assertEqual(integrate, result)

    def test_ile_jednomianow_poly(self):
        self.assertEqual(self.poly1.ile_jednomianow(), 3)
        self.assertEqual(Poly([1, 0, 0, 2]).ile_jednomianow(), 2)

    def test__call__poly(self):
        self.assertEqual(self.poly1(1), 6)
        self.assertEqual(self.poly1(self.poly2), Poly([1, -2, 11, -24, 48]))

if __name__ == "__main__":
    unittest.main()