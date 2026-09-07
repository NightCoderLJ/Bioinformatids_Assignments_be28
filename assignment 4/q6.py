# Q6 - Local alignment of ACGTATCGCGTATA and GATGCGTATCG (Smith-Waterman)

seq1 = "ACGTATCGCGTATA"
seq2 = "GATGCGTATCG"

match = 2
mismatch = -1
gap = -2

n, m = len(seq1), len(seq2)

# build the score table; negative scores are reset to zero
table = [[0] * (m + 1) for _ in range(n + 1)]
best, best_i, best_j = 0, 0, 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        pair = match if seq1[i - 1] == seq2[j - 1] else mismatch
        table[i][j] = max(0,
                          table[i - 1][j - 1] + pair,
                          table[i - 1][j] + gap,
                          table[i][j - 1] + gap)
        if table[i][j] > best:
            best, best_i, best_j = table[i][j], i, j

print("Partial alignment score table")
print("    " + "".join(f"{c:>4}" for c in "-" + seq2))
for i in range(n + 1):
    label = "-" if i == 0 else seq1[i - 1]
    print(f"{label:>4}" + "".join(f"{v:>4}" for v in table[i]))

# traceback from the highest cell until a zero is reached
align1, align2 = "", ""
i, j = best_i, best_j
while i > 0 and j > 0 and table[i][j] > 0:
    pair = match if seq1[i - 1] == seq2[j - 1] else mismatch
    if table[i][j] == table[i - 1][j - 1] + pair:
        align1, align2 = seq1[i - 1] + align1, seq2[j - 1] + align2
        i, j = i - 1, j - 1
    elif table[i][j] == table[i - 1][j] + gap:
        align1, align2 = seq1[i - 1] + align1, "-" + align2
        i -= 1
    else:
        align1, align2 = "-" + align1, seq2[j - 1] + align2
        j -= 1

print("\nBest local alignment")
print(align1)
print(align2)
print(f"Position: seq1 {i + 1}-{best_i}, seq2 {j + 1}-{best_j}")
print("Alignment score:", best)
