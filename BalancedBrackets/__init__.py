#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    if len(s) % 2 == 1:
        return 'NO'

    brackets = ['()', '[]', '{}']
    while any(char in s for char in brackets):
        for bracket in brackets:
            s = s.replace(bracket, '')

    if len(s) == 0:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    print(isBalanced('{[(])}'))
    sys.exit()
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
