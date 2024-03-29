from main import next_board_state
import numpy as np

if __name__ == "__main__":
    # TEST 1: dead cells with no live neighbors
    # should stay dead.
    init_state1 = np.array([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ])
    expected_next_state1 = np.array([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ])
    actual_next_state1 = next_board_state(init_state1)

    if expected_next_state1.all() == actual_next_state1.all():
        print("PASSED 1")
    else:
        print("FAILED 1!")
        print("Expected:")
        print(expected_next_state1)
        print("Actual:")
        print(actual_next_state1)

    # TEST 2: dead cells with exactly 3 neighbors
    # should come alive.
    init_state2 = np.array([
        [0, 0, 1],
        [0, 1, 1],
        [0, 0, 0]
    ])
    expected_next_state2 = np.array([
        [0, 1, 1],
        [0, 1, 1],
        [0, 0, 0]
    ])
    actual_next_state2 = next_board_state(init_state2)

    if expected_next_state2.all() == actual_next_state2.all():
        print("PASSED 2")
    else:
        print("FAILED 2!")
        print("Expected:")
        print(expected_next_state2)
        print("Actual:")
        print(actual_next_state2)