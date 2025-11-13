# RNA‑Seq Pipeline

## 🚀 Overview
This is a reproducible RNA‑Seq analysis pipeline developed to process raw sequencing data (FASTQ) through alignment, quantification, normalization and downstream differential expression. It’s part of the project at **BINF-Projects/RNA-Seq_pipeline**.

## 🛠️ Tech & Tools
- Alignment: STAR / HISAT2
- Quantification: featureCounts / Salmon
- Differential Expression: DESeq2 / EdgeR
- Scripting: Bash + R
- Input: FASTQ files
- Reference genome + GTF annotation

## 📦 Getting Started

### Prerequisites
- Linux/Unix environment
- STAR or HISAT2 installed
- SAMtools
- featureCounts or Salmon
- R + Bioconductor packages (DESeq2, EdgeR)
- Reference genome + annotation

### Installation
```bash
git clone https://github.com/rishu16111996/BINF-Projects.git
cd BINF-Projects/RNA-Seq_pipeline
```

### Running the Pipeline
```bash
# QC
fastqc data/raw/*.fastq.gz -o results/qc/

# Alignment
STAR --runThreadN 8 --genomeDir ref/genome_index      --readFilesIn data/raw/sample1.fastq.gz      --readFilesCommand zcat      --outFileNamePrefix results/alignment/sample1_

# Quantification
featureCounts -T 8 -a ref/annotation.gtf      -o results/counts/sample1_counts.txt      results/alignment/sample1_Aligned.sortedByCoord.out.bam

# Differential Expression
Rscript scripts/differential_expression.R results/counts/ metadata.csv
```

## 📁 Directory Structure
```
├── data/
│   ├── raw/
│   └── processed/
├── ref/
├── results/
│   ├── qc/
│   ├── alignment/
│   ├── counts/
│   └── de/
├── scripts/
├── config/
└── README.md
```

## ✅ What I Did
- Full RNA‑Seq pipeline from FASTQ → DE
- Modularized scripts for each step
- Clean directory structure
- Metadata‑aware analysis
- Ready‑to‑run commands

## 📊 Outputs
- QC reports → results/qc/
- BAM files → results/alignment/
- Count tables → results/counts/
- Differential expression → results/de/

## 🔧 Future Enhancements
- Move to Snakemake or Nextflow
- Add transcript‑level quantification
- Add Docker/Singularity container
- Automated HTML reports

## 📄 License
MIT License
