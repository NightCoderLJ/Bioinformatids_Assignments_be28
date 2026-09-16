seq1 = "AATCTATA"
seq2 = "AAG--ATA"


match_score = 1
mismatch_score = 0
origin_penalty = -2
length_penalty = -1

gap_started = False

score = 0


for i in range(len(seq1)):
    char1 = seq1[i]
    char2 = seq2[i]

    if char1 == char2:
        score += match_score
    else:
        score += mismatch_score

    if char1 == '-' or char2 == '-':
        if not gap_started:
            score += origin_penalty
            score += length_penalty
            gap_started = True
        else:
            score += length_penalty
    else:
        gap_started = False


print(score)

