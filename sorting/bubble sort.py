#https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    swaps = 0
    n = 0
    length = len(a) 
    
    for i in range(length - 1):
        for j in range(0, length - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]  # Swap elements
                swaps += 1
    
    first = a[0]
    last = a[len(a)-1]
    first_element = f"First Element: {first}"
    Last_element = f"Last Element: {last}"
    answer = f"Array is sorted in {swaps} swaps."
    print (answer)
    print (first_element)
    print (Last_element)
    return


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
