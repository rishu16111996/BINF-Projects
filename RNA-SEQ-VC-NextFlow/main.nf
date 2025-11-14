#!/usr/bin/env nextflow
// DM1 RNA-Seq Variant Calling & Differential Expression Pipeline (Nextflow)
// Author: Rishabh Narula

nextflow.enable.dsl=2

// Define pipeline processes
process FastQC {
    tag "$fastq.name"
    publishDir "${params.outdir}/qc", mode: 'copy'
    input:
    path fastq
    output:
    path "${fastq.baseName}_fastqc.html", emit: html
    path "${fastq.baseName}_fastqc.zip", emit: zip
    script:
    """
    fastqc --nogroup -o $PWD ${fastq}
    """
}

process TrimGalore {
    tag "$sample"
    publishDir "${params.outdir}/trimmed", mode: 'copy'
    input:
    tuple val(sample), path(reads1), path(reads2)
    output:
    tuple val(sample), path "${sample}_1_val_1.fq.gz", path "${sample}_2_val_2.fq.gz"
    script:
    """
    trim_galore --paired --illumina -q 20 --phred33 --length 20 \\
        --cores 4 --output_dir $PWD \\
        ${reads1} ${reads2}
    """
}

process STAR_First_Pass {
    tag "$sample"
    publishDir "${params.outdir}/star_pass1", mode: 'copy'
    input:
    tuple val(sample), path(r1), path(r2)
    output:
    tuple val(sample), path "${sample}_SJ.out.tab"
    script:
    """
    STAR --runThreadN ${task.cpus} \\
         --genomeDir ${params.star_index_dir} \\
         --readFilesIn ${r1} ${r2} --readFilesCommand zcat \\
         --outFileNamePrefix ${sample}_ \\
         --outSAMtype None \\
         --outSJfilterReads All \\
         --outFilterType BySJout \\
         --outFilterMultimapNmax 20 \\
         --outFilterMismatchNmax 999 \\
         --outFilterMismatchNoverReadLmax 0.04 \\
         --alignIntronMin 20 \\
         --alignIntronMax 1000000 \\
         --alignSJoverhangMin 8 \\
         --alignSJDBoverhangMin 1 \\
         --sjdbScore 1
    """
}

process MergeJunctions {
    tag "merge_SJ"
    publishDir "${params.outdir}/star_pass1", mode: 'copy'
    input:
    path sj_tabs
    output:
    path "SJ.out.pass1_merged.tab"
    script:
    """
    cat ${sj_tabs} | awk '$7 >= 3' | cut -f1-4 | sort -u > SJ.out.pass1_merged.tab
    """
}

process STAR_Index_Pass2 {
    tag "star_index_pass2"
    publishDir "${params.outdir}/star_index_pass2", mode: 'copy'
    input:
    path merged_sj, path genome_fasta, path genome_gtf
    output:
    path "SAindex" emit: index_marker  // marker file indicating index built
    directory "star_index_pass2"
    script:
    """
    STAR --runThreadN ${task.cpus} --runMode genomeGenerate \\
         --genomeDir star_index_pass2 \\
         --genomeFastaFiles ${genome_fasta} \\
         --sjdbFileChrStartEnd ${merged_sj} \\
         --sjdbGTFfile ${genome_gtf} \\
         --sjdbOverhang 149
    """
}

process STAR_Second_Pass {
    tag "$sample"
    publishDir "${params.outdir}/star_align", mode: 'copy'
    input:
    tuple val(sample), path(trim1), path(trim2), path star_index_dir from STAR_Index_Pass2.out
    output:
    tuple val(sample),
          path "${sample}_Aligned.sortedByCoord.out.bam",
          path "${sample}_Aligned.toTranscriptome.out.bam",
          path "${sample}_ReadsPerGene.out.tab"
    script:
    """
    STAR --runThreadN ${task.cpus} \\
         --genomeDir ${star_index_dir} \\
         --readFilesIn ${trim1} ${trim2} --readFilesCommand zcat \\
         --outFileNamePrefix ${sample}_ \\
         --outSAMtype BAM SortedByCoordinate \\
         --outSAMunmapped Within \\
         --quantMode TranscriptomeSAM GeneCounts \\
         --outSAMattributes NH HI AS NM MD \\
         --outFilterType BySJout \\
         --outFilterMultimapNmax 20 \\
         --outFilterMismatchNmax 999 \\
         --outFilterMismatchNoverReadLmax 0.04 \\
         --alignIntronMin 20 \\
         --alignIntronMax 1000000 \\
         --alignSJoverhangMin 8 \\
         --alignSJDBoverhangMin 1 \\
         --sjdbScore 1 \\
         --outBAMsortingThreadN 4
    """
}

