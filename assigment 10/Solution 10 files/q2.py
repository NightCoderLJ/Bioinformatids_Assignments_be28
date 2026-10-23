# q2.py - position weight matrix for the 7 aligned sequences (BT3040, Assignment 10)
# W(a,i) = ln[ (n(a,i) + p) / ((N + 1) * p) ],  p = 1/20 (equal background), N = 7
import math

seqs = ["MVLSPADKTNVKGKVGAHAGEYGAAAW",
        "MKRLPADPPCVKGKVKAKAGDYGATTW",
        "MALSAADKTNVKSKVGGHAGEYGAATS",
        "MVLSAADKTNVKSKAGGNAGEWWAAAW",
        "MVLSAADKTNVKSKVLANAGEFGAAAW",
        "ALLPIRTTYHKKCASGHIPEEKDLNNV",
        "DEASSLKGHHIKKLEADALLIPLSASS"]
AA = "ACDEFGHIKLMNPQRSTVWY"
N, L = len(seqs), len(seqs[0])
assert all(len(s) == L for s in seqs)
p = 1 / len(AA)

count = {a: [sum(s[i] == a for s in seqs) for i in range(L)] for a in AA}
W = {a: [math.log((count[a][i] + p) / ((N + 1) * p)) for i in range(L)] for a in AA}

print(f"N = {N} sequences, L = {L} positions, p = 1/20")
print(f"absent residue -> W = ln(p/(8p)) = {math.log(1/8):.2f}\n")
for lo, hi in [(0, 14), (14, L)]:
    print("     " + "".join(f"{i + 1:>6}" for i in range(lo, hi)))
    for a in AA:
        print(f"  {a}  " + "".join(f"{W[a][i]:6.2f}" for i in range(lo, hi)))
    print()

best = "".join(max(AA, key=lambda a: W[a][i]) for i in range(L))
print("Highest-weight residue per position:", best)
for k, s in enumerate(seqs, 1):
    print(f"Score of seq {k}: {sum(W[s[i]][i] for i in range(L)):6.2f}")
