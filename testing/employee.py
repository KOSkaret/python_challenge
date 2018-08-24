class Employee():

    def __init__(self, first,last,salary):
        """ Document an employees information """
        self.first_name = first
        self.last_name = last
        self.salary = salary
    
    def give_raise(self, increase=5000):
        """ A function to raise the salary of the employee. """
        self.salary += increase


