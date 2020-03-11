#!/usr/bin/env bash
# buildIIT.sh
nice -n19 iit_store \
-G /scratch/AiptasiaMiSeq/\ #index of intron splicing and GSNAP will use this intron index to align reads
GCA_001417965.1_Aiptasia_genome_1.1_genomic.gff \
-o AiptasiaGmapIIT \
1>buildIIT.log 2>buildIIT.err &
