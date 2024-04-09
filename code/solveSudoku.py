class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def place_number(num, row, col):
            rows[row].add(num)
            cols[col].add(num)
            boxes[(row//3, col//3)].add(num)
            board[row][col] = str(num)
        
        def could_place(num, row, col):
            return num not in rows[row] and num not in cols[col] and num not in boxes[(row//3, col//3)]

        def remove_number(num, row, col):
            rows[row].remove(num)
            cols[col].remove(num)
            boxes[(row//3, col//3)].remove(num)
            board[row][col] = "."

        def place_next_numbers(row, col):
            if row == N - 1 and col == N - 1:
                nonlocal sudokuSolved
                sudokuSolved = True
            else:
                if col == N - 1:
                    backtrack(row + 1, 0)
                else:
                    backtrack(row, col + 1)
        
        def backtrack(row=0, col=0):
            if board[row][col] == ".":
                for num in range(1, 10):
                    if could_place(num, row, col):
                        place_number(num, row, col)
                        place_next_numbers(row, col)
                        if sudokuSolved:
                            return
                        remove_number(num, row, col)
            else:
                place_next_numbers(row, col)
        
        N = 9
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = {}

        for r in range(N):
            for c in range(N):
                boxes[(r//3, c//3)] = set()

        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    place_number(num, i, j)
        
        sudokuSolved = False
        backtrack()
        print(board)
    
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output =  [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]

soln = Solution()
soln.solveSudoku(board)

for r in range(9):
    print([char == Output[r][i] for i, char in enumerate(board[r])])
        