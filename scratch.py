#!/usr/bin/env python


from math import gcd as math_gcd  # Import gcd from math library
from GCD import gcd as my_gcd  # Import my gcd program from GCD
from random import seed
from random import randint
from time import sleep


i = 1
seed(i)
a = randint(1, 1000)
b = randint(1, 1000)

for j in range(1000):
    print('math_gcd:', math_gcd(a, b))
    print('my_gcd', my_gcd(a, b))
    i += 1
    sleep(2)