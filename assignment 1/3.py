def get_complement(sequence):
    complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    sequence = sequence.upper()
    try:
        complement = "".join(complement_map[base] for base in sequence)
        return complement
    except KeyError as e:
        return f"Invalid base found: {e}"

if __name__ == "__main__":
    seq = input("Enter DNA sequence: ")
    print("Complementary strand:", get_complement(seq))
