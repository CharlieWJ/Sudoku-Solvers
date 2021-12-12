import time
from Backtrack import Backtrack
from LHL import LHL
from boards import cases, tests
# The only potentially tricky part will be making sure that the object type that represents the Sudoku puzzle
# is compatible with the various solvers for each algorithm.
# The general purpose libraries can generate test puzzles for you.

def compare():
    ##$ BACKTRACK TIMING
    backtrackTimes = {}
    b = Backtrack(tests["test1"])
    start = time.time()
    b.solve()
    stop = time.time() - start
    backtrackTimes["test1"] = stop
    print()
    b.setBoard(tests["test2"])
    start = time.time()
    b.solve()
    stop = time.time() - start
    backtrackTimes["test2"] = stop
    print()

    ###  LHL TIMING
    lhlTimes = {}
    lee = LHL()
    start = time.time()
    lee.solveSudoku(cases["case1"])
    stop = time.time() - start
    lhlTimes['case1'] = stop
    print()
    start = time.time()
    lee.solveSudoku(cases["case2"])
    stop = time.time() - start
    lhlTimes['case2'] = stop
    print("Backtrack Times:\n" + str(backtrackTimes))
    print("LHL Times:\n" + str(lhlTimes))

compare()
# -- Measurement libraries
# https://pypi.org/project/memory-profiler/ -- Analyze memory usage
# time module -- analyze runtime (use start = time.time(), runtime = time.time() - start and maybe matplotlib for charts)

# -- General purpose Sudoku libraries in Python
# -- Both can generate Sudoku puzzles with a specified difficulty.
# https://sudokutools.readthedocs.io/en/latest/index.html -- can generate Sudoku puzzles, solve in a few different ways
# https://pypi.org/project/py-sudoku/ -- Popular Python sudoku library

# -- Backtracking code
# https://python.plainenglish.io/solve-a-sudoku-puzzle-using-backtracking-in-python-8e9eb58e57e6#3498

#  -- Simulated annealing code
# https://github.com/erichowens/SudokuSolver
# https://www.adrian.idv.hk/2019-01-30-simanneal/
# https://github.com/challengingLuck/youtube/blob/master/sudoku/sudoku.py

# -- CSP code
# https://norvig.com/sudoku.html
# https://gist.github.com/ksurya/3940679

#  -- Genetic algorithm code
# https://github.com/ctjacobs/sudoku-genetic-algorithm
# https://github.com/chinyan/Genetic-Algorithm-based-Sudoku-Solver

# -- A Comparison of Algorithms
# https://github.com/MaximeDaigle/sudoku 

