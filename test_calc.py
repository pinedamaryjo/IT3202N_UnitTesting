import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        result = calculator.addition(2, 3)
        self.assertEqual(result, 5)

    def test_subtraction(self):
        result = calculator.subtraction(10, 1)
        self.assertEqual(result, 9)
        
    def test_multiplication(self):
        result = calculator.multiplication(2, 3)
        self.assertEqual(result, 6)

    def test_division(self):
        result = calculator.division(10, 2)
        self.assertEqual(result, 5)
    
if __name__ == '__main__':
    unittest.main()
