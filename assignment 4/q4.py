# Q4 - Global alignment of ACAGTCGAACG and ACCGTCCG (Needleman-Wunsch)

seq1 = "ACAGTCGAACG"
seq2 = "ACCGTCCG"

match = 2
mismatch = -1
gap = -2

n, m = len(seq1), len(seq2)

# build the score table
table = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    table[i][0] = i * gap
for j in range(1, m + 1):
    table[0][j] = j * gap

for i in range(1, n + 1):
    for j in range(1, m + 1):
        pair = match if seq1[i - 1] == seq2[j - 1] else mismatch
        table[i][j] = max(table[i - 1][j - 1] + pair,
                          table[i - 1][j] + gap,
                          table[i][j - 1] + gap)

print("Partial alignment score table")
print("     " + "".join(f"{c:>5}" for c in "-" + seq2))
for i in range(n + 1):
    label = "-" if i == 0 else seq1[i - 1]
    print(f"{label:>5}" + "".join(f"{v:>5}" for v in table[i]))

# traceback from the bottom right corner
align1, align2 = "", ""
i, j = n, m
while i > 0 or j > 0:
    pair = match if (i and j and seq1[i - 1] == seq2[j - 1]) else mismatch
    if i and j and table[i][j] == table[i - 1][j - 1] + pair:
        align1, align2 = seq1[i - 1] + align1, seq2[j - 1] + align2
        i, j = i - 1, j - 1
    elif i and table[i][j] == table[i - 1][j] + gap:
        align1, align2 = seq1[i - 1] + align1, "-" + align2
        i -= 1
    else:
        align1, align2 = "-" + align1, seq2[j - 1] + align2
        j -= 1

print("\nOptimal alignment")
print(align1)
print(align2)
print("Alignment score:", table[n][m])
