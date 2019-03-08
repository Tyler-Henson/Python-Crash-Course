"""
Problem 9-4 of Python Crash Course
"""
# Importing Restaurant class (includes methods and attributes
from numberServed2 import *


if __name__ == '__main__':
    my_taco_bell = Restaurant('taco bell', 'tex-mex')

    print(my_taco_bell.number_served)
    my_taco_bell.set_number_served(100)
    my_taco_bell.increment_number_served(10)
    print(my_taco_bell.number_served)

    my_taco_bell.describe_restaurant()
