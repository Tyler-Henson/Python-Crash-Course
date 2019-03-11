"""
Problem 9-14 of Python Crash Course
"""
from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1,self.sides))


if __name__ == '__main__':
    print('d6')
    my_die = Die()
    for _ in range(0, 10):
        my_die.roll_die()

    print('d10')
    d10 = Die(10)
    for _ in range(0, 10):
        d10.roll_die()

    print('d20')
    d20 = Die(20)
    for _ in range(0, 10):
        d20.roll_die()
