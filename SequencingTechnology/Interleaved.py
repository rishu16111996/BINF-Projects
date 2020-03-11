#!/usr/bin/env python3
# read Interleaved.py
# Import Seq, SeqRecord, and SeqIO
from Bio import SeqIO
my_left_reads = SeqIO.parse("/scratch/AiptasiaMiSeq/fastq/Aip02.R1.fastq", "fastq") # writing left files in my_left_reads
my_right_reads = SeqIO.parse("/scratch/AiptasiaMiSeq/fastq/Aip02.R2.fastq", "fastq") # writing right reads in my_right_reads
#creating an empty object
seq=[]
#open Interleaved fasta in write mode
outfile = open("Interleaved.fasta","w")
#iterate over both arrays in parallel
for left, right in zip(my_left_reads, my_right_reads):
        seq.append(left) 
        seq.append(right)
SeqIO.write(seq, outfile, "fasta") # write seq in SeqIO.write and output file in fasta type

