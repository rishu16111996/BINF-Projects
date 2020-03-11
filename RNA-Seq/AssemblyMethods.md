# Jeel Koradiya 

# assembly methods 

# methods 
the purpose of this assembly is to perfom reference guided and non guided or de-novo assembly of the genome created.

## Trninity 
is software we will use to assemble the transcriptome from contigs. 

## merge Bam file 
we will use reference guided assembly for that we need the input to be bam files so we first. samtools is used to merge bam files into single bam file. all the file are redirected to bamIn.txt -b is to pass the files in bamIn.txt file. 

## assemble the Transcriptome 
nice -n19 /usr/local/programs/trinityrnaseq-Trinity-v2.8.4/Trinity here nice -n19 command puts this program at least importance and the rest of it is the path to trinity assembler. genome_guided_bam bam is for genome guided assembly followed by merged bam file. 
genome_guided_max_intron 10000 is the command for maximum seperation distance that trinity will allow segments of trascript to span introns. after this we specify the maximum memory trinity will use for this assembly.

## de novo transcriptome assembly 
for this we first need to write script for creating a comma seperate list of file for left and right reads. we start by defining variable for leftReads= ls -q Paired/Aip*.R1.fastq is the list name for left reads and similary R2.fastq is for the right reads store in rightReads variable. we store echo of leftReads in leftReads to get rid of the line breaks.  leftReads=#leftReads// /,} this is to replace spaces with comma so as to get comma seperated list of file we follow the same for the right reads. now we psecify the priority of this operation and also path for trinity. we then specify the output directory and  the memory trinity should use to perform this assembly and also create log and err file to direct output and errors respectively.   
