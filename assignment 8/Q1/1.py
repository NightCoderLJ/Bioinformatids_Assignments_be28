import matplotlib.pyplot as plt

# Hydrophobicity scale
hydro = {
    'A': 13.85, 'D': 11.61, 'C': 15.37, 'E': 11.38, 'F': 13.93,
    'G': 13.34, 'H': 13.82, 'I': 15.28, 'K': 11.58, 'L': 14.13,
    'M': 13.86, 'N': 13.02, 'P': 12.35, 'Q': 12.61, 'R': 13.10,
    'S': 13.39, 'T': 12.70, 'V': 14.56, 'W': 15.48, 'Y': 13.88
}

# 1. Read and parse Q1.fasta
sequences = {}
current_header = ""

with open("Q1.fasta", "r") as f:
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            current_header = line[1:]  # Remove the '>' character
            sequences[current_header] = ""
        else:
            sequences[current_header] += line

# 2. Setup the plot window based on the number of sequences found
window = 7
baseline = sum(hydro.values()) / len(hydro)
fig, axes = plt.subplots(len(sequences), 1, figsize=(
    10, 3 * len(sequences)), sharey=True)

# 3. Calculate and plot the profile for each sequence
for ax, (name, seq) in zip(axes, sequences.items()):
    # Calculate moving average
    scores = [sum(hydro.get(aa, 0) for aa in seq[i:i+window]) /
              window for i in range(len(seq) - window + 1)]

    # Draw line and baseline
    ax.plot(scores, color='blue')
    ax.axhline(y=baseline, color='red', linestyle='--')

    # Format subplot
    ax.set_title(f"Sequence: {name}")
    ax.set_ylabel("Score")
    ax.grid(True, alpha=0.5)

plt.xlabel("Amino Acid Position")
plt.tight_layout()
plt.show()
