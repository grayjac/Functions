#!/usr/bin/env python


# ME499-S20 Python Lab 1 Problem 4
# Programmer: Jacob Gray
# Last Edit: 4/6/2020


from math import gcd as math_gcd
from random import randint


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
        if rem == 0:
            break

    return ints[n]


def compare_test(a, b):
    """
    Compares integers a and b and raises ValueError if they're not equal.
    :param a: Integer.
    :param b: Integer.
    :return: Raises ValueError if integers a and b are not equal, does nothing otherwise.
    """
    if a != b:
        raise ValueError


# Testing my GCD function thru 1000 pairs of random integers of range 1 thru 10,000
if __name__ == "__main__":
    for i in range(0, 999):
        rand_integer_a = randint(0, 9999)
        rand_integer_b = randint(0, 9999)
        math_gcd_test = math_gcd(rand_integer_a, rand_integer_b)  # GCD function from math module
        my_gcd_test = gcd(rand_integer_a, rand_integer_b)  # My GCD function
        compare_test(math_gcd_test, my_gcd_test)  # Comparing two GCD functions
