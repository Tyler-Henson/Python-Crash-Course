"""
Problem 9-10 of Python Crash Course
"""

from numberServed2 import Restaurant as R

if __name__ == '__main__':
    my_restaurant = R('pizza place', 'pizza')
    my_restaurant.describe_restaurant()
    my_restaurant.set_number_served(0)
    my_restaurant.increment_number_served(10)
    print(my_restaurant.number_served)



