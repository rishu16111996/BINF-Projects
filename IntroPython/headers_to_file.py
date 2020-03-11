#!/usr/bin/env python
#headers_to_file.py
import re
dmel_genome_path = '/scratch/Drosophila/dmel-all-chromosome-r6.17.fasta'
line_count = 0;
seq = ''

with open(dmel_genome_path) as dmel_genome:
    for line in dmel_genome:
        if line_count < 50:
       		# Check to see if the line is a header line (starts with)
            if re.match('^>', line):
                # Print the header
                seq += line
                line_count += 1
                #if its a header then add 1 in line_count
                #line_count +=1 

with open("dmel_headers.txt",'w') as out:
	#printing whole sequence variance in file
    out.write(seq)
