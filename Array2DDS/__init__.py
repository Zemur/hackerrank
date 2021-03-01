#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hourglassSum(arr):
    hourglass_sums = []

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if j+3 <= len(arr[i]) and i+2 <= len(arr)-1:
                hourglass_sums.append(sum([sum(arr[i][j:j+3]), arr[i+1][j+1]], sum(arr[i+2][j:j+3])))
    print(max(hourglass_sums))
    return max(hourglass_sums)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
