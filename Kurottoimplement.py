import numpy as np

import numpy as np;
from typing import List, Any

#import matplotlib.pyplot as plt
import self as self
import re as re

#plt.imshow(board, cmap="gray")
#plt.show()

#def movement()

#class Grid :

#def __init__(self, board):
    #Whether or not to include the cell in the backtracking

    #self.cell_val= 0 #(number, -1 for shaded and -2 not to be shaded)
    #self.count= []
    #self.region = []
    #self.number = 0
    #self.board = board
    #self.current_index = [0,0] # the index of the current possibility
    #self.is_solved = 0  # runs the possibility checker

def countfornumber(board,n):
    print(1)
    region = list()
    for i in range (0,n):
        for j in range (0,n):
            # print(i,j)
            if type(board[i][j]) is int and board[i][j] > -1:
                current = (i,j)
                count = 0
                region = list()
                number = board[i][j]
                traversal(region, current, board[i][j], count, n)
    if len(region) == number:
        # print (number)
        print("Correct Solution")


def traversal(region, current, number,count,n):
    currentnum = number
    print (currentnum)
    r,c = current
    up = (r-1,c)
    left = (r,c-1)
    right = (r, c+1)
    bottom = (r+1, c)

    if count > number:
        print("Wrong Solution")
    if up not in region and r > 0:
        if board[r-1][c] == -1:
                region.append(up)
                print(region)
                count += 1
                traversal(region, up, number, count,n)
                # print("in1correct solution")
    if left not in region and c > 0:
        if board[r][c-1] == -1:
                region.append (left)
                print(region)
                count += 1
                traversal (region ,left, number , count,n)
                # print("in2correct solution")
    if bottom not in region and r < (n-1):
        if board [r+1][c] == -1:
                region.append (bottom)
                print(region)
                count += 1
                traversal(region ,bottom, number , count,n)
                # print("in3correct solution")
    if right not in region and c < (n-1):
        if board[r][c+1] == -1:
                region.append (right)
                count += 1
                print (region)
                traversal (region ,right, number, count,n)
                # print ("in4correct solution")

    if len(region) > currentnum or len(region) < currentnum:
        print("incorrect solution\n")
        exit()

    np.asarray(board)
    print (board)
    print(" finishing number traversal")


# def generator ( row, column):
# a=np.random.randint(1, size=(row, column))
# print("Matrix b : \n", a)

if __name__ == "__main__":
        board = [[2," ", -1, 4, -1, " ", 5, -1, " ", 5],
            [-1, " ", " ", -1, -1, 6, " ", -1, -1, -1],
            [-1, 3, -1, " ", 6, -1, " ", 7," ",-1],
            [8, " ", " ", -1, " ", -1," ", -1,-1,9],
            [-1,-1, -1, -1, " ", -1, " "," ", 4,-1],
            [" ",6,-1 ," "," "," "," ", -1," ", -1],
            [5, " "," ",-1,-1," ", " ", -1, -1, 5],
            [-1, " ",3,-1," ",6, -1, " ", 3, " "],
            [-1, -1," "," ","7",-1,-1, -1, " ", -1],
            [5, -1,-1, 6 ,-1," ", 6, -1,-1, 7]]

        countfornumber(board,10)
