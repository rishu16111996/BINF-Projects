#!/usr/bin/env bash
#spades.py

paired="./Paired/"

rhodo="Rhodo/"
mkdir -p $rhodo

function spadesAlign {
        nice -n19 python3 /usr/local/programs/SPAdes-3.10.0-Linux/bin/spades.py \
        --threads 4 \
        -o $rhodo \
        -1 $paired"SRR522244_1.paired.fastq" \
        -2 $paired"SRR522244_2.paired.fastq"
}

spadesAlign 1>spades.log 2>spades.err &

