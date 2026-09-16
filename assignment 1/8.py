def compute_avg_stacking_energy(sequence):
    energy_map = {
        'AA': -4, 'AT': -7, 'AC': -5, 'AG': -11,
        'TA': -7, 'TT': -2, 'TC': -3, 'TG': -4,
        'CA': -9, 'CT': -5, 'CC': -6, 'CG': -7,
        'GA': -9, 'GT': -6, 'GC': -4, 'GG': -11
    }
    
    sequence = sequence.upper()
    total_energy = 0
    
    # Calculate the number of adjacent pairs
    num_pairs = len(sequence) - 1
    
    if num_pairs <= 0:
        return 0
        
    valid_pairs = 0
    for i in range(num_pairs):
        pair = sequence[i:i+2]
        if pair in energy_map:
            total_energy += energy_map[pair]
            valid_pairs += 1
            
    if valid_pairs == 0:
        return 0
        
    return total_energy / valid_pairs

if __name__ == "__main__":
    seq = input("Enter DNA sequence: ")
    avg_energy = compute_avg_stacking_energy(seq)
    print(f"Average base stacking energy: {avg_energy}")
