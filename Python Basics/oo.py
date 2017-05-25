import random
# Make a class

# class Thief:
#     sneaky = True
#
# Kenneth = Thief()
# Kenneth.sneaky = False # Changes the Kenneth instance of the class to have sneaky as false

# Methods

class Thief:
    sneaky = True

    def __init__(self, name, sneaky=True, **kwargs): # Initialises it
        self.name = name
        self.sneaky = sneaky

        for key, value in kwargs.items():
            setattr(self, key, value) # Allows us to add extra arguments

    def pickpocket(self):
        # print("Called by {}".format(self))
        return self.sneaky and bool(random.randint(0,1))


    def hide(self, light_level):
        return self.sneaky == True and light_level < 10

Kenneth = Thief("Kenneth", False, scare=None, favourite_weapon="Wit")
Kenneth.favourite_weapon
