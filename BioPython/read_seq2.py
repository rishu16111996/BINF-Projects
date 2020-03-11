#!/usr/bin/env python3
from Bio import SeqIO
import re
for record in SeqIO.parse("/scratch/Drosophila/dmel-all-chromosome-r6.17.fasta", "fasta"):
        if re.match("^\d{1}\D*$", record.id):
            num_bases = len(record.seq)
            print("Chromosome {} has {:,} bases".format(record.id, num_bases))
