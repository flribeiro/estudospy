#!/bin/python3

import os
import sys


def separaIndices(frases):
    output = ''
    for i in range(len(frases)):
        ipar = ''
        iimpar = ''
        for c in range(len(frases[i])):
            if c % 2 == 0:
                ipar += frases[i][c]
            else:
                iimpar += frases[i][c]
        output += '{} {}\n'.format(ipar, iimpar)
    return output


if __name__ == '__main__':
    ent = int(input())
    
    # frases = list(map(str, input().rstrip().split())) 
    frases = []
    
    for i in range(ent):
        frases.append(input())
    
    print(separaIndices(frases))