# degenerate.py

# Mapping of IUPAC degenerate bases to regex patterns
degenerate_map = {
    "A": "A",
    "T": "T",
    "G": "G",
    "C": "C",
    "R": "[AG]",
    "Y": "[CT]",
    "S": "[GC]",
    "W": "[AT]",
    "K": "[GT]",
    "M": "[AC]",
    "B": "[CGT]",
    "D": "[AGT]",
    "H": "[ACT]",
    "V": "[ACG]",
    "N": "[ATGC]"
}

def convert_to_regex(pattern):
    """
    Convert a DNA pattern with degenerate bases into regex
    """
    return "".join(degenerate_map.get(base, base) for base in pattern)
