"""
calculate descriptive statistics
"""

import sys
import math

NUMBERS = []


def calc_average():
    """
    Stats Method
    :return: Average of Numbers list
    """
    return sum(NUMBERS) / len(NUMBERS)


def calc_sqr_dev():
    """
    Stats Method
    :return: Square Deviation of Numbers list
    """
    return [(x - calc_average()) ** 2 for x in NUMBERS]


def calc_variance():
    """
    Stats Method
    :return: Variance of Numbers list
    """
    try:
        variance = sum(calc_sqr_dev()) / (len(NUMBERS) - 1)
    except ZeroDivisionError:
        variance = 0
    return variance


def calc_deviation():
    """
    Stats Method
    :return: Standard Deviation of Numbers list
    """
    return math.sqrt(calc_variance())


def calc_median():
    """
    Stats Method
    :return: Median of Numbers list
    """
    length_of_numbers = len(NUMBERS)
    NUMBERS.sort()

    if length_of_numbers % 2 == 0:
        median1 = NUMBERS[length_of_numbers // 2]
        median2 = NUMBERS[length_of_numbers // 2 - 1]
        median = (median1 + median2) / 2
    else:
        median = NUMBERS[length_of_numbers // 2]

    return median


def calc_statistics(column_to_parse, line_num):
    """
    Calculate Stats
    :param column_to_parse: Number of Column from the file
    :param line_num: Total number of variables passed
    :return: Print all the statements with stats
    """
    print()
    print(f"    Column: {column_to_parse:<4}")
    print("\n")
    print(f"        Count        =    {float(line_num):>8.3f}")
    print(f"        ValidNum     =    {float(len(NUMBERS)):>8.3f}")
    print(f"        Average      =    {float(calc_average()):>8.3f}")
    print(f"        Maximum      =    {float(max(NUMBERS)):>8.3f}")
    print(f"        Minimum      =    {float(min(NUMBERS)):>8.3f}")
    print(f"        Variance     =    {float(calc_variance()):>8.3f}")
    print(f"        Std Dev      =    {float(calc_deviation()):>8.3f}")
    print(f"        Median       =    {float(calc_median()):>8.3f}")
    print()

def add_number(num, line_num):
    """
    Adding number to list NUMBERS
    :param num: number from each line one by one
    :param line_num: number of line in file from which number is passed
    :return: Complete list of NUMBERS
    """
    try:
        if math.isnan(float(num)):
            pass
        else:
            NUMBERS.append(float(num))
    except ValueError:
        print()
        print(f"Skipping line number {line_num} : could not convert string to float: {num}")


def open_file(file, column_to_parse):
    """
    main function to open file and pass each number one by one
    :param file: name of the file
    :param column_to_parse: column to extract on which statistics is going to run
    :return: Start the calculate statistics function if there is entries in NUMBERS list
    """

    total_variables = 0

    with open(file, "r") as infile:
        for line_num, line in enumerate(infile, 1):
            try:
                num = line.split("\t")[column_to_parse]
                add_number(num, line_num)
                total_variables += 1
            except IndexError:
                print()
                print(
                    f"Exiting: There is no valid 'list index' in column {column_to_parse}"
                    f" in line {line_num} in file: {file}")
                print()
                sys.exit(1)

    if len(NUMBERS) == 0:
        print()
        print(f"Error: There were no valid number(s) in column {column_to_parse} in file: {file}")
        print()
    else:
        calc_statistics(column_to_parse, total_variables)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print()
        print("Error: Please provide two input with this file, first should be file"
              " name and second should be column name")
        print()
        sys.exit(1)
    else:
        open_file(str(sys.argv[1]), int(sys.argv[2]))
