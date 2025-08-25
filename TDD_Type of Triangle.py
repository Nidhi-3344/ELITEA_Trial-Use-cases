import unittest
from Type_of_triangle import triangle_type

class TestTriangleType(unittest.TestCase):

    def test_equilateral_triangle(self):
        self.assertEqual(triangle_type(5, 5, 5), "Equilateral triangle")

    def test_isosceles_triangle(self):
        self.assertEqual(triangle_type(5, 5, 7), "Isosceles triangle")
        self.assertEqual(triangle_type(5, 7, 5), "Isosceles triangle")
        self.assertEqual(triangle_type(7, 5, 5), "Isosceles triangle")

    def test_scalene_triangle(self):
        self.assertEqual(triangle_type(3, 4, 5), "Scalene triangle")

    def test_invalid_triangle(self):
        self.assertEqual(triangle_type(1, 1, 3), "Not a valid triangle")
        self.assertEqual(triangle_type(1, 3, 1), "Not a valid triangle")
        self.assertEqual(triangle_type(3, 1, 1), "Not a valid triangle")

    def test_zero_side(self):
        self.assertEqual(triangle_type(0, 1, 1), "Not a valid triangle")
        self.assertEqual(triangle_type(1, 0, 1), "Not a valid triangle")
        self.assertEqual(triangle_type(1, 1, 0), "Not a valid triangle")

    def test_negative_side(self):
        self.assertEqual(triangle_type(-1, 1, 1), "Not a valid triangle")
        self.assertEqual(triangle_type(1, -1, 1), "Not a valid triangle")
        self.assertEqual(triangle_type(1, 1, -1), "Not a valid triangle")

if __name__ == '__main__':
    unittest.main()