#!/usr/bin/env python3
"""
This module defines an abstract class Shape and its subclasses.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for geometric shapes."""

    @abstractmethod
    def area(self):
        """Abstract method to calculate area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate perimeter."""
        pass


class Circle(Shape):
    """Represents a circle, inherits from Shape."""

    def __init__(self, radius):
        """Initializes the circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculates the area of the circle."""
        return self.radius**2 * math.pi

    def perimeter(self):
        """Calculates the perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Represents a rectangle, inherits from Shape."""

    def __init__(self, width, height):
        """Initializes the rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculates the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculates the perimeter of the rectangle."""
        return (self.width + self.height) * 2


def shape_info(shape):
    """
    Prints the area and perimeter of a shape.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")