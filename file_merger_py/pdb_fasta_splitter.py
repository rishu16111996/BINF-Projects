"""
Program to split Amino Acid sequence and Secondary Structure
"""
import argparse
import sys
import re


def main():
    """
    Main Function
    :return: Prints the number of protein sequence and secondary structure
    """
    args = get_cli_args()
    file_2_open = args.INFILE

    fh_in = get_fh(file_2_open, "r")

    amino_acid = get_fh("pdb_protein.fasta", "w")
    sec_str = get_fh("pdb_ss.fasta", "w")

    list_headers, list_seqs = get_header_and_sequence_lists(fh_in)

    count_protein, count_sec_str = write_in_file(amino_acid, sec_str, list_headers, list_seqs)

    print(f"Found {count_protein} protein sequences\nFound "
          f"{count_sec_str} ss sequences", file=sys.stderr)


def write_in_file(amino_acid, sec_str, list_headers, list_seqs):
    """
    Function to write secondary structure and amino acid in files
    :param amino_acid: file handle for amino acid file
    :param sec_str: file handle for secondary structure file
    :param list_headers: list of headers in original fasta file
    :param list_seqs: list of sequence in original fasta file
    :return: Count of proteins and secondary structure present in original fasta file
    """
    count_protein = 0
    count_sec_str = 0

    for header, sequence in zip(list_headers, list_seqs):
        if re.match(".*sequence", header):
            amino_acid.write(header)
            amino_acid.write("\n")
            amino_acid.write(sequence)
            amino_acid.write("\n")
            count_protein += 1
        elif re.match(".*secstr", header):
            sec_str.write(header)
            sec_str.write("\n")
            sec_str.write(sequence)
            sec_str.write("\n")
            count_sec_str += 1

    return count_protein, count_sec_str


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
    parser = argparse.ArgumentParser(description="Give the fasta sequence "
                                                 "file name to do the splitting")
    parser.add_argument("-i", "--infile",
                        dest="INFILE",
                        type=str,
                        help="Path to the file to open",
                        required=True)

    return parser.parse_args()


if __name__ == "__main__":
    main()
