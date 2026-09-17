def analyze_pentapeptides(seq1, seq2):
   
    penta1 = [seq1[i:i+5] for i in range(len(seq1) - 4)]
    penta2 = [seq2[i:i+5] for i in range(len(seq2) - 4)]
    
    
    count1 = {}
    for peptide in penta1:
        if peptide in count1:
            count1[peptide] += 1
        else:
            count1[peptide] = 1
            
    count2 = {}
    for peptide in penta2:
        if peptide in count2:
            count2[peptide] += 1
        else:
            count2[peptide] = 1
    
    
    common_pentas = set(count1.keys()) & set(count2.keys())
    
    
    print(f"Found {len(common_pentas)} matching pentapeptides:\n")
    for p in common_pentas:
        print(f"Peptide: {p} \nFreq in Seq1: {count1[p]} \nFreq in Seq2: {count2[p]} \n-----------------")

analyze_pentapeptides("MVEKRELRCRLL", "MVEKRELQQRLL")