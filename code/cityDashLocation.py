# Given a grid where:
# - 'O' represents an open road that you can travel over in any direction (up, down, left, or right).
# - 'X' represents a blocked road that you cannot travel through.
# - 'D' represents a DashMart.

# The grid is provided as a 2D array, and a list of locations is provided where each location is a pair `[row, col]`.


city = [['X', 'O', 'O', 'D', 'O', 'O', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X', 'X', 'O', 'X', 'O', 'X'],
        ['O', 'O', 'O', 'D', 'X', 'X', 'O', 'X', 'O'],
        ['O', 'O', 'D', 'O', 'D', 'O', 'O', 'O', 'X'],
        ['O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'X'],
        ['X', 'O', 'X', 'O', 'O', 'O', 'O', 'X', 'X']]

locations = [[0,5],
            [0,7],
            [3, 0],
            [5, 6],
            [2, 1]]

output = [[-1]*len(city[0]) for _ in range(len(city))]

R, C = len(city), len(city[0])
visited = set()
queue = deque()

for row in range(R):
    for col in range(C):
        if city[row][col] == 'D':
            queue.append((row, col))
            visited.add((row, col))

def addRoom(row, col):
    if not 0 <= row < R or not 0 <= col < C or (row,col) in visited or city[row][col] == 'X':
        return
    
    visited.add((row, col))
    queue.append((row, col))

dist = 0
while queue:
    for _ in range(len(queue)):
        r,c = queue.popleft()
        output[r][c] = dist
        addRoom(r+1, c)
        addRoom(r-1, c)
        addRoom(r, c+1)
        addRoom(r, c-1)
    dist += 1

for row, col in locations:
    print(output[row][col])
            