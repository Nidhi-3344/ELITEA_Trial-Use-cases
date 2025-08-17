import unittest

class TestAddition(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)
    
    def test_add_positive_and_negative(self):
        self.assertEqual(add(2, -3), -1)
    
    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(5, 0), 5)
    
    def test_add_floats(self):
        self.assertAlmostEqual(add(2.5, 3.7), 6.2, places=2)

def add(a, b):
    return a + b

if __name__ == '__main__':
    unittest.main()