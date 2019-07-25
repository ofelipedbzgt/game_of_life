import numpy as np

w = 5
h = 5

board = np.random.rand(w, h)
print(board)
print('------------------')
print(board[0][4])


for line in board:
    for element in range(len(line)):
        pass
