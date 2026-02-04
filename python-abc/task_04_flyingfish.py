#!/usr/bin/python3
"""
Module that defines Fish, Bird, and FlyingFish classes
to illustrate multiple inheritance and method resolution order.
"""


class Fish:
    """Represents a fish with swimming behavior and habitat."""
    def swim(self):
        """Print that the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Print the habitat of the fish."""
        print("The fish lives in water")


class Bird:
    """Represents a bird with flying behavior and habitat."""
    def fly(self):
        """Print that the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Print the habitat of the bird."""
        print("The bird lives in the sky")


class FlyingFish(Bird, Fish):
    """
    Represents a flying fish that can both swim and fly.
    Demonstrates multiple inheritance and method overriding.
    """

    def fly(self):
        """Print that the flying fish is soaring."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print that the flying fish is swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print the dual habitat of the flying fish."""
        print("The flying fish lives both in water and the sky!")
