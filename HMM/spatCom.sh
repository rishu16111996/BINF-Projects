#!/usr/bin/env bash


sspatt Pyrococcus_abyssi.fasta -l $1 -m 1 --all-words >Pyrococcus_abyssi.fasta.$1.m1.allwords.txt
sspatt Pyrococcus_horikoshii.fasta -l $1 -m 1 --all-words >Pyrococcus_horikoshii.fasta.$1.m1.allwords.txt
paste Pyrococcus_horikoshii.fasta.$1.m1.allwords.txt Pyrococcus_abyssi.fasta.$1.m1.allwords.txt >Pyrococcus_horikoshii.fasta.$1.m1.allwords_Pyrococcus_abyssi.fasta.$1.m1.allwords.txt
