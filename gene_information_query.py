"""
Give the Host and Gene name to print the express gene names
"""
import argparse
import re
import sys
from assignment5 import my_io
from assignment5 import config


def main():
    """
    Main function
    :return: Prints out Expressed genes in Mammal in STD.OUT format
    """
    args = get_cli_args()
    # function to check for passed arguments
    temp_host, gene = check_passed_args(args)
    # getting scientific name
    host = modify_host_name(temp_host)
    # file name and absolute path
    file = "/".join((config.get_unigene_directory(),
                     host, gene + "." + config.get_unigene_extension()))
    # checking if file exist in directory or not
    _check_file_exist(file, host, gene)
    # List of expressed genes sorted alphabetically
    tissue_strig = get_gene_data(file)
    # Print output on STD.OUT
    print_ouput(temp_host, gene, tissue_strig)


def print_ouput(host, gene, tissue_string):
    """
    Print Expressed gene name on STD OUT
    :param host: Name of the host
    :param gene: Name of the gene passed
    :param tissue_string: sorted list of expressed genes
    :return: None
    """
    print(f"In {host}, There are {len(tissue_string)} "
          f"tissues that {gene} is expressed in:\n")

    for i, value in enumerate(tissue_string, start=1):
        print(f"{i}. {value.title()}")


def get_gene_data(gene_file):
    """
    Get Epressed gene names from host file.
    :param gene_file: Absolute path to gene file of host
    :return: Sorted list of expresssed genes in host
    """
    fh_in = my_io.get_fh(gene_file, "r")

    tissue_strig = []

    for line in fh_in:
        if re.search("EXPRESS", line):
            line = line.replace("\n", "")
            line = re.sub('[A-Z]', "", line)
            tissue_strig = line.split("|")
            tissue_strig = [x.strip(' ') for x in tissue_strig]

    my_io.get_fh(fh_in, "close")

    return sorted(tissue_strig)


def _check_file_exist(file, temp_host, gene):
    # check for the existence of file
    if my_io.is_valid_gene_file_name(file):
        # using f-strings
        print(f"\nFound Gene {gene} for {temp_host}")
    else:
        print("Not found")
        print(f"Gene {gene} does not exist for {temp_host}. "
              f"exiting now...", file=sys.stderr)
        sys.exit()


def modify_host_name(host_name):
    """
    Get Scientific name from dictionary exist in config file
    if name with "_" is passed it can be treated as scientifc name
    :param host_name: Argument passed in CLI otions
    :return: Scientific name for Host
    """
    scientific_name = ""

    if "_" in host_name:
        scientific_name = host_name
    else:
        if host_name.lower() in list(config.get_host_keywords().keys()):
            scientific_name = config.get_host_keywords()[host_name.lower()]
        else:
            _print_host_directories()
            scientific_name = host_name

    return scientific_name


def _print_host_directories():
    """
    Internal function to print the name of valid Hosts data available
    in directory scientific and non-scientific both (case-insensitive)
    :return: NONE exits the program
    """

    print("\nEither the Host Name you are searching for is not in the database"
          "\nor If you are trying to use the scientific name please "
          "put the name in double quotes:\n"
          "\n\"Scientific name\"\n"
          "\nHere is a (non-case sensitive) list of available Hosts by scientific name\n")

    for i, value in enumerate(set(list(config.get_host_keywords().values())), start=1):
        print(f"{i}. {value}")

    print("\nHere is a (non-case sensitive) list of available Hosts by common name\n")

    for i, key in enumerate(list(config.get_host_keywords().keys()), start=1):
        print(f"{i}. {key.title()}")


def check_passed_args(args):
    """
    Check how many arguments passed, if NONE: return
    default file options
    :param args: Argparse file arguments, passed in CLI
    :return: Names of the files to open
    """

    host = "Homo_sapiens"
    gene = "TGM1"
    args_to_return1 = ""
    args_to_return2 = ""

    if len(sys.argv) > 2:
        args_to_return1 = args.HOST
        args_to_return2 = args.GENE
    else:
        args_to_return1 = host
        args_to_return2 = gene

    return args_to_return1, args_to_return2


def get_cli_args():
    """
    Get Command Line Argument function to read arguments from command
    line using argparse
    :return: Argument Parser object with all the required options
    """
    parser = argparse.ArgumentParser(description="Give the Host and Gene name")

    parser.add_argument("-host",
                        dest="HOST",
                        type=str,
                        help="Name of Host",
                        required=False)

    parser.add_argument("-gene",
                        dest="GENE",
                        type=str,
                        help="Name of Gene",
                        required=False)

    return parser.parse_args()


if __name__ == "__main__":
    main()
