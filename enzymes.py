# enzymes.py

# Dictionary of restriction enzymes and their recognition sequences
# Includes some degenerate patterns (IUPAC codes)

enzymes = {
    "EcoRI": "GAATTC",
    "HindIII": "AAGCTT",
    "BamHI": "GGATCC",
    "HaeIII": "GGCC",
    "NciI": "CCSGG",   # S = G or C
    "AluI": "AGCT",
    "TaqI": "TCGA",
    "NotI": "GCGGCCGC"
}
