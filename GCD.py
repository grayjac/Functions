#!/usr/bin/env python


# ME499-S20 Python Lab 1 Problem 4
# Programmer: Jacob Gray
# Last Edit: 4/6/2020


from math import gcd as math_gcd
from random import seed
from random import random
from random import randrange


def gcd(a, b):
    """
    Calculates and returns the greatest common divisor of two numbers a and b.
    :param a: Integer a.
    :param b: Integer b.
    :return: Greatest common divisor of two numbers a and b.
    """
    n = 1  # Intermediate variable
    rem = a % b  # Remainder of a / b
    ints = [a, b]  # Integers a and b

    while rem != 0:
        ints.append(rem)
        n += 1
        rem = ints[n - 1] % ints[n]
        ints.append(rem)
        if rem == 0:
            break

    return ints[n]


# Testing GCD function
if __name__ == "__main__":
    seed()  #generate random seed off system clock

    for i in range(0, 999):
        a = randrange(0, 99999)
        b = randrange(0, 99999)
        self.assetEqual(a, b)  # Compares two integers, returns value error if false







