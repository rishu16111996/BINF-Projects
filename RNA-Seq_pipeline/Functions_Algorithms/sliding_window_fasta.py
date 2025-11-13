#!/usr/bin/env python3
# sliding_window_fasta.py

import sys
import re

def sliding_window(k, kmer):
    '''Returns the list of kmer available in string passed
    '''
    kmers = []
    end = len(kmer) - k + 1
    for start in range(0, end):
        kmers.append(kmer[start:start + k])
    return kmers

def gc_content(dna):
    '''Returns the GC content in given kmer
    '''
    dna = dna.lower()
    gc = 0
    for nucleotide in dna:
        if nucleotide in ['g', 'c']:
            gc += 1
    return gc/len(dna)

if __name__ == "__main__":
    arg_count = len(sys.argv) - 1
    if arg_count < 2:
        raise Exception("This script requires at least 2 arguments")
    elif int(sys.argv[1]) <= 0:
        sys.exit("Value of K must be greater then Zero")
                                  
    k = int(sys.argv[1])
    file_name = sys.argv[2]
 
    kmer = ""
    # open file and get the sequence in single string along with header
    with open(file_name) as genome:
        for line in genome:
            line = line.strip()
            if len(line) < 1:
                continue
            elif re.match('^>', line):
               print(line)
               kmer = ""
            else:
                kmer += line
                
    for km in sliding_window(k, kmer):
        res = 0
        res = gc_content(km)
        print("{}\t{}".format(km, round(res,2)))





