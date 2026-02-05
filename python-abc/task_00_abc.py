#!/usr/bin/python3
"""Defines an abstract Animal class and its subclasses Dog and Cat."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        pass


class Dog(Animal):
    """Dog class."""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat class."""

    def sound(self):
        return "Meow"
