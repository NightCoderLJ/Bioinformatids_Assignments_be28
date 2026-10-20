import math
from collections import Counter

sequence = "LGASGIAAFAFGSTAILIILFNMAAEVHFDPLQFFRQFFWLGLYPPKAQYGMGIPPLHDGGWWLMAGLFMTLSLGSWWIRVYSRARALGLGTHIAWNFAAAIFFVLCIGCIHPTLVGSWSEGVPFGIWPHIDWLTAFSIRYGNFYYCPWHGFSIGFAYGCGLLFAAHGATILAVARFGGDREIEQITDRGTAVERAALFW"
sec_struct = "XHHHHHHHHHHHHHHHHHHHHHHHHHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHXXHHHHHHHHHHHHHHHHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXHHHHHHHHHHHHHHHHHHHHHHHHHXXXXXXXXXXXXXXXXXXXXXXXXXXX"

N_total = len(sequence)
N_H = sec_struct.count('H')


total_counts = Counter(sequence)
helix_counts = Counter([sequence[i]
                       for i in range(N_total) if sec_struct[i] == 'H'])

print(f"{'AA'} {'Total'} {'Helix'} {'Propensity (Pa)'} {'Info Content (Ia)'}")
print("-" * 60)

for aa in "ACDEFGHIKLMNPQRSTVWY":
    n_a = total_counts.get(aa, 0)
    n_aH = helix_counts.get(aa, 0)

    if n_a == 0:
        continue

    P_a = (n_aH / N_H) / (n_a / N_total)
    I_a = math.log2(P_a) if P_a > 0 else float('-inf')

    print(f"{aa} {n_a} {n_aH} {P_a} {I_a}")
