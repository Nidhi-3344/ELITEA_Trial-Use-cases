import unittest

def classify_triangle(a, b, c):
    # This function will be implemented later
    pass

class TestTriangleClassification(unittest.TestCase):
    def test_invalid_triangle(self):
        self.assertEqual(classify_triangle(1, 1, 3), "Not a valid triangle")
        self.assertEqual(classify_triangle(3, 1, 1), "Not a valid triangle")
        self.assertEqual(classify_triangle(1, 3, 1), "Not a valid triangle")

    def test_equilateral_triangle(self):
        self.assertEqual(classify_triangle(5, 5, 5), "Equilateral triangle")

    def test_isosceles_triangle(self):
        self.assertEqual(classify_triangle(5, 5, 3), "Isosceles triangle")
        self.assertEqual(classify_triangle(5, 3, 5), "Isosceles triangle")
        self.assertEqual(classify_triangle(3, 5, 5), "Isosceles triangle")

    def test_scalene_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene triangle")

if __name__ == '__main__':
    unittest.main()