"""
Problem 9-12 of Python Crash Course
"""
from multipleModulesAdmin import Admin

if __name__ == '__main__':
    my_account = Admin('tyler', 'henson', 27, 'm')
    my_account.privileges.show_privileges()