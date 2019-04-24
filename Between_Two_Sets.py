#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    print('a ',a)
    print('b ',b)

if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')

    # nm = input().split()

    # n = int(nm[0])
    n = 2

    # m = int(nm[1])
    m = 3

    # a = list(map(int, input().rstrip().split()))
    a = [2,4]

    # b = list(map(int, input().rstrip().split()))
    b = [16,32,96]

    total = getTotalX(a, b)

    # f.write(str(total) + '\n')

    # f.close()
