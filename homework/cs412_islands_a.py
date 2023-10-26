"""
    name:  Chingiz Rajabli

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.
           Comments here on your code and submission.
"""


def largest_island(grid):
    """
    Finds the size of the largest island in the grid.
    """
    grid_size = len(grid)
    largest = 0
    visited = []

    def dfs(x, y):
        if 0 <= x < grid_size and 0 <= y < grid_size and grid[x][y] == 1 and (x, y) not in visited:
            visited.append((x, y))
            return 1 + dfs(x-1, y) + dfs(x+1, y) + dfs(x, y-1) + dfs(x, y+1)
        return 0
    
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 1 and (i, j) not in visited:
                largest = max(largest, dfs(i, j))
    
    return largest


def main():
    size = int(input())
    grid = [[0]*size]*size
    for i in range(size):
        grid[i] = list(map(int, input().split()))
    print(largest_island(grid))


if __name__ == "__main__":
    main()
