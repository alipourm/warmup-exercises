import unittest


# Make this recursive function more efficient
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# complete the following function to reverse the 'input_list' list
def revese(input_list):
    raise NotImplementedError

class TriangleType:
    ISOLACE = 0
    EQUILATERAL = 1
    SCALENE = 2
    INVALID = -1

# The following function should return the type of a triangle give the values of its
# sides, i.e., a , b, c
def get_triangle_type(a, b, c):
    if a == b == c:
        return TriangleType.EQUILATERAL
    raise NotImplementedError


# The following function should sort `input_list` and return the result
def mysort(inp_list):
    raise NotImplementedError

class DSTest(unittest.TestCase):
    def test_fib_zero(self):
        self.assertEqual(fib(0), 1)

    def test_fib_10(self):
        self.assertEqual(fib(10), fib(8)+fib(9))
    
    def test_rev_1(self):
        self.assertListEqual(revese([3,2 ,1]), [1, 2, 3])
    
    def test_triangle_1(self):
        self.assertEqual(get_triangle_type(2,2,2), TriangleType.EQUILATERAL, "Triangle (2,2,2) is equilatral!")

    def test_mysort_1(self):
        self.assertListEqual(mysort([3,2 ,1]), [1, 2, 3])

if __name__ == "__main__":
    unittest.main()