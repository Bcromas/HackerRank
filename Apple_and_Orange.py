#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    print(s,t,a,b,apples,oranges)

if __name__ == '__main__':
    # st = input().split()

    # s = int(st[0]) #s: integer, starting point of Sam's house location.
    s = 7

    # t = int(st[1]) #t: integer, ending location of Sam's house location.
    t = 11

    # ab = input().split()

    # a = int(ab[0]) #a: integer, location of the Apple tree.
    a = 5

    # b = int(ab[1]) #b: integer, location of the Orange tree.
    b = 15

    # mn = input().split()

    # m = int(mn[0]) 

    # n = int(mn[1])

    # apples = list(map(int, input().rstrip().split())) #contains m space-separated integers denoting the respective distances that each apple falls from point a.
    apples = [-2,2,1]

    # oranges = list(map(int, input().rstrip().split())) #contains n space-separated integers denoting the respective distances that each orange falls from point b.
    oranges = [5,-6]

    countApplesAndOranges(s, t, a, b, apples, oranges)