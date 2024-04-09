## PART ONE
#OG
def countSubIslands(grid1: List[List[int]], grid2: List[List[int]]) -> int:
    def dfs(row, col):
        if not 0 <= row < len(grid2) or not 0 <= col < len(grid2[0]) or not grid2[row][col]:
            return

        grid2[row][col] = 0
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    for row in range(len(grid2)):
        for col in range(len(grid2[0])):
            if grid2[row][col] and not grid1[row][col]:
                dfs(row, col)

    subIslands = 0
    for row in range(len(grid2)):
        for col in range(len(grid2[0])):
            if grid2[row][col]:
                dfs(row, col)
                subIslands += 1

    return subIslands

# PART TWO
# 40% of the 2nd grid is covered by 1st grid
from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(row, col):
            if not 0 <= row < len(grid2) or not 0 <= col < len(grid2[0]) or grid2[row][col] == 0:
                return 0, 0
            
            grid2[row][col] = 0  # Mark as visited
            total_cells = 1  # Total cells of the island in grid2
            overlap_cells = 1 if grid1[row][col] == 1 else 0  # Overlapping cells with grid1
            
            # Explore the four directions
            for d_row, d_col in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row, new_col = row + d_row, col + d_col
                total, overlap = dfs(new_row, new_col)
                total_cells += total
                overlap_cells += overlap
            
            return total_cells, overlap_cells
        
        subIslands = 0
        for row in range(len(grid2)):
            for col in range(len(grid2[0])):
                if grid2[row][col]:
                    total_cells, overlap_cells = dfs(row, col)
                    if overlap_cells / total_cells >= 0.4:  # Check if overlap is at least 40%
                        subIslands += 1
        
        return subIslands
    
    
# PART THREE
# 2nd grid subisland is at least 40% subset of other grid
def subIslands40(grid1, grid2):
    R, C = len(grid1), len(grid1[0])
    label = 2
    dirs = [(0,1), (0,-1), (1,0), (-1,0)]

    def dfs_label(row, col, label, grid):
        if not 0 <= row < R or not 0 <= col < C or grid1[row][col] != 1:
            return 0
        grid[row][col] = label
        size = 1
        for r, c in dirs:
            nr, nc = row + r, col + c
            size += dfs_label(nr, nc, label, grid)
        return size

    islandSizes = {}
    for row in range(R):
        for col in range(C):
            if grid1[row][col] == 1:
                islandSizes[label] = dfs_label(row, col, label, grid1)
                label += 1

    def is_sub(row, col):
        if not 0 <= row < R or not 0 <= col < C or grid2[row][col] != 1:
            return True, 0
        if grid1[row][col] == 0:
            return False, 0

        grid2[row][col] = 0
        isSub, size = True, 1
        for r, c in dirs:
            sub, sz = is_sub(row + r, col + c)
            isSub &= sub
            size += sz
        return isSub, size

    subIslands = 0
    for row in range(R):
        for col in range(C):
            if grid2[row][col] == 1:
                label = grid1[row][col]
                isSub, size = is_sub(row, col)

                if isSub and size >= 0.4 * islandSizes[label]:
                    subIslands += 1

    return subIslands

# Example usage
grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,1,1,0],[1,1,0,1,1]]
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]

print(subIslands40(grid1, grid2))  # Example output
grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]
grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]

print(subIslands40(grid1, grid2))  # Example output
grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]
grid2 = [[1,0,1,0,1],[1,1,1,0,1],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1]]

print(subIslands40(grid1, grid2))  # Example output