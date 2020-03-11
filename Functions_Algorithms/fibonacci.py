#!/usr/bin/env python3
# fibonacci.py

import sys

def population(n,k):
    '''Returns the population growth of organism on certain day
    '''
    sum1 = 0
    mature = 0
    unmature = 0
    mature1 = 0
    for i in range(0,n):
        if i == 0:
            sum1 = 1
        elif i == 1:
            sum1 = 1
            mature = 1
        else:
            sum1 = mature + (mature*k) + unmature
            mature1 = mature
            mature = unmature + mature
            unmature = mature1 * k
            # off = population[i-2] * k
            # population[i] = population[i-1] - off
    return(sum1)


if __name__ == "__main__":

    arg_count = len(sys.argv) - 1
    if arg_count < 2:
        raise Exception("This script requires 2 arguments: ")

    n = int(sys.argv[1])
    k = int(sys.argv[2])

    if n > 1000 or k > 1000:
        raise Exception("Population size and Days length should be less then 1000")

    # Passing argument along with function to get population growth on certain day
    popu = population(n, k)

    print("{}".format(popu))
    #print("{:,}".format(popu))
