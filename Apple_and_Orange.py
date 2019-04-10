#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_hit_house = 0
    oranges_hit_house = 0

    for i in apples:
        i_from_tree = i+a
        if i_from_tree >= s and i_from_tree <= t:
            apples_hit_house += 1

    for i in oranges:
        i_from_tree = i+b
        if i_from_tree >= s and i_from_tree <= t:
            oranges_hit_house += 1

    # return '{}\n{}'.format(apples_hit_house, oranges_hit_house)
    print('{}\n{}'.format(apples_hit_house, oranges_hit_house))

if __name__ == '__main__':
    # st = input().split()

    # s = int(st[0]) #s: integer, starting point of Sam's house location.
    s = 7

    # t = int(st[1]) #t: integer, ending location of Sam's house location.
    t = 10

    # ab = input().split()

    # a = int(ab[0]) #a: integer, location of the Apple tree.
    a = 4

    # b = int(ab[1]) #b: integer, location of the Orange tree.
    b = 12

    # mn = input().split()

    # m = int(mn[0]) 

    # n = int(mn[1])

    # apples = list(map(int, input().rstrip().split())) #contains m space-separated integers denoting the respective distances that each apple falls from point a.
    apples = [2,3,-4]

    # oranges = list(map(int, input().rstrip().split())) #contains n space-separated integers denoting the respective distances that each orange falls from point b.
    oranges = [3,-2,-4]

    print(countApplesAndOranges(s, t, a, b, apples, oranges))
