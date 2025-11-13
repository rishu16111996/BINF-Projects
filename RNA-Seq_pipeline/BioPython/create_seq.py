#!/usr/bin/env python3
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
sequences = list()
my_seq1 = SeqRecord(Seq("AGTACACTGGT"), id="seq1", description = "kmer1")
my_seq2 = SeqRecord(Seq("AGTACACTGGC"), id="seq2", description = "kmer2")
sequences.append(my_seq1)
sequences.append(my_seq2)
SeqIO.write(sequences, "kmers.fasta", "fasta")

