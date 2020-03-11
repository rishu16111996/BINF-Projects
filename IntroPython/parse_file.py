#!/usr/bin/env python
#parse_file.py
import re
dmel_genome_path = '/scratch/Drosophila/dmel-all-chromosome-r6.17.fasta'
line_count = 0;
seq = ''

with open(dmel_genome_path) as dmel_genome:
    for line in dmel_genome:
        # Increment the line count by one
        line_count += 1
        # If the line count is less than 5
        if line_count < 5:
            # Check to see if the line is a header line (starts with >)
            if re.match('^>', line):
                # Print the header
                print(line)
            else:
                # This is a sequence line so append to seq
                seq += line
print(seq)
