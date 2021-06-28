"""
File to write Gene Category, description and occurence in text file
By combining two files
"""
import argparse
import collections
import sys
from assignment4 import my_io


def main():
    """
    Main function
    :return: file in output folder with category, occurence and
    description
    """
    args = get_cli_args()
    # function to check for passed arguments
    gene_cat_file, gene_dec_file = check_passed_args(args)
    # Output file path
    outfile = "OUTPUT/categories.txt"
    # opening file handle to read and write
    fh_in1 = my_io.get_fh(gene_cat_file, "r")
    fh_in2 = my_io.get_fh(gene_dec_file, "r")
    fh_out = my_io.get_fh(outfile, "w")
    # Parsing information in dictionaries from files
    cat_count_dict, cat_desc_dict = parse_to_dict(fh_in1, fh_in2)
    # writing to file using dictionary
    parse_to_file(cat_count_dict, cat_desc_dict, fh_out)
    # closing all file handle opened
    close_all_file_handle([fh_in1, fh_in2, fh_out])


def close_all_file_handle(file_handles):
    """
    Function to close all opened file handle
    :param file_handles: List of file handles opened
    :return: True if successufll
    """
    for i in file_handles:
        my_io.get_fh(i, "close")

    return True


def parse_to_file(cat_count_dict, cat_desc_dict, fh_out):
    """
    Function to write Category, Occurence and Description in
    text file using tab seperated format
    :param cat_count_dict: category occurence count dictionary
    from parse_to_dict function
    :param cat_desc_dict: category description dictionary
    from parse_to_dict function
    :param fh_out: File handle to write in text file
    :return: True if successfull
    """
    fh_out.write("Category\tOccurrence\tDescription\n")

    for key, value in cat_count_dict.items():
        fh_out.write(f"{key}\t{value}\t{cat_desc_dict[key]}\n")

    return True


def parse_to_dict(fh_in1, fh_in2):
    """
    Function to write gene category, description, and
    occurence in dictionary from 2 given text files
    :param fh_in1: first text file handle from CLI or default option
    :param fh_in2: second text file handle from CLI or default option
    :return: Two dictionaries one for gene category and occurence based
    on counts, and second for gene category and description
    """
    cat_count_dict = {}
    category_list = []
    cat_desc_dict = {}

    lines = fh_in1.readlines()[1:]

    for line in lines:
        category = line.split("\t")[2]
        category_list.append(category.rstrip())

    for cate in category_list:
        cat_count_dict[cate] = cat_count_dict.get(cate, 0) + 1

    for line in fh_in2:
        (category, desc) = line.split("\t")
        cat_desc_dict[category] = desc.rstrip()

    del cat_count_dict['']

    cat_count_dict = dict(collections.OrderedDict(sorted
                                                  (cat_count_dict.items())))

    return cat_count_dict, cat_desc_dict


def check_passed_args(args):
    """
    Check how many arguments passed, if NONE return
    default file options
    :param args: Argparse file arguments, passed in CLI
    :return: Names of the file to open
    """

    infile1 = "chr21_genes.txt"
    infile2 = "chr21_genes_categories.txt"
    args_to_return1 = ""
    args_to_return2 = ""

    if len(sys.argv) > 2:
        args_to_return1 = args.INFILE1
        args_to_return2 = args.INFILE2
    else:
        args_to_return1 = infile1
        args_to_return2 = infile2

    return args_to_return1, args_to_return2


def get_cli_args():
    """
    Get Command Line Argument function to read arguments from command
    line using argparse
    :return: Argument Parser object with all the required options
    """
    parser = argparse.ArgumentParser(description="Combine on gene name "
                                                 "and count the category "
                                                 "occurrence")
    parser.add_argument("-i1", "--infile1",
                        dest="INFILE1",
                        type=str,
                        help="Path to the gene description file to open",
                        required=False)

    parser.add_argument("-i2", "--infile2",
                        dest="INFILE2",
                        type=str,
                        help="Path to the gene category to open",
                        required=False)

    return parser.parse_args()


if __name__ == "__main__":
    main()
