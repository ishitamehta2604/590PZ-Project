import numpy as np
from typing import List, Any

# import matplotlib.pyplot as plt


import numpy as np
import math
import random

from pip._vendor.distlib.compat import raw_input

co_ordinate1 = []
def unfilled_cell_count(board, n):
    unfilled_cells = 0
    co_ordinate = []
    for i in range(0, n):
        for j in range(0, n):
            if board[i][j] == -3:
                co_ordinate.append(i * 100 + j)
                unfilled_cells = unfilled_cells + 1
    print("unfilled cells =", unfilled_cells)
    filled_cells = n * n - unfilled_cells
    return [filled_cells, unfilled_cells, co_ordinate]


def brute_force_generation(filled_cell, unfilled_cell, co_ordinate1, board):
    arr = []
    i = 1
    co_ordinate = co_ordinate1
    maximum_cells_to_be_shaded = unfilled_cell - filled_cell
    # for number_cells_to_be_shaded in range(1, 3):
    for number_cells_to_be_shaded in range(1, maximum_cells_to_be_shaded):

        nCr = int(math.factorial(unfilled_cell) / (math.factorial(unfilled_cell - number_cells_to_be_shaded) * (
            math.factorial(number_cells_to_be_shaded))))
        # nCr = int(math.factorial(unfilled_cells)/math.factorial(unfilled_cells-number_cells_to_be_shaded))
        print("nCr=", nCr)
        for rand_number_generation_times in range(1, nCr):
            while i <= number_cells_to_be_shaded:
                random_number = random.randint(1, unfilled_cell)
                if (random_number not in arr):
                    arr.append(random_number)
                    i_cordinate = int(co_ordinate[random_number - 1] / 100)
                    j_cordinate = co_ordinate[random_number - 1] % 100
                    # print( "random=", random_number,"co=",co_ordinate[random_number-1], "board_i=",i_cordinate)
                    # print( "random=", random_number, "board_i=", i_cordinate, "board_j=", j_cordinate)
                    i = i + 1
                    board[i_cordinate][j_cordinate] = -1
        flag = count_for_number(board,n)
        if flag == 1:
            print ("Incorrect Solution")
            print(board)
            print("solution check here **********\n")
        elif flag == 0:
            print("Correct Solution")


def count_for_number(board, n):
    flag = 0
    number = 0
    region = list()
    for i in range(0, n):
        for j in range(0, n):
            # print ("In2")
            if type(board[i][j]) is int and board[i][j] > -1:
                current = (i, j)
                count = 0
                region = list()
                number = board[i][j]
                flag2 = traversal(region, current, board[i][j], count, n, flag)
    if flag == 1:
        print("Incorrect Solution")
        print(board)
    if flag2 == 0 and len(region) == number:
        # print (number)
        print("Corret Solution")
        print (board)
        return flag2

def traversal(region, current, number, count, n, flag):
    currentnum = number
    print(currentnum)
    r, c = current
    up = (r - 1, c)
    left = (r, c - 1)
    right = (r, c + 1)
    bottom = (r + 1, c)
    # print ("In3")
    if count > number:
        print("Wrong Solution")
    if up not in region and r > 0:
        if board[r - 1][c] == -1:
            region.append(up)
            print(region)
            count += 1
            traversal(region, up, number, count, n, flag)
            # print("in1correct solution")
    if left not in region and c > 0:
        if board[r][c - 1] == -1:
            region.append(left)
            print(region)
            count += 1
            traversal(region, left, number, count, n, flag)
            # print("in2correct solution")
    if bottom not in region and r < (n - 1):
        if board[r + 1][c] == -1:
            region.append(bottom)
            print(region)
            count += 1
            traversal(region, bottom, number, count, n, flag)
            # print("in3correct solution")
    if right not in region and c < (n - 1):
        if board[r][c + 1] == -1:
            region.append(right)
            count += 1
            print(region)
            traversal(region, right, number, count, n, flag)
            # print ("in4correct solution")

    elif len(region) > currentnum or len(region) < currentnum:
        flag = 1
        print("incorrect solution\n")
        print(board)
    return flag

    np.asarray(board)
    print(board)
    print(" finishing number traversal")


# def generator ( row, column):
# a=np.random.randint(1, size=(row, column))
# print("Matrix b : \n", a)

if __name__ == "__main__":

    n1 = raw_input("Enter the size of the matrix : ")
    n = int(n1)
    #print(n + "x" + n)
    filled_cells = 0
    unfilled_cells = 0
    list1 = []
    board = []
    if n == 5:
        board = [[-3, -3, -3, 3, -3],
                 [5, -3, -3, -3, 4],
                 [-3, -3, 3, -3, -3],
                 [-3, -3, -3, -3, -3],
                 [5, -3, -3, 6, -3]]
    elif n == 6:
        board = [[-3, -3, -3, 3, -3, -3],
                 [5, -3, -3, -3, 4, -3],
                 [-3, -3, 3, -3, -3, -3],
                 [-3, -3, -3, -3, -3, -3],
                 [5, -3, -3, 6, -3, -3],
                 [5, -3, -3, 6, -3, -3]]
    elif n == 4:
        board = [[-3, -3, -3, 3],
                 [5, -3, -3, -3],
                 [-3, -3, 3, -3],
                 [-3, -3, -3, -3]]
    elif n == 3:
        board = [[1, -3, -3],
                 [-3, -3, -3],
                 [-3, -3, 3]]


    elif n == 10:
        board =  [[2 ," ", -1, 4, -1, " ", 5, -1, " ", 5],
            [-1, " ", " ", -1, -1, 6, " ", -1, -1, -1],
            [-1, 3, -1, " ", 6, -1, -1, 7, " ",-1],
            [8, " ", " ", -1, " ", -1," ", -1,-1,9],
            [-1,-1, -1, -1, " ", -1, " "," ", 4,-1],
            [" ",6,-1 ," "," "," "," ", -1," ", -1],
            [5, " "," ",-1,-1," ", " ", -1, -1, 5],
            [-1, " ",3,-1," ",6, -1, " ", 3, " "],
            [-1, -1," "," ","7",-1,-1, -1, " ", -1],
            [5, -1,-1, 6 ,-1," ", 6, -1,-1, 7]]

    list1 = unfilled_cell_count(board, n)
    print (list1)
    brute_force_generation(list1[0], list1[1], list1[2], board)

