#!/usr/bin/python3
"""This module contains solutions to Minimum Operations interview
   questions
"""


def minOperations(n):
    """this function takes a number n and returns the minimum number
    of operations to result in n
    """
    # first get the prime numbers of n
    if n == 1:
        return 0
    operations = 0
    divisor = 2
    while n > 1:
        if n % 2 == 0:
            operations += divisor
            n //= divisor
        else:
            divisor += 1
    return operations
