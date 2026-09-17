import numpy as np

seq1 = 'ACGTATCGCGTATA'
seq2 = 'GATGCGTATCG'

match_score = 2
mismatch_score = -1
gap = -2

align_table = np.zeros((len(seq1) + 1, len(seq2) + 1), dtype=int)

for i in range(len(seq1)):
    align_table[i][0] = i * gap

for j in range(len(seq2)):
    align_table[0][j] = j * gap

for i in range(1, len(seq1) + 1):
    for j in range(1, len(seq2) + 1):
        match_mismatch_score = match_score if seq1[i - 1] == seq2[j - 1] else mismatch_score #since on table, the strings start from 1, but in the actual strings they start from 0, we need to subtract 1 from i and j to get the correct index in the strings.    
        align_table[i][j] = max(
            align_table[i - 1][j - 1] + match_mismatch_score,
            align_table[i - 1][j] + gap,
            align_table[i][j - 1] + gap
        )

cell = align_table[len(seq1)][len(seq2)]
i = len(seq1)
j = len(seq2)

align1 = ""
align2 = ""

while i > 1 and j > 1:
    
    cell  = max(
        align_table[i - 1][j - 1],
        align_table[i - 1][j],
        align_table[i][j - 1]
    )

    if cell == align_table[i - 1][j - 1]:
        align1 += seq1[i-1]
        align2 += seq2[j-1]
        i -= 1
        j -= 1
    elif cell == align_table[i - 1][j]:
        i -= 1
        align1 += seq1[i-1]
        align2 += "-"
    else:
        align1 += "-"
        align2 += seq2[j-1]
        j -= 1

while i > 0:
    align1 += seq1[i-1]
    align2 += "-"
    i -= 1
while j > 0:
    align1 += "-"
    align2 += seq2[j-1]
    j -= 1

# Reverse the alignments since we built them backwards
print("Final Alignment: ")
print(align1[::-1])
print(align2[::-1])
print(' ')
print("Final Score: ")
print(align_table)