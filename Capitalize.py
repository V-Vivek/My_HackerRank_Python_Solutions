# Question: https://www.hackerrank.com/challenges/capitalize/problem

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    for i in s.split():
        s = s.replace(i,i.capitalize()) # Replace each word with captitalized word
    return s
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
