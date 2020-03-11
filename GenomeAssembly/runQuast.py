#!/usr/bin/env bash 
#runQuast.py

scaffolds="./Rhodo/scaffolds.fasta"

quastOutput="path/"

mkdir -p $quastOutput

function quast {
        nice -n19 python /usr/bin/quast.py \
                -o $quastOutput \
                --gene-finding \
                --threads 4 \
                --scaffolds $scaffolds
}

quast 1>quast.log 2>quast.err &
