# utils.py

def reverse_complement(seq):
    """
    Generate reverse complement of DNA sequence
    """
    complement = str.maketrans("ATGC", "TACG")
    return seq.upper().translate(complement)[::-1]


def read_fasta(file_path):
    """
    Read sequence from FASTA file
    """
    sequence = ""
    with open(file_path, "r") as f:
        for line in f:
            if not line.startswith(">"):
                sequence += line.strip()
    return sequence.upper()


def simulate_fragments(sequence, cut_positions):
    """
    Simulate restriction digestion fragments
    Returns fragment lengths
    """
    if not cut_positions:
        return [len(sequence)]

    fragments = []
    prev = 0

    for pos in sorted(cut_positions):
        fragments.append(sequence[prev:pos])
        prev = pos

    fragments.append(sequence[prev:])

    return [len(f) for f in fragments]
