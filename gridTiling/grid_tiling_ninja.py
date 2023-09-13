"""
name: Mason Cox
Honor Code and Acknowledgments:
This work complies with the JMU Honor Code.
Comments here on your code and submission.
"""


def main():
    gridSize = int(input())
    index = list(map(int, input().split()))
        
    grid = []
    for i in range(pow(2, gridSize)):
        grid.append(['xx' for _ in range(pow(2, gridSize))])
    grid[index[0]][index[1]] = '-1'
    
    tile(grid, gridSize, [0, 0], 0)
        
    for i in range(pow(2, gridSize)):
        print(" ".join(grid[i]))
    pass


def tile(grid, gridSize, index, tileCount):
    Q2 = [index[0], index[1]]                                                     # Top left
    Q1 = [index[0], index[1] + pow(2, gridSize) // 2]                             # Top right
    Q3 = [index[0] + pow(2, gridSize) // 2, index[1]]                             # Bottom left
    Q4 = [index[0] + pow(2, gridSize) // 2, index[1] + pow(2, gridSize) // 2]     # Bottom right
    
    size = pow(2, gridSize)     # size == side length for sub grid
    
    # Base Case 2x2 grid
    if (size == 2):
        for i in range(size):
            for j in range(size):
                if (grid[index[0] + i][index[1] + j] == 'xx'):
                   grid[index[0] + i][index[1] + j] = f"{tileCount:02}"
        return tileCount + 1    # Increment the tileCount after placing new l-tile
    
    # Get the indices for the removed square
    row = 0
    col = 0
    for i in range(index[0], index[0] + size):
        for j in range(index[1], index[1] + size):
            if (grid[i][j] != 'xx'):
                row = j
                col = i
    
    # Based on index for removed square, place l-tile in required quadrant
    if (row >= Q2[1] and row < Q1[1] and col < Q3[0]):    # If index is in Q2
        grid[Q4[0]][Q4[1]] = f"{tileCount:02}"
        grid[Q4[0] - 1][Q4[1]] = f"{tileCount:02}"
        grid[Q4[0]][Q4[1] - 1] = f"{tileCount:02}"
    elif (row >= Q1[1] and col < Q4[0]):                  # If index is in Q1
        grid[Q3[0]][Q4[1] - 1] = f"{tileCount:02}"
        grid[Q3[0]][Q4[1]] = f"{tileCount:02}"
        grid[Q3[0] - 1][Q4[1] - 1] = f"{tileCount:02}"
    elif (row >= Q3[1] and col >= Q3[0] and row < Q4[1]): # If index in in Q3
        grid[Q4[0] - 1][Q1[1]] = f"{tileCount:02}"
        grid[Q4[0]][Q1[1]] = f"{tileCount:02}"
        grid[Q4[0] - 1][Q1[1] - 1] = f"{tileCount:02}"
    else:                                                 # If index is in Q4
        grid[Q4[0] - 1][Q1[1] - 1] = f"{tileCount:02}"
        grid[Q4[0]][Q1[1] - 1] = f"{tileCount:02}"
        grid[Q4[0] - 1][Q1[1]] = f"{tileCount:02}"
    
    # Increment the tileCount after placing new l-tile
    tileCount += 1
    
    # Split the current grid into 4 sub-grids recursively
    splitSize = pow(2, gridSize) // 2
    tileCount = tile(grid, gridSize - 1, [index[0], index[1]], tileCount)                     # Q2
    tileCount = tile(grid, gridSize - 1, [index[0], index[1] + splitSize], tileCount)             # Q1
    tileCount = tile(grid, gridSize - 1, [index[0] + splitSize, index[1]], tileCount)             # Q3
    tileCount = tile(grid, gridSize - 1, [index[0] + splitSize, index[1] + splitSize], tileCount)     # Q4
    return tileCount


if __name__ == "__main__":
    main()