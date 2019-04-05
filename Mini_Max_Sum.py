#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    mini = sum(arr[:4])
    max = sum(arr[1:])
    print(mini, max)

if __name__ == '__main__':
    # arr = list(map(int, input().rstrip().split()))
    arr = [43,8,2,9,300]

    miniMaxSum(arr)
