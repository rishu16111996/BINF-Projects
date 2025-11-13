#!/usr/bin/env python3
#count_aip_kmer.py
import re
Fastqs = open('/scratch/AiptasiaMiSeq/fastq/Aip02.R1.fastq', 'r')
line = ' '
kmer_length = 6
kmer_dictionary = {}
while line:
    line = Fastqs.readline()
    if re.match('^[ATGCN]+$', line):
        for start in range(0, len(line) - kmer_length):
            kmer = line[start: start + kmer_length]
            kmer_dictionary[kmer] = kmer_dictionary.get(kmer,0)+1

count_kmer =''

for kmer, count in kmer_dictionary.items():
    count_kmer=("{0}\t{1}\n".format(kmer, count))+count_kmer

with open("aip_kmers.txt",'w') as out:
        out.write(count_kmer)
