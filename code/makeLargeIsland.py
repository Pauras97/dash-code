class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < N and 0 <= nc < N:
                    yield(nr, nc)
        
        def dfs(row, col, index):
            ans = 1
            grid[row][col] = index
            for nr, nc in neighbors(row, col):
                if grid[nr][nc] == 1:
                    ans += dfs(nr, nc, index)
            return ans
        
        area = {}
        index = 2

        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    area[index] = dfs(r, c, index)
                    index += 1
        
        ans = max(area.values() or [0]) 

        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    seen = set()
                    for nr, nc in neighbors(r, c):
                        if grid[nr][nc] > 1:
                            seen.add(grid[nr][nc])
                    ans = max(ans, 1 + sum(area[i] for i in seen))

        return ans

solution = Solution()

grid = [[1,0],[0,1]]
print(solution.largestIsland(grid))

grid = [[1,1],[1,0]]
print(solution.largestIsland(grid))

grid = [[1,1],[1,1]]
print(solution.largestIsland(grid))

grid = [
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1]
]
print(solution.largestIsland(grid))


# You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

# Return the size of the largest island in grid after applying this operation.

# An island is a 4-directionally connected group of 1s.
