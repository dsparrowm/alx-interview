#!/usr/bin/python3
"""This module contains solutions to Minimum Operations interview
   questions
"""


def minOperations(n):
    """this function takes a number n and returns the minimum number
    of operations to result in n
    """
    # first get the prime numbers of n
    if n <= 1:
        return 0
    dp = [float('inf')] * (n + 1)
    # Base case: No operations needed for n < 2
    dp[1] = 0
    
    # The outer loop iterates from 2 to n
    for i in range(2, n + 1):
        #  The inner loop iterates from 1 to i - 1
        # and checks if i is divisible by j.
        for j in range(1, i):
            if i % j == 0:
                # If it is, We update the minimum operations
                # using min(dp[i], dp[j] + i // j).
                dp[i] = min(dp[i], dp[j] + i // j)
    return dp[n]
