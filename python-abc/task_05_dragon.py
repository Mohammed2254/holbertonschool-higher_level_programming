#!/usr/bin/env python3
"""
This module defines a Dragon class that inherits from SwimMixin and FlyMixin.
"""


class SwimMixin:
    """Mixin class that adds swimming capability."""

    def swim(self):
        """Prints that the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class that adds flying capability."""

    def fly(self):
        """Prints that the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Represents a Dragon that can swim and fly using mixins.
    """

    def roar(self):
        """Prints that the dragon roars."""
        print("The dragon roars!")