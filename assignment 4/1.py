import numpy as np
import matplotlib.pyplot as plt

seq_homo_sapiens = 'MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH'
seq_chicken = 'MVHWTAEEKQLITGLWGKVNVAECGAEALARLLIVYPWTQRFFASFGNLSSPTAILGNPMVRAHGKKVLTSFGDAVKNLDNIKNTFSQLSELHCDKLHVDPENFRLLGDILIIVLAAHFSKDFTPECQAAWQKLVRVVAHALARKYH'

dot_matrix = np.zeros((len(seq_homo_sapiens), len(seq_chicken)))

for i in range(len(seq_homo_sapiens)):
    for j in range(len(seq_chicken)):
        if seq_homo_sapiens[i] == seq_chicken[j]:
            dot_matrix[i, j] = 1

plt.imshow(dot_matrix, cmap='gray', interpolation='nearest')
plt.show()