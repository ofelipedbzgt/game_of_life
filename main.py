import numpy as np
from random import randint
import time

alive = '#'
dead = ' '
x = 100
y = 50
size = x
interval = 1

np.set_printoptions(linewidth=320)


def random_state(w, h):
    board = np.zeros((w, h), dtype=int)
    for line in board:
        for element in range(len(line)):
            ran = randint(0, 1)
            if ran == 0:
                line[element] = 0
            else:
                line[element] = 1
    return board


def render(board):
    line_count = 0
    print('~' * x * 2)
    for line in board:
        for element in line:
            if element == 0:
                print(dead, end=" ")
                line_count += 1
            elif element == 1:
                print(alive, end=" ")
                line_count += 1
            if line_count >= size:
                print("")
                line_count = 0
    print('~' * x * 2)


def dead_state(w, h):
    board = np.zeros((w, h), dtype=int)
    return board


def next_board_state(board):
    rows = board.shape[0]
    cols = board.shape[1]
    new_state = dead_state(rows, cols)
    # new_state = dead_state(x, y)
    for i in range(0, rows - 1):
        for j in range(0, cols - 1):
            n_list = []
            count_alive = 0
            # check all neighbours
            n1 = board[i - 1, j - 1]
            n2 = board[i, j - 1]
            n3 = board[i + 1, j - 1]
            n4 = board[i - 1, j]
            n = board[i, j]
            n5 = board[i + 1, j]
            n6 = board[i - 1, j + 1]
            n7 = board[i, j + 1]
            n8 = board[i + 1, j + 1]
            n_list.append(n1)
            n_list.append(n2)
            n_list.append(n3)
            n_list.append(n4)
            n_list.append(n5)
            n_list.append(n6)
            n_list.append(n7)
            n_list.append(n8)
            for h in n_list:
                if h == 1:
                    count_alive += 1
            if n == 1 and count_alive <= 1:
                new_state[i, j] = 0
            elif n == 1 and count_alive == 2 or count_alive == 3:
                new_state[i, j] = 1
            elif n == 1 and count_alive > 3:
                new_state[i, j] = 0
            elif n == 0 and count_alive == 3:
                new_state[i, j] = 1
    return new_state


def load_board_state(filepath):
    with open(filepath, 'r') as f:
        lines = [l.rstrip() for l in f.readlines()]

    height = len(lines)
    width = len(lines[0])
    board = dead_state(height, width)

    for b, line in enumerate(lines):
        for m, char in enumerate(line):
            board[b][m] = int(char)
    return board


def run_forever(initial_state):
    next_state = initial_state
    while True:
        render(next_state)
        next_state = next_board_state(next_state)
        time.sleep(interval)


if __name__ == "__main__":
    init_state = random_state(x, y)
    # init_state = load_board_state('./ggg.txt')
    run_forever(init_state)