process AddReadGroups {
    tag "$sample"
    publishDir "${params.outdir}/bam_postproc", mode: 'copy'
    input:
    tuple val(sample), path(coord_bam)
    output:
    tuple val(sample), path "${sample}_rg.bam"
    script:
    """
    picard AddOrReplaceReadGroups \\
          I=${coord_bam} \\
          O=${sample}_rg.bam \\
          RGID=${sample} RGLB=lib1 RGPL=illumina RGPU=unit1 RGSM=${sample}
    """
}

process MarkDuplicates {
    tag "$sample"
    publishDir "${params.outdir}/bam_postproc", mode: 'copy'
    input:
    tuple val(sample), path(rg_bam)
    output:
    tuple val(sample),
          path "${sample}_dedup.bam",
          path "${sample}_dedup.bam.bai",
          path "${sample}_dedup.metrics.txt"
    script:
    """
    picard MarkDuplicates \\
          I=${rg_bam} \\
          O=${sample}_dedup.bam \\
          M=${sample}_dedup.metrics.txt \\
          CREATE_INDEX=true \\
          ASSUME_SORT_ORDER=coordinate \\
          OPTICAL_DUPLICATE_PIXEL_DISTANCE=100
    """
}

process SplitNcigarReads {
    tag "$sample"
    publishDir "${params.outdir}/bam_postproc", mode: 'copy'
    input:
    tuple val(sample), path(dedup_bam)
    output:
    tuple val(sample), path "${sample}_split.bam"
    script:
    """
    gatk SplitNCigarReads \\
        -R ${params.genome} \\
        -I ${dedup_bam} \\
        -O ${sample}_split.bam
    """
}

process BaseRecalibrator1 {
    tag "$sample"
    publishDir "${params.outdir}/recalibration", mode: 'copy'
    input:
    tuple val(sample), path(split_bam)
    output:
    tuple val(sample), path "${sample}_recal.table"
    script:
    """
    gatk BaseRecalibrator \\
        -R ${params.genome} \\
        -I ${split_bam} \\
        --known-sites ${params.knownSites} \\
        --known-sites ${params.knownIndels} \\
        --known-sites ${params.dbsnp} \\
        -O ${sample}_recal.table
    """
}

process ApplyBQSR1 {
    tag "$sample"
    publishDir "${params.outdir}/recalibration", mode: 'copy'
    input:
    tuple val(sample), path(split_bam), path(recal_table) from SplitNcigarReads.out.join(BaseRecalibrator1.out)
    output:
    tuple val(sample), path "${sample}_recal.bam"
    script:
    """
    gatk ApplyBQSR \\
        -R ${params.genome} \\
        -I ${split_bam} \\
        --bqsr-recal-file ${recal_table} \\
        -O ${sample}_recal.bam
    """
}

process BaseRecalibrator2 {
    tag "$sample"
    publishDir "${params.outdir}/recalibration", mode: 'copy'
    input:
    tuple val(sample), path(recal_bam)
    output:
    tuple val(sample), path "${sample}_recal2.table"
    script:
    """
    gatk BaseRecalibrator \\
        -R ${params.genome} \\
        -I ${recal_bam} \\
        --known-sites ${params.knownSites} \\
        --known-sites ${params.knownIndels} \\
        --known-sites ${params.dbsnp} \\
        -O ${sample}_recal2.table
    """
}

process ApplyBQSR2 {
    tag "$sample"
    publishDir "${params.outdir}/recalibration", mode: 'copy'
    input:
    tuple val(sample), path(recal_bam), path(recal2_table) from ApplyBQSR1.out.join(BaseRecalibrator2.out)
    output:
    tuple val(sample), path "${sample}_final.bam"
    script:
    """
    gatk ApplyBQSR \\
        -R ${params.genome} \\
        -I ${recal_bam} \\
        --bqsr-recal-file ${recal2_table} \\
        -O ${sample}_final.bam
    """
}

