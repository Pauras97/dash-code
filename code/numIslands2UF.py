#TIME = O(k * α(m * n)), where:
# k is the number of positions (operations)
# α(m * n) is the Inverse Ackermann function, which grows very slowly for reasonable values of m and n (practically considered a constant).

#SPACE = O(k) worst case O(m*n)
def numIslands2(m: int, n: int, positions: List[List[int]]) -> List[int]:

    ans = []
    uf = UnionFind()

    for x, y in positions:
        if (x, y) in uf.id:
            ans.extend([uf.count])
        else:
            uf.add((x, y))
            for r, c in (0, 1), (0, -1), (1, 0), (-1, 0):
                nr, nc = x + r, y + c
                if (nr, nc) in  uf.id:
                    uf.union((x, y), (nr, nc))
            ans.extend([uf.count])
    return ans

class UnionFind:
    def __init__(self):
        self.id = {}
        self.size = {}
        self.count = 0
    
    def add(self, position):
        self.id[position] = position
        self.size[position] = 1
        self.count += 1
    
    def find(self, x):
        while x != self.id[x]:
            x = self.id[self.id[x]]
        return x
    
    def union(self, x, y):
        parX = self.find(x)
        parY = self.find(y)

        if parX == parY:
            return
        if self.size[parX] < self.size[parY]:
            self.id[parX] = parY
            self.size[parY] += self.size[parX]
            self.count -= 1
        else:
            self.id[parY] = parX
            self.size[parX] += self.size[parY]
            self.count -= 1
    
    
m, n = 3, 3
positions = [[0,0],[0,1],[1,2],[2,1]]
print(numIslands2(m, n, positions))

m, n = 1, 1
positions = [[0,0]]
print(numIslands2(m, n, positions))

m, n = 3, 3
positions = [[0,1],[1,2],[2,1],[1,0],[0,2],[0,0],[1,1]]
print(numIslands2(m, n, positions))


# You are given an empty 2D binary grid grid of size m x n. 
#The grid represents a map where 0's represent water and 1's represent land. 
#Initially, all the cells of grid are water cells (i.e., all the cells are 0's).

# We may perform an add land operation which turns the water at position into a land.
#You are given an array positions where positions[i] = [ri, ci] is the position (ri, ci) at which we should operate the ith operation.

# Return an array of integers answer where answer[i] is the number of islands after turning the cell (ri, ci) into a land.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
#You may assume all four edges of the grid are all surrounded by water.