"""
Problem 9-9 of Python Crash Course
"""


class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Returns a formated name of car"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """prints odometer reading"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Updates odometer to the passed parameter"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


class Battery():
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size=70):
        """initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Describes battery's specifications"""
        print('This car has a ' + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """print a statement about therange this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """If battery is less than 85-kWh upgrades it"""
        if self.battery_size < 85:
            message = "Upgrading " + str(self.battery_size) +\
                      " size battery to " + str(85)
            print(message)
            self.battery_size = 85


class ElectricCar(Car):
    """Represents aspects of the car unique to electric vehicles"""

    def __init__(self, make, model, year):
        """initialize attributes of parent class"""
        super().__init__(make, model, year)
        self.battery = Battery()


if __name__ == '__main__':
    my_tesla = ElectricCar('tesla', 'model s', 2016)
    print(my_tesla.get_descriptive_name())
    my_tesla.battery.describe_battery()
    my_tesla.battery.get_range()
    my_tesla.battery.upgrade_battery()
    my_tesla.battery.get_range()





