sequences = {
    "Seq 1": "RATPTRWPVGCFNRPWTKWSYDEALDGIKAAGYAWTGLLTASKPSLHH",
    "Seq 2": "ATATPEYLAALKQKSRHAAAAAVMMGLAAIGAAIGIGILGGKFLEGAARQPDLIPLLRTQFFIVMGLVDAIPMIAVGLGLYVMFAVA",
    "Seq 3": "AADVSAAVGATGQSGMTYRLGLSWDWDKSWWQTSTGRLTGYWDAGYTYWEGGDEGAGKHSLSFAPVFVYEFAGDSIKPFIEAGIGVAAFSGTRVGDQNLGSSLNFEDRIGAGLKFANGQSVGVRAIHYSNAGLKQPNDGIESYSLFYKIPI"
}

amino_acids = "ACDEFGHIKLMNPQRSTVWY"

print("AA, Seq 1 (%), Seq 2 (%), Seq 3 (%)")

for aa in amino_acids:
    s1_pct = round((sequences["Seq 1"].count(aa) / len(sequences["Seq 1"])) * 100, 2)
    s2_pct = round((sequences["Seq 2"].count(aa) / len(sequences["Seq 2"])) * 100, 2)
    s3_pct = round((sequences["Seq 3"].count(aa) / len(sequences["Seq 3"])) * 100, 2)
    
    print(f"{aa}, {s1_pct}, {s2_pct}, {s3_pct}")