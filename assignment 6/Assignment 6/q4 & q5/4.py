import math
import csv

def load_blosum62(matrix_file):
   
    matrix = {}
    with open(matrix_file, 'r') as f:
        lines = f.readlines()
    
    amino_acids = []
    for line in lines:
        if line.startswith('#'): 
            continue
        
        parts = line.strip().split()
        if not parts:
            continue
            
        if not amino_acids:
            amino_acids = parts
        else:
            row_aa = parts[0]
            scores = parts[1:]
            for col_aa, score in zip(amino_acids, scores):
                matrix[(row_aa, col_aa)] = int(score)
    return matrix

def read_clustal(aln_file):
    
    sequences = {}
    with open(aln_file, 'r') as f:
        for line in f:
            line = line.strip()
            
          
            if not line or line.startswith('CLUSTAL') or line.startswith('*') or line.startswith(' ') or line.startswith(':') or line.startswith('.'):
                continue
            
            parts = line.split()
            if len(parts) >= 2:
                seq_id = parts[0]
                seq_str = parts[1]
                
                if not all(c.isalpha() or c == '-' for c in seq_str):
                    continue
                    
                if seq_id not in sequences:
                    sequences[seq_id] = ""
                sequences[seq_id] += seq_str
    
    valid_sequences = list(sequences.values())
    
    if not valid_sequences:
        return []
        
    expected_length = len(valid_sequences[0])
    for seq_id, seq_str in sequences.items():
        if len(seq_str) != expected_length:
    
            raise ValueError(f"Alignment error: '{seq_id}' has length {len(seq_str)}, expected {expected_length}.")
            
    return valid_sequences

def calculate_conservation(msa_file, matrix_file, output_csv):
    blosum62 = load_blosum62(matrix_file)
    sequences = read_clustal(msa_file)
    
    alignment_length = len(sequences[0])
    
    
    results = [("Position", "Max_Frequency", "Entropy", "Sum_of_Pairs", "Variance")]
    
    for i in range(alignment_length):
        column = [seq[i].upper() for seq in sequences if seq[i] != '-']
        total_chars = len(column)
        
        
        if total_chars == 0:
            results.append((i + 1, 0, 0, 0, 0))
            continue
            
        unique_chars = set(column)
        
        # 1. Unweighted Frequency 
        max_freq = max(column.count(char) / total_chars for char in unique_chars)
        
        # 2. Entropy
        entropy = 0
        for char in unique_chars:
            prob = column.count(char) / total_chars
            entropy -= prob * math.log2(prob)
            
        # 3. Variance (of the unweighted frequencies)
        mean_freq = sum(column.count(c) / total_chars for c in unique_chars) / len(unique_chars)
        variance = 0
        for char in unique_chars:
            freq = column.count(char) / total_chars
            variance += (freq - mean_freq) ** 2
        variance = variance / len(unique_chars)
            
        # 4. Sum of Pairs
        sp_score = 0
        pairs_count = 0
        
        for x in range(total_chars):
            for y in range(x + 1, total_chars):
                aa1 = column[x]
                aa2 = column[y]
                
                if (aa1, aa2) in blosum62:
                    sp_score += blosum62[(aa1, aa2)]
                    pairs_count += 1
                    
        avg_sp = sp_score / pairs_count if pairs_count > 0 else 0
        
      
        results.append((i + 1, round(max_freq, 3), round(entropy, 3), round(avg_sp, 3), round(variance, 3)))

    # Write all the results to the specified CSV file
    with open(output_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(results)
    print(f"Successfully calculated scores and saved to '{output_csv}'")



calculate_conservation("set 1.aln-clustal_num", "BLOSUM62", "set1_scores_clustal.csv")
calculate_conservation("set 1 mafft.aln-clustalw", "BLOSUM62", "set1_scores_mafft.csv")
calculate_conservation("set 1 muscle.aln-clustalw", "BLOSUM62", "set1_scores_muscle.csv")

calculate_conservation("set 2.aln-clustal_num", "BLOSUM62", "set2_scores_clustal.csv")
calculate_conservation("set 2 mafft.aln-clustalw", "BLOSUM62", "set2_scores_mafft.csv")
calculate_conservation("set 2 muscle.aln-clustalw", "BLOSUM62", "set2_scores_muscle.csv")

