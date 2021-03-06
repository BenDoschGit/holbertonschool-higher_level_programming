#!/usr/bin/python3
"""Module contains a class Square
"""


class Square:
    """A class with information about a square
    """

    def __init__(self, size):
        """initialization of function
        Args:
            size (int): Size of the square.
        """

        self.__size = size

if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)
