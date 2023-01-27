#!/usr/bin/python3

"""function that returns a list of lists of integers representing the Pascal triangle"""

def pascal_triangle(n)
    """function that returns a list of lists of integers representing the Pascal triangle"""

    arr = []
    if (n <= 0):
        return arr
    arr.append([1])
    for i in range(n - 1):
        arr.append([1] + [arr[i][j] + arr[i][j + 1]
                    for j in range(len(arr[i]) - 1)] + [1])
    return arr
