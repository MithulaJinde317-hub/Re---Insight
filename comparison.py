# comparison.py

import re
from enzymes import enzymes
from degenerate import convert_to_regex
from utils import reverse_complement


def find_sites(sequence):
    """
    Find restriction sites using regex (forward strand)
    """
    results = {}

    for enzyme, pattern in enzymes.items():
        regex_pattern = convert_to_regex(pattern)
        matches = [m.start() for m in re.finditer(regex_pattern, sequence)]
        results[enzyme] = matches

    return results


def find_sites_both_strands(sequence):
    """
    Scan both forward and reverse complement strands
    """
    rc_seq = reverse_complement(sequence)

    forward = find_sites(sequence)
    reverse = find_sites(rc_seq)

    return forward, reverse


def compare_sequences(seq1, seq2):
    """
    Identify enzymes that differentiate two sequences
    """
    res1 = find_sites(seq1)
    res2 = find_sites(seq2)

    unique_to_seq1 = []
    unique_to_seq2 = []

    for enzyme in res1:
        if res1[enzyme] and not res2[enzyme]:
            unique_to_seq1.append(enzyme)
        elif res2[enzyme] and not res1[enzyme]:
            unique_to_seq2.append(enzyme)

    return unique_to_seq1, unique_to_seq2
