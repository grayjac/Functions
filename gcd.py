#!/usr/bin/env python


# ME499-S20 Python Lab 1 Problem 4
# Programmer: Jacob Gray
# Last Edit: 4/6/2020


from math import gcd as math_gcd
from random import randint


def gcd(a, b):
    """
    Calculates and returns the greatest common divisor of integers a and b. Raises TypeError if inputs a and b
    aren't integers.
    :param a: Integer a.
    :param b: Integer b.
    :return: Greatest common divisor of integers a and b.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError  # Raises TypeError if a or b isn't an integer

    n = 1  # Intermediate variable for indexing through list of integers
    rem = a % b  # Remainder of a / b
    ints = [a, b]  # Integers list

    while rem != 0:
        ints.append(rem)  # Append integer list with the remainder of a / b if it's not zero
        n += 1  # Progress index
        rem = ints[n - 1] % ints[n]  # Find the remainder of the next two integers in the list
        if rem == 0:
            break

    return abs(ints[n])


def compare_test(a, b):
    """
    Compares integers a and b and raises ValueError if they're not equal.
    :param a: Integer.
    :param b: Integer.
    :return: Raises ValueError if integers a and b are not equal, does nothing otherwise.
    """
    if a != b:
        raise ValueError


# Testing and comparing both GCD functions thru 1000 pairs of random integers of range -10,000 thru 10,000
if __name__ == "__main__":
    for i in range(0, 999):
        rand_integer_a = randint(-10000, 10000)
        rand_integer_b = randint(-10000, 10000)
        math_gcd_test = math_gcd(rand_integer_a, rand_integer_b)  # GCD function from math module
        my_gcd_test = gcd(rand_integer_a, rand_integer_b)  # My GCD function
        compare_test(math_gcd_test, my_gcd_test)  # Comparing two GCD functions
    else:
        print('No errors found')  # Prints if GCD functions pass all comparison tests
