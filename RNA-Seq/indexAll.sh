#!/usr/bin/env bash
#indexAll.sh

filepath="./bam/"  
left=".sorted.bam" 

function indexAll { #loop through all left reads .bam files in left
for leftInFile in $filepath*$left
do 
pathRemoved="${leftInFile/$filepath/}"
sampleName="${pathRemoved/$left/}"
samtools index $filepath$sampleName$left
done
}
indexAll 1>indexAll.log 2>indexAll.err & #write success and errors in log and err file resp "&" means run the program in background 


