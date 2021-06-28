This is a READ_ME file for all the scripts in assignment 3.

# Question 1

Program PDB_FASTA_SPLITTER.py take one input as -i, which is the text file with amino acid and secondary structure sequence with their respective headers, and it will print out number of amino acid and secondary structure found in file in STD.ERR and also prints out two files one with all the amino acid sequence with headers and second with secondary structure with all the headers.

Command to run = python3 pdb_fasta_splitter.py -i arg1

arg1 = Text file with amino acid and secondary structures with headers
Output = Two text file with amino acid and secondary structures

____________________________________________________________________________


# Question 2

Program nucleotide_statistics_from_fasta.py takes two arguments, -i and -o, -i takes fasta file with sequence and headers, while -o takes the name of output file in which statistics need to be printed. This program takes the fasta file and print out the statistics of sequence in text file.

Command to run = python3 nucleotide_statistics_from_fasta.py -i arg1 -o arg2

arg1 = FASTA file with sequence and headers
arg2 = Output file name to print stats of sequence with respect to headers


_____________________________________________________________________________


# Question 3

Test suite for the scripts above test_pdb_fasta_splitter.py and test_nucleotide_statistics_from_fasta.py is a pytest module for assignment 3 scripts, it covers 81% of these two scripts.

To run pytest with html coverage file = pytest --cov-report html --cov --cov-config=.coveragerc

To run pytest without html coverage file = pytest --cov --cov-config=.coveragerc

pytest needs .coveragerc file which is available in directory too, with python path to omit all python extra functions.
