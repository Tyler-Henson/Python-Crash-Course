"""
Problem 9-2 of Python Crash Course
"""
#from restaurant import *
#import restaurant
r = __import__("restaurant")

if __name__ == '__main__':
    taco = r.Restaurant('taco bell', 'tex-mex')
    pizza = r.Restaurant('Dominos', 'sorta-italian')
    burger = r.Restaurant("burger king", 'burger')

    # after importing the class we dont need to refrence to other file it seems
    taco.describe_restaurant()
    pizza.describe_restaurant()
    burger.describe_restaurant()

