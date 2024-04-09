## TIME kMN where k is buildings
def shortestDistance(grid: List[List[int]]) -> int:
        
    rows = len(grid)   
    cols = len(grid[0])
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    
    walk = 0
    mindist = float('inf')
    
    total = [[0] * cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                minDist = float('inf')
                queue = deque([(i, j, 0)])
                
                while queue:
                    r, c, dist = queue.popleft()
                    for x, y in dirs:
                        nr, nc = r + x, c + y
                        if not 0 <= nr < rows or not 0 <= nc < cols or grid[nr][nc] != walk:
                            continue
                        grid[nr][nc] -= 1
                        total[nr][nc] += dist + 1
                        minDist = min(minDist, total[nr][nc])
                        queue.append((nr, nc, dist + 1))
                
                walk -= 1
                if minDist == float('inf'): return -1
    
    return minDist

grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
print(shortestDistance(grid))
            
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        