import unittest
from projects.Calculator.calculator import Calculator

class TestSum(unittest.TestCase):
    def test_sum(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(1,2), 5) 
    
    def test_large_sum(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(1000, 2000), 3000)

if __name__ == '__main__':
    unittest.main()