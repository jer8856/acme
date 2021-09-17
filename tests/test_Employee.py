from acme import Employee
import unittest

class TestEmploye(unittest.TestCase):

    def setUp(self):
        self.employee = Employee('TEST_RENE')

    def test_getSalary(self):
        salary: float = self.employee.getSalary(
            'MO10:00-12:00,,')
        self.assertEqual(salary, 30)
        salary: float = self.employee.getSalary(
            'TH00:01-00:00')
        self.assertEqual(salary, 480)
        salary: float = self.employee.getSalary(
            'SU05:00-11:00,MO18:00-19:00')
        self.assertEqual(salary, 540.0)
