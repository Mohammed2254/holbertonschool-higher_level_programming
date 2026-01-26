#!/usr/bin/python3
"""Define an empty class Rectangle"""


class Rectangle:
    """a reactangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """main"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """reading func"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting func"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """reading dunv"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting func"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calc area"""
        return self.__height * self.__width

    def perimeter(self):
        """perimeter func"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """for anyone"""
        if self.width == 0 or self.height == 0:
            return ""
        TheRec = []
        for j in range(self.height):
            TheRec.append(str(self.print_symbol) * self.width)
        return "\n".join(TheRec)

    def __repr__(self):
        """for dev"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """a comment for this func"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compare"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        if rect_1.area() > rect_2.area():
            return rect_1
        return rect_1
