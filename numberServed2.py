"""
Problem 9-4 of Python Crash Course
"""


class Restaurant:
    """A simple restaurant model"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initiate the attributes name and cuisine"""
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints information about the restaurant"""
        print(self.name.title() + " serves " + self.cuisine.title() + ' food.')

    def open_restaurant(self):
        """Simulates opening the restaurant"""
        print(self.name.title() + " is open!")

    def set_number_served(self, number):
        """Set initial value for attribute"""
        self.number_served = number

    def increment_number_served(self, number):
        """increment attribute by an amount"""
        self.number_served += number


if __name__ == '__main__':
    my_restaurant = Restaurant("pizza hut", "pizza-like")
    my_restaurant.describe_restaurant()
    my_restaurant.open_restaurant()
