# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts
def main():
    grid_size = int(input())
    a, b = map(int, input().split())
    grid = [[0 for _ in range(128)] for _ in range(128)]
    grid[a][b] = -1
    
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
        if (n == 2):
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
        
        elif(r>= x + int(n / 2) and c < y + int(n / 2)):
            place(x + int(n / 2) - 1, y+ int(n / 2), x + int(n / 2), y + int(n / 2), x + int(n / 2) - 1, y + int(n / 2) - 1)
        elif(r < x + int(n / 2) and c >= y + int(n / 2)):
            place(x + int(n / 2), y + int(n / 2) - 1, x + int(n / 2), y + int(n / 2), x + int(n / 2) - 1, y + int(n / 2) - 1)
        elif(r >= x + int(n / 2) and c >= y + int(n / 2)):
            place(x + int(n / 2) - 1, y + int(n / 2), x + int(n / 2), y + int(n / 2) - 1, x + int(n / 2) - 1, y + int(n / 2) - 1)

        tile(int(n / 2), x, y + int(n / 2))
        tile(int(n / 2), x, y)
        tile(int(n / 2), x + int(n / 2), y)
        tile(int(n / 2), x + int(n / 2), y + int(n / 2))

        return 0
    
    tile(grid_size, a, b)
    
    for i in range(grid_size):
        for j in range(grid_size):
            print(grid[i][j], end=" ")
        print()

        


        

if __name__ == "__main__":
    main()