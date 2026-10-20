target_seq = "KVFGRCELAAAMKRHGLDNYRGYSLGNWVCAAKFESNFNTQATNRNTDGSTDYGILQINSRWWCNDGRTPGSRNLCNIPCSALLSSDITASVNCAKKIVSDGNGMNAWVAWRNRCKGTDVQAWIRGCRL"


helix_scores = {
    'E': 1, 'A': 1, 'L': 1, 'H': 1, 'M': 1, 'Q': 1, 'W': 1, 'V': 1, 'F': 1,
    'K': 0.5, 'I': 0.5,
    'D': 0, 'T': 0, 'S': 0, 'R': 0, 'C': 0,
    'N': -1, 'Y': -1, 'P': -1, 'G': -1
}

strand_scores = {
    'M': 1, 'V': 1, 'I': 1, 'C': 1, 'Y': 1, 'F': 1, 'Q': 1, 'L': 1, 'T': 1, 'W': 1,
    'A': 0.5,
    'R': 0, 'G': 0, 'D': 0,
    'K': -1, 'S': -1, 'H': -1, 'N': -1, 'P': -1, 'E': -1
}

p_alpha = {
    'E': 1.53, 'A': 1.45, 'L': 1.34, 'H': 1.24, 'M': 1.20, 'Q': 1.17, 'W': 1.14,
    'V': 1.14, 'F': 1.12, 'K': 1.07, 'I': 1.00, 'D': 0.98, 'T': 0.82, 'S': 0.79,
    'R': 0.79, 'C': 0.77, 'N': 0.73, 'Y': 0.61, 'P': 0.59, 'G': 0.53
}


p_beta = {
    'M': 1.67, 'V': 1.65, 'I': 1.60, 'C': 1.30, 'Y': 1.29, 'F': 1.28, 'Q': 1.23,
    'L': 1.22, 'T': 1.20, 'W': 1.19, 'A': 0.97, 'R': 0.90, 'G': 0.81, 'D': 0.80,
    'K': 0.74, 'S': 0.72, 'H': 0.71, 'N': 0.65, 'P': 0.62, 'E': 0.26
}


def find_alpha_helices(seq):
    """
    Finds alpha helices using a 6-residue window (threshold >= 4) 
    and extends based on the 4-residue boundary average.
    """
    found_segments = set()

    for i in range(len(seq) - 5):
        window = seq[i:i+6]
        score = sum(helix_scores[aa] for aa in window)

        if score >= 4.0:
            start = i
            end = i + 5

            while start > 0:
                left_boundary = seq[start-1: start+3]
                if len(left_boundary) == 4 and sum(p_alpha[aa] for aa in left_boundary) >= 4.0:
                    start -= 1
                else:
                    break

            while end < len(seq) - 1:
                right_boundary = seq[end-2: end+2]
                if len(right_boundary) == 4 and sum(p_alpha[aa] for aa in right_boundary) >= 4.0:
                    end += 1
                else:
                    break

            found_segments.add((start, end, seq[start:end+1]))

    return sorted(list(found_segments))


def find_beta_strands(seq):
    """
    Finds beta strands using a 5-residue window (threshold >= 3)
    and extends based on the 3-residue boundary average.
    """
    found_segments = set()

    for i in range(len(seq) - 4):
        window = seq[i:i+5]
        score = sum(strand_scores[aa] for aa in window)

        if score >= 3.0:
            start = i
            end = i + 4

            while start > 0:
                left_boundary = seq[start-1: start+2]
                if len(left_boundary) == 3 and sum(p_beta[aa] for aa in left_boundary) >= 3.0:
                    start -= 1
                else:
                    break

            while end < len(seq) - 1:
                right_boundary = seq[end-1: end+2]
                if len(right_boundary) == 3 and sum(p_beta[aa] for aa in right_boundary) >= 3.0:
                    end += 1
                else:
                    break

            found_segments.add((start, end, seq[start:end+1]))

    return sorted(list(found_segments))


print("IDENTIFIED ALPHA HELICES: ")
helices = find_alpha_helices(target_seq)
for start, end, segment in helices:
    print(f"Indices {start + 1}-{end + 1}: {segment}")

print("\nIDENTIFIED BETA STRANDS: ")
strands = find_beta_strands(target_seq)
for start, end, segment in strands:
    print(f"Indices {start + 1}-{end + 1}: {segment}")
