#!/usr/bin/python3
"""This module contains solutions to Minimum Operations interview
   questions
"""


def minOperations(n):
    """this function takes a number n and returns the minimum number
    of operations to result in n
    """
    if n <= 1:
        return 0
    # first get the prime numbers of n
    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    # the sum of the prime numbers is the minimum operations
    return sum(factors)
