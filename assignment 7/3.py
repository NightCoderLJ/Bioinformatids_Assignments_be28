import math

sequences = {
    "Seq 1": "RATPTRWPVGCFNRPWTKWSYDEALDGIKAAGYAWTGLLTASKPSLHH",
    "Seq 2": "ATATPEYLAALKQKSRHAAAAAVMMGLAAIGAAIGIGILGGKFLEGAARQPDLIPLLRTQFFIVMGLVDAIPMIAVGLGLYVMFAVA",
    "Seq 3": "AADVSAAVGATGQSGMTYRLGLSWDWDKSWWQTSTGRLTGYWDAGYTYWEGGDEGAGKHSLSFAPVFVYEFAGDSIKPFIEAGIGVAAFSGTRVGDQNLGSSLNFEDRIGAGLKFANGQSVGVRAIHYSNAGLKQPNDGIESYSLFYKIPI"
}

group_A = {
    'A': 8.47, 'D': 5.97, 'C': 1.39, 'E': 6.32, 'T': 5.79,
    'F': 3.91, 'G': 7.82, 'H': 2.26, 'I': 5.71, 'V': 7.02,
    'K': 5.76, 'L': 8.48, 'M': 2.21, 'N': 4.54, 'W': 1.44,
    'P': 4.63, 'Q': 3.82, 'R': 4.93, 'S': 5.94, 'Y': 3.58
}

group_B = {
    'A': 8.95, 'D': 5.91, 'C': 0.47, 'E': 4.78, 'T': 6.54,
    'F': 3.68, 'G': 8.54, 'H': 1.25, 'I': 4.77, 'V': 6.76,
    'K': 4.93, 'L': 8.78, 'M': 1.56, 'N': 5.74, 'W': 1.24,
    'P': 3.74, 'Q': 4.75, 'R': 5.24, 'S': 8.05, 'Y': 4.13
}

print("Sequence, Dist to A, Dist to B, Assigned Group")

for name, seq in sequences.items():
    dist_A = 0
    dist_B = 0
    
    for aa in group_A.keys():
        seq_comp = (seq.count(aa) / len(seq)) * 100
        
        dist_A += (seq_comp - group_A[aa]) ** 2
        dist_B += (seq_comp - group_B[aa]) ** 2
        
    dist_A = math.sqrt(dist_A)
    dist_B = math.sqrt(dist_B)
    
    assigned = "Group A" if dist_A < dist_B else "Group B"
    
    print(f"{name}, {round(dist_A, 2)}, {round(dist_B, 2)}, {assigned}")