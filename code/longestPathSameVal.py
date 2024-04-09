class LongestPath:

    def getLongestPath(self, grid):
        
        longest = 0
        R, C = len(grid), len(grid[0])
        visited = set()
    
        def dfs(i, j):
            if (i, j) in visited:
                return 0
            
            currLongest = 0
            visited.add((i, j))
            
            for r, c in (0,1), (0, -1), (1, 0), (-1, 0):
                nr, nc = r + i, c + j
                if 0 <= nr < R and 0 <= nc < C and grid[i][j] == grid[nr][nc]:
                    currLongest = max(currLongest, dfs(nr, nc))
            
            visited.remove((i, j))
            return 1 + currLongest
                

        for row in range(R):
            for col in range(C):
                longest = max(dfs(row, col), longest)

        return longest

long = LongestPath()
nums = [
[1,1],
[5,5],
[5,5]
]
print(long.getLongestPath(nums))

nums = [[1, 1, 1, 1],
        [0, 1, 1, 0]]
print(long.getLongestPath(nums))

nums = [[0, 1, 0],
        [1, 1, 1]]
print(long.getLongestPath(nums))


nums = [[1, 1, 1, 2, 4],
        [5, 1, 5, 3, 1],
        [3, 4, 2, 1, 1]]
print(long.getLongestPath(nums))

