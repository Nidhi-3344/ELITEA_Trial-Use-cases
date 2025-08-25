import unittest

# Red stage: Write failing tests

class TestTriangleType(unittest.TestCase):
    def test_equilateral_triangle(self):
        self.assertEqual(classify_triangle(5, 5, 5), "Equilateral")

    def test_isosceles_triangle(self):
        self.assertEqual(classify_triangle(5, 5, 3), "Isosceles")

    def test_scalene_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene")

    def test_invalid_triangle(self):
        self.assertEqual(classify_triangle(1, 1, 3), "Not a triangle")

    def test_negative_sides(self):
        with self.assertRaises(ValueError):
            classify_triangle(-1, 2, 3)

    def test_zero_side(self):
        with self.assertRaises(ValueError):
            classify_triangle(0, 2, 3)

# Green stage: Implement the function to pass the tests

def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("All sides must be positive")
    
    if a + b <= c or b + c <= a or c + a <= b:
        return "Not a triangle"
    
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or c == a:
        return "Isosceles"
    else:
        return "Scalene"

# Refactor stage: Improve the code while keeping tests passing

def is_valid_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def classify_triangle_refactored(a, b, c):
    if any(side <= 0 for side in (a, b, c)):
        raise ValueError("All sides must be positive")
    
    if not is_valid_triangle(a, b, c):
        return "Not a triangle"
    
    unique_sides = len(set([a, b, c]))
    if unique_sides == 1:
        return "Equilateral"
    elif unique_sides == 2:
        return "Isosceles"
    else:
        return "Scalene"

# Update test class to use refactored function
class TestTriangleTypeRefactored(unittest.TestCase):
    def test_equilateral_triangle(self):
        self.assertEqual(classify_triangle_refactored(5, 5, 5), "Equilateral")

    def test_isosceles_triangle(self):
        self.assertEqual(classify_triangle_refactored(5, 5, 3), "Isosceles")

    def test_scalene_triangle(self):
        self.assertEqual(classify_triangle_refactored(3, 4, 5), "Scalene")

    def test_invalid_triangle(self):
        self.assertEqual(classify_triangle_refactored(1, 1, 3), "Not a triangle")

    def test_negative_sides(self):
        with self.assertRaises(ValueError):
            classify_triangle_refactored(-1, 2, 3)

    def test_zero_side(self):
        with self.assertRaises(ValueError):
            classify_triangle_refactored(0, 2, 3)

if __name__ == '__main__':
    unittest.main()