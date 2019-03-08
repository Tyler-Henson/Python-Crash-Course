"""
Problem 9-7 of Python Crash Course
"""

import loginAttempts2 as lA2

class Admin(lA2.User):
    def __init__(self, first_name, last_name, age, sex,):
        super().__init__(first_name, last_name, age, sex)
        self.privileges = [
            'can add post',
            'can delete post',
            'can ban user',
            ]

    def show_privileges(self):
        print("You have the following privileges:")
        for privilege in self.privileges:
            print(privilege)


if __name__ == '__main__':
    me = Admin('tyler', 'henson', 27, 'm')
    me.show_privileges()
    me.describe_user()
