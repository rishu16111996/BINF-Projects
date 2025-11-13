#!/usr/bin/env python3
#read find_dmel_orf.py
from Bio import SeqIO
from Bio.Seq import Seq
# impor re and seq
import re
for record in SeqIO.parse("/scratch/Drosophila/dmel-all-chromosome-r6.17.fasta", "fasta"):
        if re.match("^\d{1}\D*$", record.id):
        # single digit ID which is followed by zero or more and  non numeric
            dna = record.seq
            rna = dna.transcribe()
            ##transcription of DNA to RNA 
            orf = re.search('AUG([AUGC]{3})+?(UAA|UAG|UGA)', str(rna)).group()
            ##searching for open reading frame and commanding to search from start codon AUG and stop with stop codons UAA or UAG or UGA and putting all that into a string using str command and grouping them. 
            protein = Seq(orf)
            protein = protein.translate()
            ## translation of RNA into protein 
            print(protein)

