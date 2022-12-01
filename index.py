from random import randrange





def printfor():
    for i in range(4):
        for j in range(4):
            endspace = "    "
            if (grid[i][j] > 9):
                endspace = "   "
            elif (grid[i][j] > 99):
                endspace = "  "
            elif (grid[i][j] > 999):
                endspace = " "
            print(grid[i][j], end=endspace)
        print()


def generate():
    odd = randrange(4)
    if (odd >= 0 and odd <= 2):
        randnumber = 2
    else:
        randnumber = 4
    randrow = randrange(4)
    randcol = randrange(4)
    while (grid[randrow][randcol] > 0):
        randrow = randrange(4)
        randcol = randrange(4)
    grid[randrow][randcol] = randnumber


def marge(row, column, secondrow, secondcol):
    grid[secondrow][secondcol] = 2*grid[secondrow][secondcol]


def shiftup(col):
    for row in range(1, 4):
        searchrow = row-1
        while (grid[searchrow][col] == 0 and searchrow > 0):
            searchrow = searchrow-1
        if (searchrow == 0 and grid[searchrow][col] == 0):
            grid[0][col] = grid[row][col]
            grid[row][col] = 0
        elif (grid[searchrow][col] == grid[row][col]):
            marge(row, col, searchrow, col)
            grid[row][col] = 0
        elif (row > searchrow+1):
            while(grid[searchrow-1][col]==0):
                grid[searchrow+1][col] = grid[row][col]
                grid[row][col] = 0
                grid[searchrow-1][col] = grid[searchrow][col]
                grid[searchrow][col]=grid[searchrow+1][col]
                grid[searchrow+1][col]=0
                

def shiftdown(col):
    for row in range(2, -1, -1):
        searchrow = row+1
        while (grid[searchrow][col] == 0 and searchrow < 3):
            searchrow = searchrow+1
        if (searchrow == 3 and grid[searchrow][col] == 0):
            grid[3][col] = grid[row][col]
            grid[row][col] = 0
        elif (grid[searchrow][col] == grid[row][col]):
            marge(row, col, searchrow, col)
            grid[row][col] = 0
        elif (row > searchrow-1):
            # while(grid[searchrow+1][col]==0):
            grid[searchrow-1][col] = grid[row][col]
            grid[row][col] = 0
                # grid[searchrow+1][col] = grid[searchrow][col]
                # grid[searchrow][col]=grid[searchrow-1][col]
                # grid[searchrow-1][col]=0


def shiftleft(row):
    for col in range(1, 4):
        searchcol = col-1
        while (grid[row][searchcol] == 0 and searchcol < 0):
            searchcol = searchcol-1
        if (searchcol == 0 and grid[row][searchcol] == 0):
            grid[row][0] = grid[row][col]
            grid[row][col] = 0
        elif (grid[row][searchcol] == grid[row][col]):
            marge(row, col, row, searchcol)
            grid[row][col] = 0
        elif (col > searchcol+1):
            while(grid[searchcol-1][row]==0):
                grid[row][searchcol+1] = grid[row][col]
                grid[row][col] = 0
                grid[searchcol-1][row] = grid[searchcol][row]
                grid[searchcol][row]=grid[searchcol+1][row]
                grid[searchcol+1][row]=0


def shiftright(row):
    for col in range(2, -1, -1):
        searchcol = col+1
        while (grid[row][searchcol] == 0 and searchcol < 3):
            searchcol = searchcol+1
        if (searchcol == 3 and grid[row][searchcol] == 0):
            grid[row][3] = grid[row][col]
            grid[row][col] = 0
        elif (grid[row][searchcol] == grid[row][col]):
            marge(row, col, row, searchcol)
            grid[row][col] = 0
        elif (col > searchcol-1):
            grid[row][searchcol-1] = grid[row][col]
            grid[row][col] = 0


grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
print("2048 game")
generate()

while (True):
    printfor()
    move = input("Move up,right,left,Down. Enter W,A,S,D: ")
    if (move == "W"):
        shiftup(0)
        shiftup(1)
        shiftup(2)
        shiftup(3)
    elif (move == "D"):
        shiftdown(0)
        shiftdown(1)
        shiftdown(2)
        shiftdown(3)
    elif (move == "S"):
        shiftleft(0)
        shiftleft(1)
        shiftleft(2)
        shiftleft(3)
    elif (move == "A"):
        shiftright(0)
        shiftright(1)
        shiftright(2)
        shiftright(3)
     
    generate()
