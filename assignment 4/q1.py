# Q1 - Dot plot for the human and chicken haemoglobin beta chain

import matplotlib.pyplot as plt

human = ("MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKV"
         "KAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKE"
         "FTPPVQAAYQKVVAGVANALAHKYH")

chicken = ("MVHWTAEEKQLITGLWGKVNVAECGAEALARLLIVYPWTQRFFASFGNLSSPTAILGNPMV"
           "RAHGKKVLTSFGDAVKNLDNIKNTFSQLSELHCDKLHVDPENFRLLGDILIIVLAAHFSKD"
           "FTPECQAAWQKLVRVVAHALARKYH")


def dot_plot(seq1, seq2, filename):
    x, y = [], []
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            if seq1[i] == seq2[j]:
                x.append(i + 1)
                y.append(j + 1)
    plt.figure(figsize=(6, 6))
    plt.scatter(x, y, s=4, marker="s", color="black")
    plt.xlabel("Human HBB")
    plt.ylabel("Chicken HBB")
    plt.gca().invert_yaxis()
    plt.savefig(filename, dpi=200, bbox_inches="tight")
    plt.close()


def same_segments(seq1, seq2, min_length=4):
    segments = []
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            # only start counting at the beginning of a diagonal run
            if seq1[i] != seq2[j]:
                continue
            if i > 0 and j > 0 and seq1[i - 1] == seq2[j - 1]:
                continue
            n = 0
            while i + n < len(seq1) and j + n < len(seq2) and seq1[i + n] == seq2[j + n]:
                n += 1
            if n >= min_length:
                segments.append((i + 1, j + 1, n, seq1[i:i + n]))
    return segments


dot_plot(human, chicken, "q1_dotplot.png")
dot_plot(human[:20], chicken[:20], "q1_dotplot_first20.png")

print("Segments identical in both sequences (length >= 4):")
for start1, start2, n, seq in same_segments(human, chicken):
    print(f"human {start1}-{start1 + n - 1}   chicken {start2}-{start2 + n - 1}   {seq}")
