"""
 Sample modified from CS5500, Mike Shah

 A rectangle class
 Note that there is no constructor or destructor,
 so a default one will be created for us.
"""

from abc import ABC, abstractmethod


class Shape(ABC):

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @abstractmethod
    def set_values(self, width, height):
        pass

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def set_values(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        # Access private variables of the parent class
        return self._Shape__width * self._Shape__height


if __name__ == "__main__":
    # Create a rectangle object with initial values
    rect = Rectangle(3, 4)

    # Print out the area function
    print("area:", rect.area())
