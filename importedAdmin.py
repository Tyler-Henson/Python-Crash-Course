"""
Problem 9-11 of Python Crash Course
"""

from privileges import Admin #Privileges
#import loginAttempts2 as lA2


if __name__ == '__main__':
    my_account = Admin('tyler', 'henson', 27, 'm')
    my_account.privileges.show_privileges()

