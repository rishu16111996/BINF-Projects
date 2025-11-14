# DM1 RNA-Seq Variant Calling & Expression Pipeline (Nextflow)
**Author: Rishabh Narula**

This repository contains a fully reproducible **Nextflow pipeline** for processing RNA-Seq data from a **Myotonic Dystrophy Type 1 (DM1)** patient and a matched control.  
The pipeline performs **QC → trimming → two‑pass STAR alignment → GATK RNA‑seq variant calling → gene quantification**, producing both **variant calls** and **gene expression matrices**.

This project is part of my portfolio demonstrating workflow engineering expertise in **Nextflow**, **GATK**, **STAR**, and **NGS processing**.

---

## 🔬 Pipeline Overview

### ✔ Steps Implemented
1. **FastQC** – Raw quality assessment  
2. **Trim Galore** – Adapter & low‑quality trimming  
3. **STAR Two‑Pass Alignment**
   - First pass: splice junction discovery  
   - Merge junctions  
   - Build updated STAR index  
   - Second pass: final genome alignment + transcriptome alignment + gene counts  
4. **Picard Tools**
   - Add read groups  
   - Mark duplicates  
5. **GATK RNA Best Practices**
   - SplitNCigarReads  
   - BaseRecalibrator (Pass 1)  
   - ApplyBQSR  
   - BaseRecalibrator (Pass 2)  
   - ApplyBQSR  
6. **GATK HaplotypeCaller → gVCFs**  
7. **GATK CombineGVCFs + GenotypeGVCFs → final joint VCF**  
8. **MultiQC** – Unified QC report summarizing all samples  

---

## 📂 Project Structure

```
DM1_Nextflow_Pipeline/
├── main.nf
├── nextflow.config
├── environment.yml
├── README.md
└── data/fastq/
```

Place paired-end FASTQ files inside the `data/fastq/` directory.

---

## 🧬 Input Data

The pipeline expects FASTQ files named as:

```
sample_1.fastq.gz
sample_2.fastq.gz
```

Example dataset analyzed:  
📌 **SRX30106897 — DM1 patient RNA‑Seq sample**

---

## ⚙️ Conda Environment

Install all dependencies:

```bash
conda env create -f environment.yml
conda activate dm1_rna_pipeline_env
```

Environment includes:

- fastqc  
- trim-galore  
- star  
- picard  
- gatk4  
- samtools  
- bcftools  
- multiqc  

---

## ▶ Running the Pipeline

Execute with:

```bash
nextflow run main.nf -profile conda
```

Nextflow will automatically:

✔ Detect samples  
✔ Run all processes  
✔ Create directories under `results/`  

---

## 📁 Output Structure

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

### Key Outputs

#### 🧬 Variant Calls
- `final_variants.vcf.gz`
- `final_variants.vcf.gz.tbi`

#### 📈 Gene Expression
- `<sample>_ReadsPerGene.out.tab`  
  (can be used for DESeq2 differential expression)

#### 📊 QC Reports
- `multiqc_report.html`

---

## 🎯 Purpose

This pipeline was built to showcase:

- Professional-grade workflow development  
- Experience with RNA‑Seq + GATK variant calling  
- Use of Nextflow + Conda for reproducible NGS analysis  
- Best‑practice bioinformatics engineering  

Perfect for recruiters and technical interview evaluation.

---

## 👨‍💻 Author

**Rishabh Narula**  
Bioinformatics • RNA‑Seq • Workflow Engineering • Nextflow • GATK • Cloud • Python
