#!/usr/bin/env bash
# alignAll.sh

filepath="./Paired/" #intialze variable to contain paired reads 
left=".R1.fastq"  # intialize variable to contain left fastq files
right=".R2.fastq" # intialize varibale to contain right fastq files
newForm=".sam" # output in .sam 
output="sam/" 
mkdir -p $output  # make directory output
function alignReads {  # loop through 
    for leftInFile in $filepath*$left
    do
        pathRemoved="${leftInFile/$filepath/}"
        sampleName="${pathRemoved/$left/}"
        echo $sampleName
        nice -n19 gsnap\
        -A sam \ #gsnap to create sam alignment 
        -D . \  # database
        -d AiptasiaGmapDb\
        -s AiptasiaGmapIIT.iit\
        $filepath$sampleName$left\
        $filepath$sampleName$right\
        1>$output$sampleName$newForm
    done
}
alignReads 1>AllalignReads.log 2>AllalignReads.err &
