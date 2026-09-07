# Q2 - Score of the alignment AATCTATA / AAG--ATA

seq1 = "AATCTATA"
seq2 = "AAG--ATA"

match = 1
mismatch = 0
origination = -2
length = -1

score = 0
in_gap = False

for a, b in zip(seq1, seq2):
    if a == "-" or b == "-":
        if not in_gap:              # first column of a new gap
            score += origination
            in_gap = True
        score += length
    else:
        in_gap = False
        score += match if a == b else mismatch

print(seq1)
print(seq2)
print("Alignment score:", score)
