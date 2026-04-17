import re
from enzymes import enzymes
from degenerate import convert_to_regex

def find_sites(sequence):
    results = {}

    for enzyme, pattern in enzymes.items():
        regex_pattern = convert_to_regex(pattern)
        matches = [m.start() for m in re.finditer(regex_pattern, sequence)]
        
        results[enzyme] = matches

    return results

def reverse_complement(seq):
    complement = str.maketrans("ATGC", "TACG")
    return seq.translate(complement)[::-1]

def find_sites_both_strands(sequence):
    rc_seq = reverse_complement(sequence)

    forward = find_sites(sequence)
    reverse = find_sites(rc_seq)

    return forward, reverse
