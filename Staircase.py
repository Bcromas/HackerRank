#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    num_steps = n
    iterator = 1
    spaces = (num_steps - 1)
    for i in range(num_steps):
        print('{}{}'.format(spaces*' ',iterator*'#'))
        iterator += 1
        spaces -= 1


if __name__ == '__main__':
    #n = int(input())
    n=9

    staircase(n)