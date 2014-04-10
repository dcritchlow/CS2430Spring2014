#!/usr/bin/python
import numpy as np

# Store the solution set
x = {}

def nQueen(k, n):
    """
    Builds solutions for 'n' size of chess board
    """
    for i in range(1, n+1):
        if place(k, i):
            x[k] = i
            if k == n:
                # print x.values()
                printBoard(x)
            else:
                nQueen(k+1, n)

def place(row, col):
    """
    Backtracking algorithm to check queen placement
    """
    for j in range(1, row):
        # Check for 'rook' and 'bishop' conflicts
        if x[j] == col or abs(j - row) == abs(x[j] - col):
            return False
    return True

def printBoard(solution):
    """
    Prints a pretty board using numpy
    """
    board = np.array([['*'] * n] * n)
    for row, col in solution.items():
        board[row-1, col-1] = 'Q'
    print board,'\n'

if __name__ == '__main__':
    # Solve for board size 8x8
    n = 8
    nQueen(1, n)








