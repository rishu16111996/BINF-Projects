#!/usr/bin/env python3
# BioPython_seqio.py

from Bio import SeqIO
import sys
import re
from Bio.SeqRecord import SeqRecord


if __name__ == "__main__":

    argsC = len(sys.argv) - 1
    if argsC < 2:
        raise Exception("This script require at least two arguments")
    
    # User input by input file and output file
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]
    
    newSeq = []

    # Using SeqIO to parse the fasta file
    for record in SeqIO.parse(inputFile, "fasta"):
        new = record.seq
        # getting complement of DNA
        new = new.reverse_complement()
        # changing string to complement
        record.seq = new
        # appending new record with complemented string
        newSeq.append(record)

    # Writing out in file using SeqIO.write
    SeqIO.write(newSeq, outputFile, "fasta")
    
