# Paste your tool's exact aligned output here (including any '-' characters)
s1 = "MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH"
s2 = "MVHWTAEEKQLITGLWGKVNVAECGAEALARLLIVYPWTQRFFASFGNLSSPTAILGNPMVRAHGKKVLTSFGDAVKNLDNIKNTFAQLSELHCDKLHVDPENFRLLGDILIIVLAAHFSKDFTPECQAAWQKLVRVVAHALAHKYH"

# The true original length of the unaligned Human HBB query sequence
orig_query_len = 147 

# Grouped by biochemical properties (with Proline added to Polar)
similar_groups = [
    "DE",      # Negative (Acidic)
    "RKH",     # Positive (Basic)
    "STNQP",   # Polar (Uncharged)
    "AVIL",    # Aliphatic (Non-polar)
    "FYW",     # Aromatic
    "CM"       # Sulfur-containing
]

matches = 0
similars = 0
gaps = 0

# 1. Dynamically calculate the length of the alignment block
alignment_len = len(s1)

for i in range(alignment_len):
    c1 = s1[i]
    c2 = s2[i]
    
    if c1 == "-" or c2 == "-":
        gaps += 1
    elif c1 == c2:
        matches += 1
        similars += 1  
    else:
        for g in similar_groups:
            if c1 in g and c2 in g:
                similars += 1
                break

# 2. Dynamically count only the actual amino acid letters in the query (ignoring gaps)
query_aligned_bases = sum(1 for ch in s1 if ch != "-")

# Calculate final percentages
ident_pct = (matches / alignment_len) * 100
sim_pct = (similars / alignment_len) * 100
gap_pct = (gaps / alignment_len) * 100
cov_pct = (query_aligned_bases / orig_query_len) * 100

print(f"Alignment Length: {alignment_len}")
print(f"Sequence Identity: {ident_pct:.2f}%")
print(f"Sequence Similarity: {sim_pct:.2f}%")
print(f"Gap Percentage: {gap_pct:.2f}%")
print(f"Query Coverage: {cov_pct:.2f}%")