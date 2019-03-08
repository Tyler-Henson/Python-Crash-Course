"""
Problem 9-6 of Python Crash Course
"""
from numberServed2 import *


class IcecreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors=[]):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):

        if self.flavors:
            print("We have the following flavors:")
            for flavor in self.flavors:
                print(flavor)
        else:
            print("Sorry, we don't have any flavors at all!")


if __name__ == '__main__':
    flavors = ['vanilla', 'chocolate', 'strawberry']
    my_shop = IcecreamStand("tix-ice", 'ice-cream shop')
    my_shop.display_flavors()

    my_shop = IcecreamStand("tix-ice", 'ice-cream shop', flavors)
    my_shop.display_flavors()
    my_shop.describe_restaurant()
