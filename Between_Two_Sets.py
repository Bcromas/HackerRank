#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    # min_a = min(a)
    # max_a = max(a)

    # min_b = min(b)
    # max_b = max(b)

    # min_both = min(min_a, min_b)
    # max_both = max(max_a, max_b)

    # print(min_both, max_both)

    for i in a:
        for j in range(100):
            print(i, j)


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
    # print(total)

    # f.write(str(total) + '\n')

    # f.close()
