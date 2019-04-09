#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    new_grades_arr = []
    for i in grades:

        next_mul_5 = i + (5-(i%5))
        diff = next_mul_5-i
        
        if i < 38:
            new_grade = i
            new_grades_arr.append(new_grade)
        else:
            if diff < 3:
                new_grade = next_mul_5
                new_grades_arr.append(new_grade)
            else:
                new_grade = i
                new_grades_arr.append(new_grade)
    return new_grades_arr
    

if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())

    # grades = []
    grades = [73,67,3,100,5,99,38,7,33]

    # for _ in range(n):
        # grades_item = int(input())
        # grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)

    # f.write('\n'.join(map(str, result)))
    # f.write('\n')

    # f.close()