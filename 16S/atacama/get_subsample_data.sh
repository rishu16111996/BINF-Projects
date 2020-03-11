#!/usr/bin/env bash

wget \
  -O "emp-paired-end-sequences/forward.fastq.gz" \
  "https://data.qiime2.org/2019.10/tutorials/atacama-soils/1p/forward.fastq.gz"

wget \
  -O "emp-paired-end-sequences/reverse.fastq.gz" \
  "https://data.qiime2.org/2019.10/tutorials/atacama-soils/1p/reverse.fastq.gz"

wget \
  -O "emp-paired-end-sequences/barcodes.fastq.gz" \
  "https://data.qiime2.org/2019.10/tutorials/atacama-soils/1p/barcodes.fastq.gz"
