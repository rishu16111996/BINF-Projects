#!/usr/bin/env bash
# alignAll.sh
# Align All paired fastq files

filepath="/scratch/SampleDataFiles/Paired/"     # file path of directory fastq files
left=".R1.paired.fastq"                # left format
rigth=".R2.paired.fastq"               # rigth format
output="quant/"                   # output directory of new aligned files
mkdir -p $output

function alignReads {                 
	for leftInFile in $filepath*$left         
    # for loop to iterate over each and every file in folder
	do
		pathRemoved="${leftInFile/$filepath/}"                # accessing each file
		sampleName="${pathRemoved/$left/}"
		echo $sampleName
		salmon quant -l IU \
            -1 $filepath$sampleName$left \
            -2 $filepath$sampleName$rigth \
            -i AipIndex \
            --validateMappings \
            -o $output$sampleName
	done
}
alignReads 1>AllalignReads.log 2>AllalignReads.err &
