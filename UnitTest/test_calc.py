"This is unit test for calc.py"
import unittest
from MainCode import calc


class TestCalc(unittest.TestCase):
    "Class TextCalc is the main class"

    def test_add(self):
        "function test for add"
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        "function test for subtract"
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(5, 10), -5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_divide(self):
        "function test for divide"
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        # with self.assertRaises(ValueError):
        #     calc.divide(10, 0)

    if __name__ == '__main__':
        unittest.main()
