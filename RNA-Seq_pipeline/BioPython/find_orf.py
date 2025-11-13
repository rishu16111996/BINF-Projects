#!/usr/bin/env python3
import re
from Bio.Seq import Seq
dna = Seq("GGTCCGGGATGCCTGAATGGTACACTGGTAAGTACACTGTAAGTAAAAAAAA")
rna = dna.transcribe()
print(rna)
orf = re.search('AUG([AUGC]{3})+?(UAA|UAG|UGA)', str(rna)).group()
print(orf)
