tile_number = int(0)

# Function to fill the corners of the three sub-boards 
# which don't contain the missing cell
def fill(x1, y1, x2, y2, x3, y3, board):
    global tile_number
    tile_number+=1
    board[int(x1)][int(y1)] = tile_number
    board[int(x2)][int(y2)] = tile_number
    board[int(x3)][int(y3)] = tile_number

# Function for filling the board
def func(n, r, c, board):
    n = int(n)
    r = int(r)
    c = int(c)
    # Declares variables which will store the 
    # row number and column number of the missing cell
    missing_cell_row,missing_cell_col = 0, 0
    # Base case
    # If the board size is 2
    if(n==2):
        global tile_number
        # We will fill the board with a new tile, 
        # thus increase the tile number by 1 
        tile_number+=1
        # Fill all the tiles other than the missing tile
        for i in range(n):
            for j in range(n):
                if (board[int(r + i)][int(c + j)] == 0):
                    board[int(r + i)][int(c + j)] = tile_number
        return
    else:
        # Find the missing cell's row and column
        for i in range(r, r+n):
            for j in range(c, c+n):
                if (board[i][j] is not 0): #The cell whose value is 
                    # not 0 is the missing cell
                    missing_cell_row, missing_cell_col = i, j
                    
    # If missing tile is in the 1st quadrant
    if (missing_cell_row < r + n / 2 and missing_cell_col < c + n / 2):
        fill(r + n / 2, c + (n / 2) - 1, r + n / 2, c + n / 2, r + n / 2 - 1, c + n / 2,board)
 
    # If missing tile is in the 3rd quadrant
    elif (missing_cell_row >= r + n / 2 and missing_cell_col < c + n / 2):
        fill(r + (n / 2) - 1, c + (n / 2), r + (n / 2), c + n / 2, r + (n / 2) - 1, c + (n / 2) - 1,board)
 
    # If missing tile is in the 2nd quadrant
    elif (missing_cell_row < r + n / 2 and missing_cell_col >= c + n / 2):
        fill(r + n / 2, c + (n / 2) - 1, r + n / 2, c + n / 2, r + n / 2 - 1, c + n / 2 - 1,board)

 
    # If missing Tile is in 4th quadrant
    elif (missing_cell_row >= r + n / 2 and missing_cell_col >= c + n / 2):
        fill(r + (n / 2) - 1, c + (n / 2), r + (n / 2), c + (n / 2) - 1, r + (n / 2) - 1, c + (n / 2) - 1,board)
 
    # call the recursive function for the 4 sub-boards
    func(n/2, r, c + n / 2,board)
    func(n/2, r, c,board)
    func(n/2, r + n / 2, c,board)
    func(n/2, r + n / 2, c + n / 2,board)


n = int(4)
board = [[0, 0, 0, 0],
        [0, -1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]
    
func(n,int(0),int(0),board) #Call the function to fill the board
# Prthe filled board in the end
for i in range(n):
    for j in range(n):
        print(str(int(board[i][j])), end = " ")
    print()