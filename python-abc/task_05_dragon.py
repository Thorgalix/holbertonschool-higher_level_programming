#!/usr/bin/python3
"""
Module demonstrating the use of mixins to give a Dragon
the ability to swim, fly, and roar.
"""


class SwimMixin:
    """
    Mixin class that provides swimming capability.

    This class is intended to be combined with other classes
    to give them the ability to swim.
    """
    def swim(self):
        """
        Prints a message indicating that the creature swims.

        This method can be used by any class that inherits from SwimMixin.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class that provides flying capability.

    This class is intended to be combined with other classes
    to give them the ability to fly.
    """
    def fly(self):
        """
        Prints a message indicating that the creature flies.

        This method can be used by any class that inherits from FlyMixin.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon that can swim, fly, and roar.

    Inherits behavior from SwimMixin and FlyMixin to gain
    swimming and flying abilities. Additionally, it has its
    own method roar to produce a roaring sound.
    """
    def roar(self):
        """
        Prints a message indicating that the dragon roars.

        This method is specific to the Dragon class.
        """
        print("The dragon roars!")


if __name__ == "__main__":
    draco = Dragon()
    draco.swim()
    draco.fly()
    draco.roar()
