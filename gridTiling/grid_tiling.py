# Your Task
# You are going to write a program to compute L-tilings of 
#  square grids. You will assign each tile a number starting with 00. The first tile you generate should have all of its grid cells marked with a 00, the next tile 01, etc. 

# Input

# The first line of input will give the grid size parameter n as an integer. The second line will contain the index (i, j) of the removed tile. 

# Output

# Your code should output 
# lines, each containing 
#  2-digit numbers separated by spaces (and formatted so that single digit numbers have a leading 0). The value of each grid location should be the tile index you generated. (You may assume you won't need 3 digits). 

# Sample Input 1

# 3
# 0 0
# Sample Output 1

# -1 02 03 03 07 07 08 08
# 02 02 01 03 07 06 06 08
# 04 01 01 05 09 09 06 10
# 04 04 05 05 00 09 10 10
# 12 12 13 00 00 17 18 18
# 12 11 13 13 17 17 16 18
# 14 11 11 15 19 16 16 20
# 14 14 15 15 19 19 20 20

# Sample Input 2

# 3
# 1 2
# Sample Output 2

# 02 02 03 03 07 07 08 08
# 02 01 -1 03 07 06 06 08
# 04 01 01 05 09 09 06 10
# 04 04 05 05 00 09 10 10
# 12 12 13 00 00 17 18 18
# 12 11 13 13 17 17 16 18
# 14 11 11 15 19 16 16 20
# 14 14 15 15 19 19 20 20
# Sample Input 3

# 4
# 10 10
# Sample Output 2

# 03 03 04 04 08 08 09 09 24 24 25 25 29 29 30 30
# 03 02 02 04 08 07 07 09 24 23 23 25 29 28 28 30
# 05 02 06 06 10 10 07 11 26 23 27 27 31 31 28 32
# 05 05 06 01 01 10 11 11 26 26 27 22 22 31 32 32
# 13 13 14 01 18 18 19 19 34 34 35 35 22 39 40 40
# 13 12 14 14 18 17 17 19 34 33 33 35 39 39 38 40
# 15 12 12 16 20 17 21 21 36 36 33 37 41 38 38 42
# 15 15 16 16 20 20 21 00 00 36 37 37 41 41 42 42
# 45 45 46 46 50 50 51 00 66 66 67 67 71 71 72 72
# 45 44 44 46 50 49 51 51 66 65 65 67 71 70 70 72
# 47 44 48 48 52 49 49 53 68 65 -1 69 73 73 70 74
# 47 47 48 43 52 52 53 53 68 68 69 69 64 73 74 74
# 55 55 56 43 43 60 61 61 76 76 77 64 64 81 82 82
# 55 54 56 56 60 60 59 61 76 75 77 77 81 81 80 82
# 57 54 54 58 62 59 59 63 78 75 75 79 83 80 80 84
# 57 57 58 58 62 62 63 63 78 78 79 79 83 83 84 84

# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts
def main():
    grid_size = int(input())
    a, b = map(int, input().split())
    grid = [[0 for _ in range(128)] for _ in range(128)]
    grid[a][b] = -1
    
    for i in range(n):
        print(' '.join(map(lambda x: str(x).zfill(2), grid[i])))

    def place(x1, y1, x2, y2, x3, y3):
        global tile_num
        tile_num += 1
        grid[x1][y1] = tile_num
        grid[x2][y2] = tile_num
        grid[x3][y3] = tile_num

    def tile(n, x, y):
        global tile_num
        r = 0
        c = 0
        if (n == 2)
            tile_num += 1
            for i in range(n):
                for j in range(n):
                    if (grid[x+i][y+j] == 0):
                        grid[x+i][y+j] = tile_num
            return 0
        for i in range(x, x+n):
            for j in range(y, y+n):
                if (grid[i][j] != 0):
                    r = i
                    c = j
        if (r < x + n / 2 and c < y + n / 2):
            place(x + int(n / 2), y + int(n / 2) - 1, x + int(n / 2), y + int(n / 2), x + int(n / 2) - 1, y + int(n / 2))
        


        

if __name__ == "__main__":
    main()