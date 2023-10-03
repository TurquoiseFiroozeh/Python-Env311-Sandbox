"This is unit test for employee.py"
import unittest
from MainCode.employee import Employee


class TestEmployee(unittest.TestCase):
    "Class TextEmployee is the main class"

    def test_email(self):
        "function test for email"
        emp_1 = Employee('Corey', 'Schafer', 50000)
        emp_2 = Employee('Sue', 'Smith', 60000)

        self.assertEqual(emp_1.email(), 'Corey.Schafer@email.com')
        self.assertEqual(emp_2.email(), 'Sue.Smith@email.com')

    if __name__ == '__main__':
        unittest.main()
