import numpy as np
import pandas as pd
import sys

fileName = sys.argv[1]

print(fileName + "\n\n\n")

puzzle = pd.read_csv(fileName, sep=',', header=None)

puzzle = puzzle.fillna(0)

print("Inputted Sudoku Puzzle:")
print(np.asmatrix(puzzle))

def movePossible(x, y, m):
    for i in range(0, 9):
        if puzzle[i][x] == m:
            return False
    for j in range(0, 9):
        if puzzle[y][j] == m:
            return False
    x_i = (x // 3) * 3
    y_i = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if puzzle[y_i][x_i] == m:
                return False
    return True


def solution():
    for y in range(9):
        for x in range(9):
            if puzzle[y][x] == 0:
                for m in range(1, 10):
                    if movePossible(x, y, m):
                        puzzle[y][x] = m
                        solution()
                        puzzle[y][x] = 0
                return
    print("Solution:")
    print(np.asmatrix(puzzle))
    input("Press Enter/Return to check for more solutions")


solution()
