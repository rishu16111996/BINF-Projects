#!/usr/bin/env python3
# BioPython_seq.py

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_dna
from Bio import SeqIO

# Using SeqRecord to create an object with generic DNA
seqRecord = SeqRecord(seq = Seq("aaaatgggggggggggccccgtt", generic_dna), id = "#12345", description = "example 1")

print(seqRecord)
print(seqRecord.seq)
print(seqRecord.id)
print(seqRecord.description)

# Writing created DNA to gb format file for genebank using SeqIO.write
SeqIO.write(seqRecord, "BioPython_seq.gb", "gb")





