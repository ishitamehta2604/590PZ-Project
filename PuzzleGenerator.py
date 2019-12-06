import numpy as np


def generator(row, column):
    a = np.random.randint(0,2, size=(row, column))
    a = -1 * a
    print("Matrix b : \n", a)
    b = np.array(a.tolist())
    count = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if b[i][j] == 0:
                current = i, j
                region = list()
                number = 0
                counter(region, current, number, count, b)


def counter(region, current, number, count, board):
    b = board
    (i, j) = (r, c) = current
    up = (r-1,c)
    left = (r,c-1)
    right = (r, c+1)
    bottom = (r+1, c)
    if up not in region :
        if count <= number:
            if b[r-1][c] == -1:
                region.append (up)
                count+=1
                number = count
                counter (region , up, number, count , b)

    elif left not in region:
        if count <= number:
            if b[r][c-1] == -1:
                region.append (left)
                count += 1
                number = count
                counter(region, left, number, count, b)

    elif bottom not in region :
        if count <= number:
            if b[r+1][c] == -1:
                region.append (bottom)
                count += 1
                number = count
                counter(region ,bottom, number, count , b)

    elif right not in region :
        if count <= number:
            if b [r][c+1] == -1:
                region.append (right)
                count+=1
                number = count
                counter (region ,right, number, count , b)

    else:
        if count > number or count < number :
            print("incorrect solution\n")
            print(i,j)


if __name__ == "__main__":
    generator(10,10)
