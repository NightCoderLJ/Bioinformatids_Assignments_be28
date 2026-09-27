# Molecular weights provided in Question 2
weights = {
    'A': 85,  'C': 115, 'D': 130, 'E': 145, 'F': 160, 
    'G': 70,  'W': 200, 'H': 150, 'I': 125, 'K': 145, 
    'L': 125, 'M': 143, 'N': 130, 'Y': 175, 'P': 110, 
    'Q': 140, 'R': 170, 'S': 100, 'T': 115, 'V': 110
}

sequences = {
    "Seq 1": "RATPTRWPVGCFNRPWTKWSYDEALDGIKAAGYAWTGLLTASKPSLHH",
    "Seq 2": "ATATPEYLAALKQKSRHAAAAAVMMGLAAIGAAIGIGILGGKFLEGAARQPDLIPLLRTQFFIVMGLVDAIPMIAVGLGLYVMFAVA",
    "Seq 3": "AADVSAAVGATGQSGMTYRLGLSWDWDKSWWQTSTGRLTGYWDAGYTYWEGGDEGAGKHSLSFAPVFVYEFAGDSIKPFIEAGIGVAAFSGTRVGDQNLGSSLNFEDRIGAGLKFANGQSVGVRAIHYSNAGLKQPNDGIESYSLFYKIPI"
}

for name, seq in sequences.items():
    # Calculate the sum of weights for every amino acid in the sequence
    total_weight = sum(weights[aa] for aa in seq)
    print(f"{name}: {total_weight}")