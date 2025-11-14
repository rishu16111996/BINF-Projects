# DM1 RNA-Seq Analysis Pipeline (Snakemake)
**Author: Rishabh Narula**

This repository contains a full **Snakemake implementation** of an RNA-Seq analysis workflow for a **DM1 patient vs control** dataset. It reproduces an end-to-end RNA-seq + variant calling workflow using **Trim Galore, STAR (two-pass), Picard, GATK, bcftools, MultiQC**, and Conda environment management.

This project demonstrates my ability to design scalable and reproducible **Snakemake workflows** for NGS analysis.

---

## 🔬 Pipeline Workflow

### ✔ Steps Implemented
1. **FastQC** – Raw QC  
2. **Trim Galore** – Adapter trimming  
3. **STAR First Pass** – Splice junction discovery  
4. **Junction Merge & STAR Index Rebuild**  
5. **STAR Second Pass** – Final alignment + gene counts  
6. **Picard Processing**  
   - AddOrReplaceReadGroups  
   - MarkDuplicates  
7. **GATK RNASeq Variant Calling**
   - SplitNCigarReads  
   - BaseRecalibrator (2 passes)  
   - ApplyBQSR  
   - HaplotypeCaller (gVCF mode)  
8. **Joint Genotyping → final VCF**  
9. **MultiQC** – Unified QC output  

---

## 📂 Repository Structure
```
DM1_Snakemake_Pipeline/
├── Snakefile
├── config.yaml
├── environment.yml
├── README.md
└── data/fastq/
```

---

## 🧬 Input FASTQs

Place paired-end FASTQ files in `data/fastq/`:

```
sample_1.fastq.gz
sample_2.fastq.gz
```

Example dataset used:  
**SRX30106897 — DM1 patient sample**

Snakemake automatically detects sample names.

---

## ⚙️ Conda Environment

Install tools:

```bash
conda env create -f environment.yml
conda activate dm1_rna_pipeline_env
```

Tools included:
- fastqc  
- trim-galore  
- STAR  
- picard  
- gatk4  
- samtools  
- bcftools  
- multiqc  

---

## ▶ Run Snakemake

```bash
snakemake --use-conda -j 4
```

Outputs appear in `results/`:

```
results/
  qc/
  trimmed/
  star_pass1/
  star_index_pass2/
  star_align/
  bam_postproc/
  recalibration/
  variants/
```

---

## 📊 Outputs

### Final Variant Call Set  
`results/variants/final_variants.vcf.gz`

### Gene Count Files  
`*_ReadsPerGene.out.tab`  
Suitable for DESeq2 differential expression.

### QC Summary  
`multiqc_report.html`

---

## 🎯 Purpose

This Snakemake project showcases:

- Production-ready workflow design  
- RNA-seq + GATK RNA Best Practices  
- Pipeline engineering with Snakemake  
- Reproducibility through Conda

Excellent as a portfolio demonstration for computational biology & bioinformatics roles.

---

## 👨‍💻 Author  
**Rishabh Narula**  
Bioinformatics • RNA-Seq • Snakemake • GATK4 • STAR • Workflow Automation
