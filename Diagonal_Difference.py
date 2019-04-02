#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    L_R_iteration = 0 #start at first index
    R_L_iteration = -1 #start at last index
    left_right_sum = 0
    right_left_sum = 0
    for i in arr:
        left_right_sum += i[L_R_iteration]
        right_left_sum += i[R_L_iteration]
        # print (i[L_R_iteration], 'left_right_sum =', left_right_sum,'\n',
        #     i[R_L_iteration], 'right_left_sum =', right_left_sum, '\n\n')
        L_R_iteration += 1 #step to next index
        R_L_iteration -= 1 #step to one index prior
    tally = left_right_sum - right_left_sum
    return abs(tally)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())

    # arr = []

    # for _ in range(n):
        # arr.append(list(map(int, input().rstrip().split())))
    arr = [[3,11,2,4,22],
            [3,10,4,5,6],
            [3,3,10,8,-12],
            [3,5,44,5,7],
            [3,0,-13,13,777],
            ]

    result = diagonalDifference(arr)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()