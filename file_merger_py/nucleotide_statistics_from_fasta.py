"""
Program to open Fasta file and print out the Nucleotide stats in text file
"""
import argparse
import sys
import re


def main():
    """
    Main Function to print out the Nucleotide stats of input Fasta file
    :return: Text file with Nucleotide Stats
    """
    args = get_cli_args()
    file_2_open = args.INFILE
    file_2_write = args.OUTFILE

    fh_in = get_fh(file_2_open, "r")
    fh_out = get_fh(file_2_write, "w")

    list_headers, list_seqs = get_header_and_sequence_lists(fh_in)

    print_sequence_stats(list_headers, list_seqs, fh_out)


def _get_nt_occurrence(nucleotide, sequence):
    """
    Function to count particular nucleotide sequence
    :param nucleotide: Nucleotide Name to count the occurrence in sequence
    :param sequence: Sequence to count occurrence of Nucleotide
    :return: Length of Nucleotide occurrence in Sequence
    """
    if nucleotide in ["A", "G", "T", "C", "N"]:
        occurrence = [x.start() for x in re.finditer(nucleotide, sequence)]
    else:
        sys.exit("Did not code this condition")
    return len(occurrence)


def _get_accession(header_string):
    """
    Get Accession Number of Header from fasta file
    :param header_string: Name of the header
    :return: Accession Number for the Sequence to print in text file
    """
    return header_string.split(" ", 1)[0].replace(">", "")


def print_sequence_stats(list_header, list_seqs, fh_out):
    """
    Main function to calculate and print Stats for Nucleotide from Fasta file
    :param list_header: list of headers in original fasta file
    :param list_seqs: list of sequence in original fasta file
    :param fh_out: File handler to write the stats in text file
    :return: Text file with stats of nucleotide from given fasta file
    """

    # pylint: disable=invalid-name

    count = 0

    fh_out.write("Number\tAccession\tA's\tG's\tC's\tT's\tN's\tLength\tGC%\n")

    for header, sequence in zip(list_header, list_seqs):

        num_As = _get_nt_occurrence('A', sequence)
        num_Cs = _get_nt_occurrence('C', sequence)
        num_Gs = _get_nt_occurrence('G', sequence)
        num_Ts = _get_nt_occurrence('T', sequence)
        num_Ns = _get_nt_occurrence('N', sequence)
        accession_string = _get_accession(header)
        count += 1

        fh_out.write(f"{count}\t{accession_string}\t{num_As}\t{num_Gs}\t{num_Cs}"
                     f"\t{num_Ts}\t{num_Ns}\t{len(sequence)}"
                     f"\t{(((num_Gs + num_Cs) / len(sequence)) * 100):.1f}\n")

    fh_out.close()


def _check_size_of_lists(list_headers, list_seqs):
    """
    Check size of header and sequence function
    :param list_headers: list of headers in original fasta file
    :param list_seqs: list of sequence in original fasta file
    :return: Return True if size of header and sequence is equal else exit function
    """
    if len(list_headers) != len(list_seqs):
        sys.exit("The size of the sequences and the header lists is different \n"
                 "Are you sure the FASTA is in correct format")
    else:
        return True


def get_header_and_sequence_lists(file_handler):
    """
    Get Header and Sequence function to create two different lists
    :param file_handler: input fasta file handle to parse lists
    :return: two lists with headers and sequence from original fasta file
    """
    list_headers = []
    list_seqs = []
    seq = ""

    for line in file_handler:
        if re.match(r">", line):
            list_headers.append(line.strip())
            if len(seq) >= 1:
                list_seqs.append(seq)
                seq = ""
        else:
            seq = seq + line.strip()

    if len(seq) >= 1:
        list_seqs.append(seq)

    _check_size_of_lists(list_headers, list_seqs)

    get_fh(file_handler, "close")

    return list_headers, list_seqs


def get_fh(file_name, file_arg):
    """
    Get file Handle function to open and close the files passed
    To open and close the file in same function I created the new
    file_arg == close, if close is passed in get_fh function it should take
    the file handle and close it, else if any other invalid file_arg is passed
    it should throw and error.
    :param file_name: Name of the input or output file to read or write
    :param file_arg: File argument either read or write
    :return: Returns the file handle
    """
    if file_arg == "close":
        file_name.close()
    else:
        try:
            handler = open(file_name, file_arg)
            return handler

        except IOError:
            sys.exit("IOError cannot open file.."
                     "Are you sure you provided correct FASTA file?")
        except ValueError:
            sys.exit("PLease provide the correct opening mode")

    return True


def get_cli_args():
    """
    Get Command Line Argument function to read arguments from command line using argparse
    :return: Argument Parser object with all the required options
    """
    parser = argparse.ArgumentParser(description="Give the fasta sequence file "
                                                 "name to get the nucleotide statistics")
    parser.add_argument("-i", "--infile",
                        dest="INFILE",
                        type=str,
                        help="Path to the file to open",
                        required=True)

    parser.add_argument("-o", "--outfile",
                        dest="OUTFILE",
                        type=str,
                        help="Path to the file to write",
                        required=True)

    return parser.parse_args()


if __name__ == "__main__":
    main()
