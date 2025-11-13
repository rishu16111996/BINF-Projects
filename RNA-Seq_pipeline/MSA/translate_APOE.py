#!/usr/bin/env python3
# translate_APOE.py

from Bio import SeqIO
from Bio.Seq import Seq

# empty list
sequ = []

# looping over fasta file
for record in SeqIO.parse("APOE_refseq_transcript.fasta", "fasta"):
    # getting sequence as DNA
    new = record.seq
    # transcribing
    new = new.transcribe()
    #translating
    new = new.translate()
    
    # storing in original variable
    record.seq = new
    # appending in list
    sequ.append(record)

# writing fasta file in new file using SeqIo.write 
SeqIO.write(sequ, "apoe_aa.fasta", "fasta")


