"""
Problem 9-5 of Python Crash Course
"""


class User:

    def __init__(self, first_name, last_name, age, sex,):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = 0

    def describe_user(self):
        print("Info:")
        print(self.first_name)
        print(self.last_name)
        print(self.age)
        print(self.sex)

    def greet_user(self):
        print("Hello, " + self.first_name + ' ' +
              self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
