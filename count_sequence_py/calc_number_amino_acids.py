"""
This Program takes the sequence name and number of amino acid in sequence and calculate the weight
of protein based on protein length and average weight of each amino acid
"""

import sys


def calc_weight(sequence_len):
    """
    Function to calculate the average weight
    """
    return sequence_len * AVG_WEIGHT


def get_len():
    """
    Function to get the length of sequence in nucleotides from user and print out the number of
    amino acid
    """
    len_seq = input("Please enter the length of the sequence: ")
    protein_len = (int(len_seq) % 3)

    # pylint: disable=no-else-return
    # checking if sequence length is multiple of 3 or not
    if protein_len == 0:
        print("The length of the DNA is:", len_seq)
        print("The length of the decoded protein is:", (int(len_seq) / 3))
        # returning the number of amino acid after conversion from nucleotides
        return int(len_seq) / 3

    # if not exit the program with error message
    else:
        print("Error: the DNA sequence is not a multiple of 3")
        sys.exit("your sequence looks fishy")


def get_name():
    """
    Function to get the name of the sequence from user
    """
    dna_name = input("Please enter a name for the DNA sequence: ")
    print("Your sequence name is:", dna_name)


if __name__ == '__main__':

    # average weight of each amino acid
    AVG_WEIGHT = 110
    # name of sequence
    get_name()
    # length of sequence
    PROTEIN_LENGTH = get_len()

    # getting the weight of protein
    WEIGHT_IN_KD = calc_weight(PROTEIN_LENGTH)

    # printing out final output
    print('The average weight of this protein sequence is:', (WEIGHT_IN_KD / 1000))
