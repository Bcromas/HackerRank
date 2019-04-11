#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    kanga_start_1 = x1
    kanga_start_2 = x2

    kanga_jump_1 = v1
    kanga_jump_2 = v2

    jumps_1 = []
    jumps_2 = []

    result_flag = 'NO'

    for i in range(10000):
        jump_1 = kanga_start_1+(kanga_jump_1*i)
        jumps_1.append(jump_1)

        jump_2 = kanga_start_2+(kanga_jump_2*i)
        jumps_2.append(jump_2)

        result = zip(jumps_1,jumps_2)
    for i in result:
        if i[0] == i[1]:
            result_flag = 'YES'
        # print(i, result_flag)

    return result_flag

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # x1V1X2V2 = input().split()

    # x1 = int(x1V1X2V2[0])
    x1 = 63

    # v1 = int(x1V1X2V2[1])
    v1 = 8

    # x2 = int(x1V1X2V2[2])
    x2 = 94

    # v2 = int(x1V1X2V2[3])
    v2 = 3

    result = kangaroo(x1, v1, x2, v2)
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
