def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    dirs = [[0,1], [0,-1], [1,0], [-1,0]]
    R, C = len(matrix), len(matrix[0])

    cache = [[0] * C for _ in range(R)]
    ans = 0

    def dfs(i, j):
        if cache[i][j]:
            return cache[i][j]

        for r, c in dirs:
            nr, nc = i + r, j + c
            if not 0 <= nr < R or not 0 <= nc < C or matrix[nr][nc] >= matrix[i][j]:
                continue

            cache[i][j] = max(cache[i][j], dfs(nr, nc))

        cache[i][j] += 1
        return cache[i][j]

    for i in range(R):
        for j in range(C):
            ans = max(ans, dfs(i, j))

    return ans