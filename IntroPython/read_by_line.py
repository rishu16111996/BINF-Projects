#!/usr/bin/env python
# read_by_line.py
read_sample = open('/scratch/SampleDataFiles/Sample.R1.fastq', 'r')
line = ' '
while line:
    line = read_sample.readline()
    print(line)
