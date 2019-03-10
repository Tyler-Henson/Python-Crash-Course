"""
Part of problem 9-12 of Python Crash Course
"""
import loginAttempts2 as lA2
from multipleModulesPrivileges import Privileges


class Admin(lA2.User):
    def __init__(self, first_name, last_name, age, sex,):
        super().__init__(first_name, last_name, age, sex)
        self.privileges = Privileges()

