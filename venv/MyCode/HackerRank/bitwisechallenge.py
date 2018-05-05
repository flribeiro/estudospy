#!/bin/python3

import sys


def all_bitwise(n, k):
    maior = 0
    for B in range(1, n + 1):
        for A in range(1, B):
            bw = A&B
            if bw > maior and bw < k:
                maior = bw
    return maior

def encontraResp(bw, k):
    resp = 0
    for i in bw:
        if i > resp and i < k:
            resp = i

    return resp

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    bw = all_bitwise(n, k)
    #resp = encontraResp(bw, k)
    print(bw)
    
