class Backtrack:
    def __init__(self, board):
        self.board = board
    
    def setBoard(self, board):
        self.board = board
    
    def printBoard(self):
        for row in self.board:
            print(row)

    def isPossible(self, row, col, val):
        for j in range(0, 9):
            if self.board[row][j] == val:
                return False

        for i in range(0, 9):
            if self.board[i][col] == val:
                return False

        startRow = (row // 3) * 3
        startCol = (col // 3) * 3
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[startRow+i][startCol+j] == val:
                    return False
        return True

    def solve(self):
        for i in range(0, 9):
            for j in range(0, 9):
                if self.board[i][j] == 0:
                    for val in range(1, 10):
                        if self.isPossible(i, j, val):
                            self.board[i][j] = val
                            self.solve()

                            # Bad choice, make it blank and check again
                            self.board[i][j] = 0
                    return
        # We found a solution, print it            
        self.printBoard()


#solve()
# board = [
#      [0, 0, 0, 8, 0, 0, 4, 0, 3],
#      [2, 0, 0, 0, 0, 4, 8, 9, 0],
#      [0, 9, 0, 0, 0, 0, 0, 0, 2],
#      [0, 0, 0, 0, 2, 9, 0, 1, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 7, 0, 6, 5, 0, 0, 0, 0],
#      [9, 0, 0, 0, 0, 0, 0, 8, 0],
#      [0, 6, 2, 7, 0, 0, 0, 0, 1],
#      [4, 0, 3, 0, 0, 6, 0, 0, 0]
# ]

# solver = Backtrack(board)
# solver.solve()