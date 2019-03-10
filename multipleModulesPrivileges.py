"""
Part of problem 9-12 of Python Crash Course
"""


class Privileges:
    def __init__(self):
        self.privileges = [
            'can add post',
            'can delete post',
            'can ban user',
        ]

    def show_privileges(self):
        print("You have the following privileges:")
        for privilege in self.privileges:
            print(privilege)

