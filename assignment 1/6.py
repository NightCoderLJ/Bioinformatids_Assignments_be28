def search_sequence(sequence, search_str):
    positions = []
    start = 0
    # Iterates to find all potentially overlapping matches
    while True:
        start = sequence.find(search_str, start)
        if start == -1:
            break
        positions.append(start + 1)  # Using 1-based indexing as is common in biology
        start += 1
    return positions

if __name__ == "__main__":
    seq = input("Enter the DNA sequence: ").upper()
    search_strs = ['AAG', 'GTC', 'GAG', 'ACTA', 'ATAT']

    
    for search_str in search_strs:
        search_str = search_str.strip()
        positions = search_sequence(seq, search_str)
        
        print(f"\nSearch string: {search_str}")
        print(f"Total match: {len(positions)}")
        if positions:
            print(f"Position of match: {', '.join(map(str, positions))}")
