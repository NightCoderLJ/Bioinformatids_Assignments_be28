sequences = {
    "Seq 1": "RATPTRWPVGCFNRPWTKWSYDEALDGIKAAGYAWTGLLTASKPSLHH",
    "Seq 2": "ATATPEYLAALKQKSRHAAAAAVMMGLAAIGAAIGIGILGGKFLEGAARQPDLIPLLRTQFFIVMGLVDAIPMIAVGLGLYVMFAVA",
    "Seq 3": "AADVSAAVGATGQSGMTYRLGLSWDWDKSWWQTSTGRLTGYWDAGYTYWEGGDEGAGKHSLSFAPVFVYEFAGDSIKPFIEAGIGVAAFSGTRVGDQNLGSSLNFEDRIGAGLKFANGQSVGVRAIHYSNAGLKQPNDGIESYSLFYKIPI"
}

# Values provided from the table
Hgm = {'A': 13.85, 'D': 11.61, 'C': 15.37, 'E': 11.38, 'F': 13.93, 'G': 13.34, 'H': 13.82, 'I': 15.28, 'K': 11.58, 'L': 14.13, 'M': 13.86, 'N': 13.02, 'P': 12.35, 'Q': 12.61, 'R': 13.10, 'S': 13.39, 'T': 12.70, 'V': 14.56, 'W': 15.48, 'Y': 13.88}
Ca = {'A': 20.00, 'D': 26.00, 'C': 25.00, 'E': 33.00, 'F': 46.00, 'G': 13.00, 'H': 37.00, 'I': 39.00, 'K': 46.00, 'L': 35.00, 'M': 43.00, 'N': 28.00, 'P': 22.00, 'Q': 36.00, 'R': 55.00, 'S': 20.00, 'T': 28.00, 'V': 33.00, 'W': 61.00, 'Y': 46.00}
Et = {'A': 1.90, 'D': 1.52, 'C': 2.04, 'E': 1.54, 'F': 1.86, 'G': 1.90, 'H': 1.76, 'I': 1.95, 'K': 1.37, 'L': 1.97, 'M': 1.96, 'N': 1.56, 'P': 1.70, 'Q': 1.52, 'R': 1.48, 'S': 1.75, 'T': 1.77, 'V': 1.98, 'W': 1.87, 'Y': 1.69}

print("Sequence, Avg Hgm, Avg Ca, Avg Et")

for name, seq in sequences.items():
    length = len(seq)
    
    avg_Hgm = sum(Hgm[aa] for aa in seq) / length
    avg_Ca = sum(Ca[aa] for aa in seq) / length
    avg_Et = sum(Et[aa] for aa in seq) / length
    
    print(f"{name}, {round(avg_Hgm, 4)}, {round(avg_Ca, 4)}, {round(avg_Et, 4)}")