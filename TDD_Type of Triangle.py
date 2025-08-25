import unittest

def classify_triangle(a, b, c):
    # TODO: Implement this function
    pass

class TestTriangleClassification(unittest.TestCase):
    def test_invalid_triangle(self):
        self.assertEqual(classify_triangle(1, 1, 3), "Not a triangle")
        self.assertEqual(classify_triangle(0, 1, 1), "Not a triangle")
        self.assertEqual(classify_triangle(-1, 2, 2), "Not a triangle")

    def test_equilateral_triangle(self):
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")

    def test_isosceles_triangle(self):
        self.assertEqual(classify_triangle(5, 5, 3), "Isosceles")
        self.assertEqual(classify_triangle(5, 3, 5), "Isosceles")
        self.assertEqual(classify_triangle(3, 5, 5), "Isosceles")

    def test_scalene_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene")

if __name__ == '__main__':
    unittest.main()