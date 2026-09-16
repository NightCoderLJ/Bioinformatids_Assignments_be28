import numpy as np


seq1 = "ACGTATCGCGTATA"
seq2 = "GATGCGTATCG"

match_score = 2
mismatch_score = -1
gap = -2

align_table = np.zeros((len(seq1) + 1, len(seq2) + 1), dtype=int)

max_score = 0

for i in range(1, len(seq1) + 1):
    for j in range(1, len(seq2) + 1):
        match_or_mismatch = match_score if seq1[i-1] == seq2[j-1] else mismatch_score

        diag_score = align_table[i-1][j-1] + match_or_mismatch
        up_score = align_table[i-1][j] + gap
        left_score = align_table[i][j-1] + gap

       
        align_table[i][j] = max(0, diag_score, up_score, left_score)
        
     
        if align_table[i][j] > max_score:
            max_score = align_table[i][j]
            max_pos = (i, j)


i , j = max_pos
cell = align_table[i][j]

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