import numpy as np
from random import randint
from pprint import pprint

alive = '#'
dead = ' '
x = 10
y = 10
size = x


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
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
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
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def dead_state(w, h):
    board = np.zeros((w, h), dtype=int)
    return board


def alive_state(w, h):
    board = np.ones((w, h), dtype=int)
    return board


def next_board_state(board):
    for line in board:
        for element in range(len(line)):
            # check all neighbours states

            if ran == 0:
                line[element] = 0
            else:
                line[element] = 1




render(random_state(x, y))
