import math
"""
    name:  Chingiz Rajabli

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.
            - I used this article by geeksforgeeks to understnad the problem a bit better:
            https://www.geeksforgeeks.org/tiling-problem-using-divide-and-conquer-algorithm/
  
           Comments here on your code and submission.
"""


def main():
    grid_size = int(math.pow(2, int(input())))
    a, b = map(int, input().split())
    global tile_num
    tile_num = 0
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    grid[a][b] = -1
    tile(grid_size, 0, 0, grid)
 
    for i in range(grid_size):
        for j in range(grid_size):
            print(f"{grid[i][j]:02d}", end=" ")
        print()


def place(x1, y1, x2, y2, x3, y3, grid):
    global tile_num
    tile_num += 1
    grid[x1][y1] = tile_num
    grid[x2][y2] = tile_num
    grid[x3][y3] = tile_num
     
def tile(n, x, y, grid):
    global tile_num
    r = 0
    c = 0

    if (n == 2):
        tile_num += 1
        for i in range(n):
            for j in range(n):
                if(grid[x + i][y + j] == 0):
                    grid[x + i][y + j] = tile_num
        return 0   
    
    for i in range(x, x + n):
        for j in range(y, y + n):
            if (grid[i][j] != 0):
                r = i
                c = j 

    if (r < x + n // 2 and c < y + n // 2):
        place(x + (n // 2), y + (n // 2) - 1, x + (n // 2), 
              y + (n // 2), x + (n // 2) - 1, y + (n // 2), grid)
     
    elif(r >= x + (n // 2) and c < y + (n // 2)):
        place(x + (n // 2) - 1, y + (n // 2), x + (n // 2), 
              y + (n // 2), x + (n // 2) - 1, y + (n // 2) - 1, grid)
     
    elif(r < x + (n // 2) and c >= y + (n // 2)):
        place(x + (n // 2), y + (n // 2) - 1, x + (n // 2), 
              y + (n // 2), x + (n // 2) - 1, y + (n // 2) - 1, grid)
     
    elif(r >= x + (n // 2) and c >= y + (n // 2)):
        place(x + (n // 2) - 1, y + (n // 2), x + (n // 2), 
              y + (n // 2) - 1, x + (n // 2) - 1, y + (n // 2) - 1, grid)
     
    tile((n // 2), x, y + (n // 2), grid)
    tile((n // 2), x, y, grid)
    tile((n // 2), x + (n // 2), y, grid)
    tile((n // 2), x + (n // 2), y + (n // 2), grid)
      


if __name__ == "__main__":
    main()

