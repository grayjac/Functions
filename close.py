#!/usr/bin/env python


# ME499-S20 Python Lab 1 Problem 2
# Programmer: Jacob Gray
# Last Edit: 4/6/2020


def close(number_one, number_two, number_three):
    """
    Returns True if the absolute difference between the first two numbers is less than the third number.

    :param number_one: Can be an integer or floating point.
    :param number_two: Can be an integer or floating point.
    :param number_three: Can be an integer or floating point.
    :return: True or False.
    """

    if abs(number_one - number_two) < number_three:
        a = True  # Set intermediate variable 'a' True
    else:
        a = False  # Set intermediate variable 'a' False

    return a



