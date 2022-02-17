Read_ME.txt for run_mutect_pon_workflow.txt and run_mutect_workflow.txt

1. First of all its clear mandatory, that user needs all the bam, resource and reference file, available in data/ directroy to run these scripts. And user need to be on LInux, or MAC OS machine.

2. Atleast 16Gb of space is required in disk to run these scripts, If user don't need annotation file using Funcotator, than only 2GB space needed, as GATK Funcotator reference file is only 14GB.

3. For run_mutect_pon_workflow.txt script, to run it as bash convert it to ".sh" file format from ".txt" and same for the run_mutect_workflow.txt

4. In first step in run_mutect_pon_workflow.txt, we are downloading GATK-4.1.6.0, so user use only this version while on this script. Then we are extracting it, using unzip function. 

5. For both the scripts we created $gatk4 variable with "java -jar gatk-4.1.6.0/gatk-package-4.1.6.0-local.jar" command as argument to use, GATK-4.1.6.0 version only latter on in this script.

*ASSUMPTION*

I created run_mutect_pon_workflow.txt script as dynamic script, so you can either pass three arguments from bash command line, along with script for example :

~$ bash run_mutect_pon_workflow.sh HG00190 HG02759 NA19771

These three argument is BAM files names which should be present in /data/bams folders without any extenstion like ".intervaled.bam", as it is pre-written in script, just pass any 3 bam file names to create Panel of normal with this script, 

Or you can run this script without any argument then it will take default bam files which is basically (HG00190, HG02759, NA19771), without throwing any error, as I created IF-Else loop for regulation of number of passed arguments. Script with default bam files run like this :

~$ bash run_mutect_pon_workflow.sh

But, If User is passing new BAM files, he should pass three BAM files, not less or more than that, otherwise it will use default BAMS only.

6. In the end run_mutect_pon script create PON.vcf.gz file, as output.

7. For next script all the basic steps are same, and file directories are also same, I am just downloading Funcotator reference file which is 14GB, if user have it already, they can comment that line of code, otherwise it will download Funcotator Reference file and unzip it in current working directory and use it for creating annotation for mutetct2 calls.

8. For run_mutect_workflow, script we will get output as filtered.maf file, which is annotated variant version maf file for Mutect2 calls, using hg38 as refrence genome.
