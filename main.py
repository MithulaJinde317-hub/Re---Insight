# main.py

from comparison import compare_sequences, find_sites
from utils import read_fasta, simulate_fragments

def main():
    print("\n=== RE-Insight: Restriction Enzyme Analysis Tool ===\n")

    choice = input("Choose input type:\n1. Manual input\n2. FASTA file\nEnter choice (1/2): ")

    if choice == "1":
        seq1 = input("\nEnter wild-type sequence: ").upper()
        seq2 = input("Enter mutant sequence: ").upper()

    elif choice == "2":
        file1 = input("Enter path for wild-type FASTA: ")
        file2 = input("Enter path for mutant FASTA: ")

        seq1 = read_fasta(file1)
        seq2 = read_fasta(file2)

    else:
        print("Invalid choice")
        return

    # Compare sequences
    unique1, unique2 = compare_sequences(seq1, seq2)

    print("\n--- RESULTS ---")

    print("\nEnzymes cutting ONLY wild-type:")
    print(unique1 if unique1 else "None")

    print("\nEnzymes cutting ONLY mutant:")
    print(unique2 if unique2 else "None")

    # Optional: show fragment simulation for first enzyme
    from comparison import find_sites

    sites = find_sites(seq1)

    if unique1:
        enzyme = unique1[0]
        print(f"\nFragment simulation for {enzyme} (wild-type):")

        fragments = simulate_fragments(seq1, sites[enzyme])
        print("Fragment sizes:", fragments)


if __name__ == "__main__":
    main()
