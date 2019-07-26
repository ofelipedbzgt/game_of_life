import numpy as np
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [10, 11, 12]])
print(a)
rows = a.shape[0]
cols = a.shape[1]
print(rows)
print(cols)

for x in range(0, rows):
    for y in range(0, cols):
        print(a[x, y])