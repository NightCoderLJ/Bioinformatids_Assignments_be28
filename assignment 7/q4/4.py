sequences = {
    "Seq 1": "RATPTRWPVGCFNRPWTKWSYDEALDGIKAAGYAWTGLLTASKPSLHH",
    "Seq 2": "ATATPEYLAALKQKSRHAAAAAVMMGLAAIGAAIGIGILGGKFLEGAARQPDLIPLLRTQFFIVMGLVDAIPMIAVGLGLYVMFAVA",
    "Seq 3": "AADVSAAVGATGQSGMTYRLGLSWDWDKSWWQTSTGRLTGYWDAGYTYWEGGDEGAGKHSLSFAPVFVYEFAGDSIKPFIEAGIGVAAFSGTRVGDQNLGSSLNFEDRIGAGLKFANGQSVGVRAIHYSNAGLKQPNDGIESYSLFYKIPI"
}

amino_acids = "ACDEFGHIKLMNPQRSTVWY"

for name, seq in sequences.items():
    N = len(seq)
    
    counts = {aa: seq.count(aa) for aa in amino_acids}
    
    pair_counts = {}
    for aa1 in amino_acids:
        for aa2 in amino_acids:
            pair = aa1 + aa2
            pair_counts[pair] = sum(1 for k in range(N-1) if seq[k:k+2] == pair)
            
    metrics_a, metrics_b, metrics_c = [], [], []
    
    with open(f"{name}_matrix_a.txt", "w") as fa, \
         open(f"{name}_matrix_b.txt", "w") as fb, \
         open(f"{name}_matrix_c.txt", "w") as fc:
        
        header = "AA," + ",".join(amino_acids) + "\n"
        fa.write(header)
        fb.write(header)
        fc.write(header)
        
        for aa1 in amino_acids:
            row_a, row_b, row_c = [aa1], [aa1], [aa1]
            
            for aa2 in amino_acids:
                pair = aa1 + aa2
                nij = pair_counts[pair]
                ni = counts[aa1]
                nj = counts[aa2]
                
                val_a = (nij * 100 / (ni + nj)) if (ni + nj) > 0 else 0
                metrics_a.append((pair, val_a))
                row_a.append(str(round(val_a, 2)))
                
                val_b = (nij * 100 / (N - 1)) if (N - 1) > 0 else 0
                metrics_b.append((pair, val_b))
                row_b.append(str(round(val_b, 2)))
                
                val_c = (nij * 100 / (ni * nj)) if (ni * nj) > 0 else 0
                metrics_c.append((pair, val_c))
                row_c.append(str(round(val_c, 2)))
            
            fa.write(",".join(row_a) + "\n")
            fb.write(",".join(row_b) + "\n")
            fc.write(",".join(row_c) + "\n")
            
    top_a = sorted(metrics_a, key=lambda x: x[1], reverse=True)[:10]
    top_b = sorted(metrics_b, key=lambda x: x[1], reverse=True)[:10]
    top_c = sorted(metrics_c, key=lambda x: x[1], reverse=True)[:10]
    
    print(f"{name}, Top 10 (a), " + ", ".join([f"{p[0]}: {round(p[1],2)}" for p in top_a]))
    print(f"{name}, Top 10 (b), " + ", ".join([f"{p[0]}: {round(p[1],2)}" for p in top_b]))
    print(f"{name}, Top 10 (c), " + ", ".join([f"{p[0]}: {round(p[1],2)}" for p in top_c]))