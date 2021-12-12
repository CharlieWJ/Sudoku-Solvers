class LHL:
    def __init__(self):
        self.InBlock, self.InRow, self.InCol = [0] * 81, [0] * 81, [0] * 81 
        self.BLANK = 0 
        self.ONES = 0x3fe  	                  # Binary 1111111110
        self.Entry = [0] * 81                 # Records entries 1-9 in the grid, as the corresponding bit set to 1
        self.Block, self.Row, self.Col = [0] * 9, [0] * 9, [0] * 9	# Each int is a 9-bit array
        self.SeqPtr = 0
        self.Sequence = [0] * 81
        self.solved = []

    #                  int, int
    def SwapSeqEntries(self, S1, S2):
        temp = self.Sequence[S2]
        self.Sequence[S2] = self.Sequence[S1]
        self.Sequence[S1] = temp


    # int, int, int
    def InitEntry(self, i, j, val):
        Square = 9 * i + j 
        valbit = 1 << val 
        SeqPtr2 = 0 
        #print(valbit)
        
        # add suitable checks for data consistency
        
        self.Entry[Square] = valbit
        idx = int(self.InBlock[Square])
        if idx < 9:
            self.Block[idx] = self.Block[idx] & ~valbit

        idx = int(self.InCol[Square])
        if idx < 9:
            self.Col[idx] = self.Col[idx] & ~valbit  # Simpler Col[j] &= ~valbit

        idx = int(self.InRow[Square])
        if idx < 9:
            self.Row[idx] = self.Row[idx] & ~valbit  # Simpler Row[i] &= ~valbit 
        SeqPtr2 = self.SeqPtr 
        while SeqPtr2 < 81 and self.Sequence[SeqPtr2] != Square:
            SeqPtr2 += 1
        self.SwapSeqEntries(self.SeqPtr, SeqPtr2) 
        self.SeqPtr += 1

    #             char[][]
    def PrintArray(self):
        Square = 0
        ch = ''
        for i in range(9):
            for j in range(9):
                valbit = self.Entry[Square] 
                Square += 1
                if valbit == 0:
                    ch = '-' 
                else:
                    for val in range(1,10):
                        if (valbit == (1 << val)):
                            ch = str(val)
                            break
                self.solved[i][j] = ch

    # Returns int, param is int
    def NextSeq(self, s):
        s2 = 0
        MinBitCount = 100

        for t in range(s, 81):
            Square = self.Sequence[t]
            idx, jdx = int(self.InBlock[Square]), int(self.InCol[Square])
            if idx < 9 and jdx < 9:
                Possibles = self.Block[idx] & self.Row[idx] & self.Col[jdx]
            BitCount = 0
            while (Possibles):
                Possibles = Possibles & ~(Possibles & -Possibles) 
                BitCount += 1

            if (BitCount < MinBitCount):
                MinBitCount = BitCount
                s2 = t
        return s2 


    #              int, [][] char
    def Place(self, s):
        if (s >= 81):
            self.PrintArray()
            return 
        
        s2 = self.NextSeq(s)
        self.SwapSeqEntries(s, s2)
        Square = self.Sequence[s] 
        BlockIndex = int(self.InBlock[Square])
        RowIndex = int(self.InRow[Square])
        ColIndex = int(self.InCol[Square])
        
        Possibles = 0
        if BlockIndex < 9 and RowIndex < 9 and ColIndex < 9:
            Possibles = self.Block[BlockIndex] & self.Row[RowIndex] & self.Col[ColIndex]

        while (Possibles):
            valbit = Possibles & (-1*Possibles)  # Lowest 1 bit in Possibles
            Possibles = Possibles & ~valbit 
            self.Entry[Square] = valbit
            self.Block[BlockIndex] = self.Block[BlockIndex] & ~valbit
            self.Row[RowIndex] = self.Row[RowIndex] & ~valbit
            self.Col[ColIndex] = self.Col[ColIndex] & ~valbit 
            self.Place(s + 1)
            self.Entry[Square] = self.BLANK  # Could be moved out of the loop
            self.Block[BlockIndex] = self.Block[BlockIndex] | valbit 
            self.Row[RowIndex] = self.Row[RowIndex] | valbit 
            self.Col[ColIndex] = self.Col[ColIndex] | valbit 

        self.SwapSeqEntries(s, s2) 

    #               char[][]
    def solveSudoku(self, board):
        self.SeqPtr = 0 
        self.solved = board[:]
        for i in range(9):
            for j in range(9):
                Square = 9 * i + j
                self.InRow[Square] = i
                self.InCol[Square] = j
                self.InBlock[Square] = (i // 3) * 3 + ( j // 3) 
        for i in range(81):
            self.Sequence[i] = i 
            self.Entry[i] = self.BLANK 
        
        for i in range(9):
            self.Block[i] = self.Row[i] = self.Col[i] = self.ONES
        
        for i in range(9):
            for j in range(9):
                if ('.' != self.solved[i][j]):
                    self.InitEntry(i, j, int(self.solved[i][j])) 

        self.Place(self.SeqPtr)
        #print(self.solved)
        self.showBoard()

        #return self.solved

    def showBoard(self):
        for x in self.solved:
            print(x)

# solver = LHL()
# case1 = [
#         ["5","3",".",".","7",".",".",".","."],
#         ["6",".",".","1","9","5",".",".","."],
#         [".","9","8",".",".",".",".","6","."],
#         ["8",".",".",".","6",".",".",".","3"],
#         ["4",".",".","8",".","3",".",".","1"],
#         ["7",".",".",".","2",".",".",".","6"],
#         [".","6",".",".",".",".","2","8","."],
#         [".",".",".","4","1","9",".",".","5"],
#         [".",".",".",".","8",".",".","7","9"]]

# solver.solveSudoku(case1)