"""
Test Suite for PDB_FASTA_SPLITTER
"""
import pytest

# pylint: disable=C0116
# pylint: disable=C0103

from pdb_fasta_splitter import write_in_file, _check_size_of_lists, \
    get_header_and_sequence_lists, get_fh

LIST_HEADER = ['>1sequence', '>1secstr', ">2sequence", ">2secstr"]
LIST_SEQS = ['ACGTAC', 'ACGTCC', 'ACCGGT', 'AAAACT']
LIST_SEQS_NOT_EQUAL = ['ACGTAC', 'ACGTCC', 'ACCGGT']
FILE_HANDLE = get_fh("ss.txt", "r")
AMINO_ACID = get_fh("test_pdb_protein.fasta", "w")
SEC_STR = get_fh("test_pdb_ss.fasta", "w")


def test_write_in_file():
    count_amino, count_sec_str = write_in_file(AMINO_ACID, SEC_STR, LIST_HEADER, LIST_SEQS)
    assert count_amino == 2
    assert count_sec_str == 2


def test__check_size_of_lists():
    assert _check_size_of_lists(LIST_HEADER, LIST_SEQS)
    with pytest.raises(SystemExit):
        _check_size_of_lists(LIST_HEADER, LIST_SEQS_NOT_EQUAL)


def test_get_header_and_sequence_lists():
    header_list, seq_list = get_header_and_sequence_lists(FILE_HANDLE)
    assert len(header_list) == 332484
    assert len(seq_list) == 332484


def test_get_fh_4_IOError():
    # does it raise IOError
    # this should exit
    with pytest.raises(SystemExit):
        get_fh("does_not_exist.txt", "r")


def test_get_fh_4_ValueError():
    # does it raise IOError
    # this should exit
    with pytest.raises(SystemExit):
        get_fh("ss.txt", "rrr")
