# Short Read Alignment 

## Rishabh Narula


# Short Read Alignment 
The purpose of this directory is to build GMPA database genome with reference to Aiptasia reads which includes steps like trimming the Aiptasia reads, aligning, sorting and indexing. 

# Methods – 
# Trimming Reads – 
scratch/AiptasiaMi/Seq/fastq is the source to perform trimming. We use Trimmomatic multi layered command line to trim and crop Illumina data, it is very fast and java based command line. 

### Steps – 
File path, suffix for left and right reads are initialized and the output directory is created. Function trimAll in run in loop for left reads fastq. This followed by removing and assigning of the path of file and then the trimmomatic task as mentioned above is run for left and right reads and the output is stored in paired and unpaired respectively along with success written to .output file and errors written to .err file.


# Aligning the reads – 
the trimmed sample are aligned using GMAP database. Gmap_build is used to create a GMAP database from the Aiptasia genome.  GSNAP then uses this data base to align RNA-Seq reads into .sam (sequence alignment/map) format.  

### Steps – 
We create output directory and specify the format of the file. Function alignAll reads is run through loop for all the left reads files in the output file. Input file is the quality trimmed and stored in paired directory. The command -A says GSNAP to create sam alignment program. Also after the function is run successfully the success and errors are written in .log and .err files. 

# Sorting and indexing the Aligning reads – 
The sam files from aligning are then sorted and converted into bam format by samtools. 

