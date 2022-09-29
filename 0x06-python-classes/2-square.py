#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 15:53:15 2022
"""


class Square(object):
    """Sqaure class that define a square
    """

    def __init__(self, size=0):
        """Square init method.
        Args:
            size (int):  The size of a square
        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
