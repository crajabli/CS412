def dfs(grid, i, j, visited):
    """
    Performs a DFS on the grid starting from cell (i, j) and marks all adjacent cells that contain a 1 as visited.
    """
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0 or visited[i][j]:
        return 0
    
    visited[i][j] = True
    size = 1
    
    size += dfs(grid, i+1, j, visited)
    size += dfs(grid, i-1, j, visited)
    size += dfs(grid, i, j+1, visited)
    size += dfs(grid, i, j-1, visited)
    
    return size

def largest_island(grid):
    """
    Finds the size of the largest island in the grid.
    """
    largest = 0
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and not visited[i][j]:
                size = dfs(grid, i, j, visited)
                largest = max(largest, size)
    
    return largest

def main():
    size = int(input())
    grid = [[False]*size]*size
    print(grid)


if __name__ == "__main__":
    main()
