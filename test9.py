class Cat():
    """Simple model of a cat"""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age
        self.ears = Ears()

    def sit(self):
        """Simulate the cat sitting"""
        print(self.name.title() + ' is now sitting.')

    def lick_self(self):
        """Simulate the cat licking itself"""
        print(self.name.title() + " is licking itself.")


class Kitten(Cat):
    def __init__(self, name, age):
        super().__init__(name,age)
        self.smol = True

    def sit(self):
        """Simulate the kitten sitting"""
        print(self.name.title() + ', a kitten, is now sitting.')


class Ears():
    def __init__(self, hearing_ability=True):
        self.hearing_ability = hearing_ability

    def describe_hearing_ability(self):
        print("This cat has " + str(self.hearing_ability) + " hearing.")


class mech():
    """A simple battle mech"""

    def __init__(self, model, height):
        """Initialize model and height attributes"""
        self.model = model
        self.height = height


    def shoot(self):
        """Simulate the mech firing it's main gun"""
        print("ratatatatta!")


    def aim_gun(self):
        """Simulate the mech performing aiming calculation"""
        print(self.model.title() + " pattern gun fires from height- " +
              self.height)
        print("aiming...")


if __name__ == '__main__':
    '''
    my_cat = Cat('houdini', 8)
    my_mech = mech('ragnarok', '12m')
    my_ear = Ears()
    my_ear.describe_hearing_ability()

    # my_cat.sit()
    # my_cat.lick_self()

    # my_mech.aim_gun()
    # my_mech.shoot()

    my_kitten = Kitten("sassy", 1)
    my_kitten.ears.hearing_ability = False
    my_kitten.lick_self()
    my_kitten.sit()
    if my_kitten.smol:
        print(my_kitten.name + " is smol")
    my_kitten.ears.describe_hearing_ability()
    '''


    from car import Car as c
    my_new_car = c('audi', 'a4', 2016)
    print(my_new_car.get_descriptive_name())

    my_new_car.odometer_reading = 23
    my_new_car.read_odometer()
