"""
Problem 9-3 of Python Crash Course
"""


class user:

    def __init__(self, first_name, last_name, age, sex,):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex

    def describe_user(self):
        print("Info:")
        print(self.first_name)
        print(self.last_name)
        print(self.age)
        print(self.sex)

    def greet_user(self):
        print("Hello, " + self.first_name + ' ' +
              self.last_name)


if __name__ == '__main__':
    me = user('tyler', 'henson', '27', 'm')
    me.greet_user()
    me.describe_user()

    him = user('anthony', 'm', '27', 'm')
    him.greet_user()
    him.describe_user()
