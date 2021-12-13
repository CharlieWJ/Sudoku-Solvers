import constraint as cp
from boards import nums
## Not used in comparisons 
class CSPSuryak:
    # About: Sudoku Solver using constraint programming
    # Author: suryak
    # Description:
    #       * Requires constraint lib
    #       * Takes sudoku puzzle input via text file
    #       * Empty locations are required to be filled with 0
    #       * Output can be observed on console
    # Note: This is written using Python 2.7
    def __init__(self) -> None:
        pass
    # Normalizes sudoku solution
    def dataNormalize(self, data):
        """
        args: data; output from sudoku_solve()
        returns: Normalized output of input - Diplayed at console
        """
        sudoku_nums = [ eachPos[1] for eachPos in sorted(data[0].items()) ]
        for step in range(0,81,9):
            print(sudoku_nums[step:step+9])

    # Solves the sudoku puzzle
    def sudoku_solve(self, nums):
        """
        args: array of the board (modified)
        returns: Sudoku solution
        return type: list
        description:
            * It reads sudoku puzzle input via text file.
            * Creates problem instance, sudoku = Problem()
            * Adds sudoku input and their indices as variables
            * Adds constraints to the problem
                1. No two numbers in a row should be same
                2. No two numbers in a column should be same
                3. No two numbers in a 3x3 box shoud be same
            * returns the solution
        """
        # reads the puzzle from file
        ## ENTER FILE NAME HERE
        #fileName = input("Enter file name: ")
        #if fileName.strip() == "":
        #    fileName = "csptest.txt"
        #puzzleNums = open(fileName).read()
        # stores the numbers in a list. Ex: [1,2,9,0,3...]
        puzzleNums = nums #[ int(eachNum) for eachNum in puzzleNums.split() ]
        # Problem instance created.
        # Recursive backtracking is used here
        sudoku = cp.Problem(cp.RecursiveBacktrackingSolver())
        # List of 9x9 sudoku puzzle indices. Ex: [(0,0), (0,1).. (9,9)]
        sudokuIndex = [ (row, col) for row in range(9) for col in range(9) ]
        # adding variables to the sudoku instance
        for eachIndex,eachNum in zip(sudokuIndex, puzzleNums):
            # If empty location is found, its range is set to 1-10
            if eachNum == 0:
                sudoku.addVariable(eachIndex, range(1,10) )
            # If not an empty location, its a value is assigned
            else:
                sudoku.addVariable(eachIndex, [eachNum] )

        # constraints for each row and column
        # counting from 0-9 (numeber of rows/ columns)
        var = 0
        for aCount in range(9):
            # A list of locations present in a row.
            rowIndices = [ (var, col) for col in range(9) ]
            # Adding constraint
            # No two numbers in a row should be same
            sudoku.addConstraint( cp.AllDifferentConstraint(), rowIndices )
            # A list of locations present in a column
            colIndices = [ (row, var) for row in range(9) ]
            # Adding constraint
            # No two numbers in a column should be same
            sudoku.addConstraint( cp.AllDifferentConstraint(), colIndices )
            var+=1

        # constraints for each block (3x3) of board
        # Finding all boxes in sudoku board. Its 9 in this case
        rowStep = 0
        colStep = 0
        while rowStep < 9:
            colStep = 0
            while colStep < 9:
                # list of locations present in a box
                boxIndices = [ (row, col) for row in range(rowStep, rowStep+3) \
                                for col in range(colStep, colStep+3)]
                # Adding constraint
                # No two numbers in the box should be same
                sudoku.addConstraint( cp.AllDifferentConstraint(), boxIndices )
                colStep+=3
            rowStep+=3
        # return the solution
        return sudoku.getSolutions()


# solver = CSPSuryak()
# if __name__ == '__main__':
#     print("sudoku output\n\n")
#     solver.dataNormalize(solver.sudoku_solve(nums['num1']))
#     #input("\n\nEnter any key to exit")