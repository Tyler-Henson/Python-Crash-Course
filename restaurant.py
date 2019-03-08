"""
Problem 9-1 of Python Crash Course
"""


class Restaurant:
    """A simple restaurant model"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initiate the attributes name and cuisine"""
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        """Prints information about the restaurant"""
        print(self.name.title() + " serves " + self.cuisine.title() + ' food.')

    def open_restaurant(self):
        """Simulates opening the restaurant"""
        print(self.name.title() + " is open!")


if __name__ == '__main__':
    my_restaurant = Restaurant("pizza hut", "pizza-like")
    my_restaurant.describe_restaurant()
    my_restaurant.open_restaurant()
