#!/usr/bin/env python3
# count_aip_kmer.py
# Open a sample fastq file for reading and counting kmers in sequence of 6 length
# Import re to support regular expressions in this program.

import re

all_lines = open('./Haemophilus_influenzae.fasta', 'r')  # Opening file and importing in read format 

line = ' '   # assigning empty string

kmer_length = 5   # integer of value 6 as kmer_length

kmer_dictionary = {}   # kmer dictionary to store kmers, with specific count

while line:                      # while loop
        line = all_lines.readline()               # reading line by line, of file using readline function
        if re.match('^[ATGCN]+$', line):           # checking for regular expression in line
           for start in range(0, len(line) - kmer_length):           # reading nucleotides from line in 6 format till end
               kmer = line[start: start + kmer_length]
               kmer_dictionary[kmer] = kmer_dictionary.get(kmer, 0) + 1               # storing values in kmer dictionary, if available adding 1 to it

counted_kmer = ''              # empty string

for kmer, count in sorted(kmer_dictionary.items(), key=lambda x:x[1] , reverse=True):          # storing dictionary as string in new variable
    counted_kmer = ("{0}\t{1}\n".format(kmer, count)) + counted_kmer

with open("aip_kmers.txt", 'w') as  out:                      # writing the final output file in aip_kmer.txt
     out.write(counted_kmer)                                  # using out.write function

