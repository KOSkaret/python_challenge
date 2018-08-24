import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class employee """
    def setUp(self):
        """
        Creates an employee and default values for them.
        """
        first = 'Lars'
        last = 'Konrad'
        salary = 10000

        self.my_employee = Employee(first,last,salary)
    
    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, 15000)

    def test_give_custom_raise(self):
        self.my_employee.give_raise(1)
        self.assertEqual(self.my_employee.salary,10001)

unittest.main()