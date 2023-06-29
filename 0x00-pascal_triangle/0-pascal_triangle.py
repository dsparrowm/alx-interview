#!/usr/bin/pytho3
"""This module represents the pascal triangle of n numbers"""


def pascal_triangle(n):
    """function that returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    triangle = []
    for row_num in range(n):
        row = []
        for i in range(row_num + 1):
            if i == 0 or i == row_num:
                row.append(1)
            else:
                value = triangle[row_num - 1][i] + triangle[row_num - 1][i - 1]
                row.append(value)
        triangle.append(row)
    return triangle
