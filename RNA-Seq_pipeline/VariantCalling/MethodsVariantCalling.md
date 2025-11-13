## Overview

This variant calling workflow in bash scripting is used.

1.  getGenomes.sh- In this bash script, the wget function is used to
    obtain a copy of the fast file and then gunzip is used to unpack or
    unzip the file which when done will extract the GRCh38 reference
    genome. (Li and Durbin 2009)

2.  getReads. sh- This bash script is used for downloading the fast
    reads. For this purpose, the SRA Toolkit is used, specifically the
    fast-dump function which dumps/downloads the fastq file and then
    split the files since the layout of the is paired. So after the
    split files flag is used, two fastq files are obtained. (McKenna et
    al. 2010)

3.  trimReads.sh- This bash script employs Trimmomatic which is a
    trimming tool employing Java for trimming Illumina reads. It quality
    trims the reads and splits it into paired and unpaired reads. (Chen
    et al. 2014)

4.  indexGenome.sh- In the next step, indexGenome.sh uses BWA or the
    Burrows-Wheeler Aligner to create a BWT index of the reference
    genome obtained from getGenome.sh A fai is used to create a fasta
    index, since some NGS tools require fasta index files (Bolger,
    Lohse, and Usadel 2014)

5.  alignReads.sh- This bash script uses the bwa mem algorithm which
    performs local alignment. In this script, the RG or the read groups
    identifiers are also tagged. If paired end files are used, the
    output SAM files can be combined using Picard’s MergeSamFiles to
    bind them into one and carry further analyses.
    (<span class="citeproc-not-found" data-reference-id="Valrie">**???**</span>)

6.  sortSam.sh- The output SAM file from bwa mem is then sorted using
    sort flag from Samtools. It arranges all the entries in a SAM file
    in an order (by leftmost coordinates) Ultimately, a BAM or a binary
    alignment map which is a compressed file format of SAM is created
    using Samtools. Other flags used in the script signify the number of
    threads to be used and the memory assigned to these threads.
    (Kalinin et al. 2018)

7.  indexReads.sh- The sorted BAM files are further indexed using and a
    BAM index or a .bai file is produced as an
    output.

8.  runDeepVariant.sh- This script allows us to run DeepVariant and carry out variant calling which produces a VCF file in the end enlisting the variants. (Johnson, Alexander, and Brown 2019)

## References

<div id="refs" class="references">

<div id="ref-Bolger">

Bolger, Anthony M., Marc Lohse, and Bjoern Usadel. 2014. “Trimmomatic: A
Flexible Trimmer for Illumina Sequence Data.” *Bioinformatics (Oxford,
England)* 30 (15): 2114–20.
<https://doi.org/10.1093/bioinformatics/btu170>.

</div>

<div id="ref-Chen">

Chen, Chuming, Sari S. Khaleel, Hongzhan Huang, and Cathy H. Wu. 2014.
“Software for Pre-Processing Illumina Next-Generation Sequencing Short
Read Sequences.” *Source Code for Biology and Medicine* 9 (May): 8–8.
<https://doi.org/10.1186/1751-0473-9-8>.

</div>

<div id="ref-Lisa">

Johnson, Lisa K., Harriet Alexander, and C. Titus Brown. 2019.
“Re-Assembly, Quality Evaluation, and Annotation of 678 Microbial
Eukaryotic Reference Transcriptomes.” *GigaScience* 8 (4): giy158.
<https://doi.org/10.1093/gigascience/giy158>.

</div>

<div id="ref-Kalinin">

Kalinin, Alexandr A., Gerald A. Higgins, Narathip Reamaroon,
Sayedmohammadreza Soroushmehr, Ari Allyn-Feuer, Ivo D. Dinov, Kayvan
Najarian, and Brian D. Athey. 2018. “Deep Learning in Pharmacogenomics:
From Gene Regulation to Patient Stratification.” *Pharmacogenomics* 19
(7): 629–50. <https://doi.org/10.2217/pgs-2018-0008>.

</div>

<div id="ref-Li">

Li, Heng, and Richard Durbin. 2009. “Fast and Accurate Short Read
Alignment with Burrows-Wheeler Transform.” *Bioinformatics (Oxford,
England)* 25 (14): 1754–60.
<https://doi.org/10.1093/bioinformatics/btp324>.

</div>

<div id="ref-Mckenna">

McKenna, Aaron, Matthew Hanna, Eric Banks, Andrey Sivachenko, Kristian
Cibulskis, Andrew Kernytsky, Kiran Garimella, et al. 2010. “The Genome
Analysis Toolkit: A MapReduce Framework for Analyzing Next-Generation
DNA Sequencing Data.” *Genome Research* 20 (9): 1297–1303.
<https://doi.org/10.1101/gr.107524.110>.

</div>

</div>
