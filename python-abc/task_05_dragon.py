#!/usr/bin/python3
"""Demonstrates mixins with SwimMixin, FlyMixin, and Dragon."""

# --- Mixins ---
class SwimMixin:
    """Provides swimming ability."""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Provides flying ability."""

    def fly(self):
        print("The creature flies!")


# --- Dragon Class ---
class Dragon(SwimMixin, FlyMixin):
    """Dragon class that can swim and fly."""

    def roar(self):
        print("The dragon roars!")


# --- Testing ---
if __name__ == "__main__":
    draco = Dragon()

    print("Testing dragon abilities:")
    draco.swim()   # The creature swims!
    draco.fly()    # The creature flies!
    draco.roar()   # The dragon roars!
