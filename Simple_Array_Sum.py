import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    # print(ar)
    tally = 0
    for i in ar:
        print(i)
        tally += i
    print(tally)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # ar_count = int(input())
    ar_count = 3

    # ar = list(map(int, input().rstrip().split()))
    ar = [4,5,8]

    result = simpleArraySum(ar)

    # fptr.write(str(result) + '\n')

    # fptr.close()