2#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    # print(a, b)
    a_score = 0
    b_score = 0
    
    # if a[0] > b[0]:
    #     a_score += 1
    # else:
    #     b_score += 1

    # if a[1] > b[1]:
    #     a_score += 1
    # else:
    #     b_score += 1

    # if a[2] > b[2]:
    #     a_score += 1
    # else:
    #     b_score += 1

    # return [a_score, b_score]

    for a1,b1 in zip(a,b):
        if a1 == b1:
            continue
        elif a1 > b1:
            a_score += 1
        else:
            b_score += 1

    return [a_score, b_score]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # a = list(map(int, input().rstrip().split()))
    a = [7,22,2]

    # b = list(map(int, input().rstrip().split()))
    b = [8,23,4]

    result = compareTriplets(a, b)
    print(result)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()