process HaplotypeCaller {
    tag "$sample"
    publishDir "${params.outdir}/variants", mode: 'copy'
    input:
    tuple val(sample), path(final_bam)
    output:
    tuple val(sample),
          path "${sample}.g.vcf.gz",
          path "${sample}.g.vcf.gz.tbi"
    script:
    """
    gatk HaplotypeCaller \\
        -R ${params.genome} \\
        -I ${final_bam} \\
        -ERC GVCF \\
        -O ${sample}.g.vcf.gz
    """
}

process CombineGVCFs {
    tag "CombineGVCFs"
    publishDir "${params.outdir}/variants", mode: 'copy'
    input:
    path gvcf_files
    output:
    path "combined.g.vcf.gz",
    path "combined.g.vcf.gz.tbi"
    script:
    """
    gatk CombineGVCFs -R ${params.genome} \\
        ${gvcf_files.collect{ "-V ${it}".toString() }.join(" ")} \\
        -O combined.g.vcf.gz
    """
}

process GenotypeGVCFs {
    tag "GenotypeGVCFs"
    publishDir "${params.outdir}/variants", mode: 'copy'
    input:
    path combined_gvcf
    output:
    path "final_variants.vcf.gz",
    path "final_variants.vcf.gz.tbi"
    script:
    """
    gatk GenotypeGVCFs -R ${params.genome} \\
        -V ${combined_gvcf} \\
        -O final_variants.vcf.gz
    """
}

process MultiQC {
    tag "MultiQC"
    publishDir "${params.outdir}/qc", mode: 'copy'
    input:
    path(qc_files)
    output:
    path "multiqc_report.html"
    script:
    """
    multiqc -o $PWD ${params.outdir}
    """
}

// Define workflow execution order and channels
workflow {
    // Input FASTQ channel (paired-end reads)
    Channel.fromFilePairs("${params.reads}/*_1.fastq.gz", flat: true, size: 2, namePattern: ~/([^_]+)_1\.fastq\.gz/) \
            .map { sample, reads -> tuple(sample, reads[0], reads[1]) } \
            .set { read_pairs_ch }

    // Run FastQC on all FASTQ files
    // (split read pairs into individual files for QC)
    read_pairs_ch.map{ it -> tuple(it[0], it[1]) }.concat( read_pairs_ch.map{ it -> tuple(it[0], it[2]) } ) \
                 .map{ it[1] } | FastQC

    // Trim adapters and low-quality sequences
    trimmed_ch = read_pairs_ch | TrimGalore

    // STAR first pass alignment (for junction discovery)
    sj_ch = trimmed_ch | STAR_First_Pass

    // Merge junctions from all samples
    merged_sj_ch = sj_ch.collect() | MergeJunctions

    // Build STAR index with discovered junctions
    index_ch = merged_sj_ch.combine(Channel.value(file(params.genome)), Channel.value(file(params.gtf))) | STAR_Index_Pass2

    // STAR second pass alignment using new index
    aligned_ch = trimmed_ch.combine(index_ch) | STAR_Second_Pass

    // Separate outputs of second pass
    coord_bams_ch = aligned_ch.map{ sample, sorted_bam, trans_bam, counts -> tuple(sample, sorted_bam) }

    // Add read groups, mark duplicates, split CIGAR
    rg_bams_ch    = coord_bams_ch | AddReadGroups
    dedup_bams_ch = rg_bams_ch    | MarkDuplicates
    split_bams_ch = dedup_bams_ch | SplitNcigarReads

    // Base recalibration (two-pass BQSR)
    recal_tables1_ch = split_bams_ch | BaseRecalibrator1
    applied_bams1_ch = split_bams_ch.join(recal_tables1_ch) | ApplyBQSR1
    recal_tables2_ch = applied_bams1_ch | BaseRecalibrator2
    final_bams_ch    = applied_bams1_ch.join(recal_tables2_ch) | ApplyBQSR2

    // Variant calling per sample
    gvcfs_ch = final_bams_ch | HaplotypeCaller

    // Joint genotyping
    combined_gvcf_ch = gvcfs_ch.collect() | CombineGVCFs
    final_vcf_ch     = combined_gvcf_ch | GenotypeGVCFs

    // Run MultiQC after FastQC and MarkDuplicates metrics are available
    // (collect all fastqc outputs and dedup metrics for QC reporting)
    qc_inputs_ch = Channel.from(FastQC.out.html, MarkDuplicates.out.map{ it[2] })  // gather fastqc HTMLs and metrics
    qc_inputs_ch.collect() | MultiQC

    // Specify workflow outputs (for clarity)
    emit:
    final_vcf_ch
}
