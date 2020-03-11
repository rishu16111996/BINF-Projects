
#!/usr/bin/env bash
#trim.sh

pairedOutPath="Paired/"
unpairedOutPath="Unpaired/"

mkdir -p $pairedOutPath
mkdir -p $unpairedOutPath

function trim {
    nice -n19 java -jar /usr/local/programs/Trimmomatic-0.36/trimmomatic-0.36.jar PE \
    -threads 1 -phred33 \
    SRR522244_1.fastq \
    SRR522244_2.fastq \
    $pairedOutPath"SRR522244_1.paired.fastq" \
    $unpairedOutPath"SRR522244_1.unpaired.fastq" \
    $pairedOutPath"SRR522244_2.paired.fastq" \
    $unpairedOutPath"SRR522244_2.unpaired.fastq" \
    HEADCROP:0 \
    ILLUMINACLIP:/usr/local/programs/Trimmomatic-0.36/adapters/TruSeq3-PE.fa:2:30:10 \
    LEADING:20 TRAILING:20 SLIDINGWINDOW:4:30 MINLEN:36
}
trim 1>trim.log 2>trim.err &
