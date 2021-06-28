"""
Test Suite for NUCLEOTIDE_STATS_FROM_FASTA.py
"""
from os import path
import pytest

# pylint: disable=C0116
# pylint: disable=C0103

from nucleotide_statistics_from_fasta import _check_size_of_lists, \
    get_header_and_sequence_lists, get_fh, print_sequence_stats, _get_accession, \
    _get_nt_occurrence

LIST_HEADER = ['>EUG123', '>EUG124', ">EUG126", ">EUG128"]
LIST_SEQS = ['ACGTAC', 'ACGTCC', 'ACCGGT', 'AAAACT']
LIST_SEQS_NOT_EQUAL = ['ACGTAC', 'ACGTCC', 'ACCGGT']
FILE_OUT = get_fh("test_influenza_stats.txt", "w")
FILE_HANDLE = get_fh("influenza.fasta", "r")


def test_print_sequence_stats():
    print_sequence_stats(LIST_HEADER, LIST_SEQS, FILE_OUT)
    assert path.exists("test_influenza_stats.txt")


def test__get_accession():
    assert _get_accession(LIST_HEADER[0]) == "EUG123"
    assert _get_accession(LIST_HEADER[1]) == "EUG124"


def test__get_nt_occurrence():
    assert _get_nt_occurrence("A", LIST_SEQS[3]) == 4
    assert _get_nt_occurrence("C", LIST_SEQS[2]) == 2
    with pytest.raises(SystemExit):
        _get_nt_occurrence("Y", LIST_SEQS[3])


def test__check_size_of_lists():
    assert _check_size_of_lists(LIST_HEADER, LIST_SEQS)
    with pytest.raises(SystemExit):
        _check_size_of_lists(LIST_HEADER, LIST_SEQS_NOT_EQUAL)


def test_get_header_and_sequence_lists():
    header_list, seq_list = get_header_and_sequence_lists(FILE_HANDLE)
    assert len(header_list) == 91830
    assert len(seq_list) == 91830


def test_get_fh_4_IOError():
    # does it raise IOError
    # this should exit
    with pytest.raises(SystemExit):
        get_fh("does_not_exist.txt", "r")


def test_get_fh_4_ValueError():
    # does it raise IOError
    # this should exit
    with pytest.raises(SystemExit):
        get_fh("ss.influenza.fasta", "rrr")
