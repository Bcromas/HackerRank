#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if 'pm' in s.lower():
        s_replace = s.replace('PM','')
        s_split = s_replace.split(':')
        if int(s_split[0])+12 == 24:
            mil_hour = '12'
        else:
            mil_hour = int(s_split[0])+12
        mil_min = s_split[1]
        mil_sec = s_split[2]
        mil_time = str(mil_hour)+':'+mil_min+':'+mil_sec
    elif 'am' in s.lower():
        s_replace = s.replace('AM','')
        s_split = s_replace.split(':')
        if int(s_split[0]) == 12:
            mil_hour = '00'
        else:
            mil_hour = s_split[0]
        mil_min = s_split[1]
        mil_sec = s_split[2]
        mil_time = str(mil_hour)+':'+mil_min+':'+mil_sec
    return mil_time

if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()
    # s = '07:05:45PM'
    # s = '07:05:45PM'
    # s = '12:45:54PM' #expected output: 12:45:54
    s = '12:40:22AM' #expected output: 00:40:22

    result = timeConversion(s)
    print(result)

    # f.write(result + '\n')

    # f.close()