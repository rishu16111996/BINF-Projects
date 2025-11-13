#!/usr/env/bin python3
# BioPython_genbank.py

from Bio import Entrez
from Bio import SeqIO

# assigning email id to get database from Genebank using Entrez
Entrez.email = "narula.r@northeastern.edu"

seq = []

# Using Entrez class efetch fucntion to get genebank database
with Entrez.efetch(db="nucleotide", rettype="gb", retmode="text", id="515056") as handle:
    seqRecord = SeqIO.read(handle, "gb")
    # Appending downloaded sequence to empty list
    seq.append(seqRecord)
   

with Entrez.efetch(db="nucleotide", rettype="gb", retmode="text", id="J01673.1") as handle:
    seqRecord = SeqIO.read(handle, "gb")
    seq.append(seqRecord)


for entry in seq:
    # executing the loop for each sequence, printing name first
    print("Sequence Name:{}".format(entry.name))
    # printing sequence
    print(entry.seq)
    for i in entry.features:
        # printing features
        print("{}\t{}\t{}".format(i.type, i.location, i.strand))
   

