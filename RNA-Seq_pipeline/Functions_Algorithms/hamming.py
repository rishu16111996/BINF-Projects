#!/usr/bin/env python3
# hamming.py

import sys

def hamming(str1, str2):
    '''Returns the Hamming distance between two DNA string
    '''
    score = 0
    for i in range(0, len(str1)):
        if str1[i] == str2[i]:
            pass
        else:
            score += 1
    #return sum(a!=b for a,b in zip(str1, str2))
    return score

if __name__ == "__main__":
    arg_count = len(sys.argv) - 1
    if arg_count < 2:
        raise Exception("This script require 2 arguments")
 
    str1 = sys.argv[1]
    str2 = sys.argv[2]

    if len(str1) != len(str2):
        raise Exception("Size of two DNA string should be same")

    score = hamming(str1, str2)

    print("{}\t{}\t{}".format(str1, str2, score))





