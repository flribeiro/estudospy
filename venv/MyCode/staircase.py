import os
import sys

#
# Complete the staircase function below.
#
def staircase(n):
    degrau = 1
    for i in range(n-1, -1, -1):
        print(' ' * i, end='')
        print('#' * (n-i))
    
    
if __name__ == '__main__':
    n = int(input())

    staircase(n)