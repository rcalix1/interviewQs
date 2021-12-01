import numpy as np

def rotate_matrix(m):
    m1 = np.zeros((4, 4))
    print(m)
    for i in range(4):
        for j in range(4):
            m1[j][3-i] = m[i][j]
    print(m1)


#m = np.zeros((4,4))

m = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

m = np.asarray(m)

rotate_matrix(m)
