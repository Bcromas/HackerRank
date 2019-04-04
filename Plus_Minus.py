#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    arr_len = len(arr)
    arr_neg = []
    arr_pos = []
    arr_zero = []
    for i in arr:
        if i == 0:
            arr_zero.append(i)
        elif i > 0:
            arr_pos.append(i)
        else:
            arr_neg.append(i)

    print(round((len(arr_pos)/arr_len),6))
    print(round((len(arr_neg)/arr_len),6))
    print(round((len(arr_zero)/arr_len),6))

if __name__ == '__main__':
    # n = int(input())

    # arr = list(map(int, input().rstrip().split()))
    arr = [3,-1,0,0,988,-89217298,-54,0,0]

    plusMinus(arr)