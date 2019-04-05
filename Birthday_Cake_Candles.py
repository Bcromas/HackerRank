#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    max_candle = max(ar)
    num_candles = ar.count(max_candle)
    return num_candles

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # ar_count = int(input())

    # ar = list(map(int, input().rstrip().split()))
    ar = [3,9,9,9]

    result = birthdayCakeCandles(ar)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
