#!/usr/bin/env python


# ME499-S20 Python Lab 1 Problem 1
# Programmer: Jacob Gray
# Last Edit: 4/5/2020


from math import pi  # Import pi function from math library


def cylinder_volume(radius, height):
    """
    Calculates and returns the volume of a cylinder.

    :param radius: The radius of the cylinder.
    :param height: The height of the cylinder.
    :return: The volume of the cylinder.
    """

    # If the radius or height is negative, then raise a ValueError. This will force the program to stop, and the user
    # to fix the argument parameters.
    if radius < 0:
        raise ValueError
    elif height < 0:
        raise ValueError

    # If the program runs to here and the arguments are valid, calculate and return the cylinder volume.
    return pi * radius ** 2 * height


def torus_volume(inner_radius, outer_radius):
    """
    Calculates and returns the volume of a torus.

    :param inner_radius: The inner radius of the torus.
    :param outer_radius: The outer radius of the torus.
    :return: The volume of the torus.
    """

    # If the inner radius or outer radius is negative, then raise a ValueError. This will force the program to stop,
    # and the user to fix the argument parameters.
    if inner_radius < 0:
        raise ValueError
    elif outer_radius <= inner_radius:
        raise ValueError

    # If the program runs to here and the argument are valid, calculate and return the torus volume.
    return 2 * pi ** 2 * inner_radius * (outer_radius - inner_radius)

