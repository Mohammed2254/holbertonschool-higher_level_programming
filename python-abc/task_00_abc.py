#!/usr/bin/env python3
"""
This module defines an abstract class Animal and its subclasses Dog and Cat.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal."""

    @abstractmethod
    def sound(self):
        """Abstract method for the animal sound."""
        pass


class Dog(Animal):
    """Represents a Dog, inherits from Animal."""

    def sound(self):
        """Returns the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Represents a Cat, inherits from Animal."""

    def sound(self):
        """Returns the sound of a cat."""
        return "Meow"
