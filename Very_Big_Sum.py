#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    tally = 0
    for i in ar:
        tally += i

    return tally

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # ar_count = int(input())

    # ar = list(map(int, input().rstrip().split()))
    ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

    result = aVeryBigSum(ar)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()