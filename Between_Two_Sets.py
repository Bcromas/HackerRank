#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    
    #generate lists of ints that are products of an element in array a 
    list_X = []
    for i in a:
        list_i = []
        for j in range(1,101):
            list_i.append(i*j)
        list_X.append(list_i)

    #idea is to iterate through lists in list_X & find intersection of individual list members
    # for i in list_X:
        # intersect_i = set(i).intersection(i+1)
        

    # intersect = set(list_a).intersection(list_b)
    # intersect_list = list(intersect)
    # intersect_list_sorted = sorted(intersect_list)
    # print(intersect_list_sorted)

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

    # total = getTotalX(a, b)
    # print(total)

    # f.write(str(total) + '\n')

    # f.close()
