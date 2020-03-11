#!/usr/bin/env bash
# sortAll.sh

filepath="./sam/"
left=".sam"
newForm=".sorted.bam"
output="bam/"
mkdir -p $output

function sortAll {
for leftInFile in $filepath*$left
do
    pathRemoved="${leftInFile/$filepath/}"
    sampleName="${pathRemoved/$left/}"
    samtools sort \
    $filepath$sampleName$left \
    -o $output$sampleName$newForm
done
}
sortAll 1>sortAll.log 2>sortAll.err &
