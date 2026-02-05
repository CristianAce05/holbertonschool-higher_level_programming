#!/usr/bin/python3
"""Demonstrates multiple inheritance with Fish, Bird, and FlyingFish."""

class Fish:
    """Fish class."""

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """Bird class."""

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish inherits from both Fish and Bird."""

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")


# --- Testing ---
if __name__ == "__main__":
    ff = FlyingFish()

    print("Testing methods:")
    ff.fly()      # The flying fish is soaring!
    ff.swim()     # The flying fish is swimming!
    ff.habitat()  # The flying fish lives both in water and the sky!

    print("\nMethod Resolution Order (MRO):")
    for cls in FlyingFish.mro():
        print(cls)
