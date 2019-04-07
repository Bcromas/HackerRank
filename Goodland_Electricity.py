#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pylons function below.
def pylons(k, arr):
    print(k, arr)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nk = input().split()

    #n: the number of cities in Goodland
    # n = int(nk[0])
    n = 6

    #k: an integer that represents distribution range
    # k = int(nk[1])
    k = 2

    # arr: an array of integers that represent suitability as a building site
    # arr = list(map(int, input().rstrip().split()))
    arr = [0,1,1,1,1,0]

    result = pylons(k, arr)

    # fptr.write(str(result) + '\n')

    # fptr.close()