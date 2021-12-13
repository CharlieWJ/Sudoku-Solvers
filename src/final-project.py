import time
from Backtrack import Backtrack
from LHL import LHL
# import CSP as csp
import Solvers as solvers
import GA as ga
from GA_Probs import easyGA, mediumGA, hardGA
from boards import easyBackTrack, easyLHL, easySet
import numpy as np
from memory_profiler import memory_usage
# The only potentially tricky part will be making sure that the object type that represents the Sudoku puzzle
# is compatible with the various solvers for each algorithm.
# The general purpose libraries can generate test puzzles for you.


btime = "Backtrack Times:\n"
btimeMean = "Backtracking Avg. Time:\n"
lhlStr = "LHL Times:\n"
lhltimeMean = "LHL Avg. Time:\n"
saStr = "Simulated Annealing Times:\n"
satimeMean = "Simulated Annealing Avg. Time:\n"
cspStr = "Norvig CSP Times:\n"
csptimeMean = "Norvig CSP Avg. Time:\n"
line = "----------"

bmem = "Backtrack Memory:\n"
bmemMean = "Backtracking Avg. Memory:\n"
lhlmemStr = "LHL Memory:\n"
lhlmemMean = "LHL Avg. Memory:\n"
samemStr = "Simulated Annealing Memory:\n"
samemMean = "Simulated Annealing Avg. Memory:\n"
cspmemStr = "Norvig CSP Memory:\n"
cspmemMean = "Norvig CSP Avg. Memory:\n"

memUse = "---- MEMORY USAGE ----"
avgTimeStr = "---- AVERAGE TIMES ----"
avgMemStr = "---- AVERAGE MEMORY USAGE ----"


def average(dct):
    vals = dct.values()
    mean = sum(vals)/len(vals)
    return mean

def compareEasy():
    ### BACKTRACK TIMING
    backtrackTimes = {}
    backtrackMemory = {}
    b = Backtrack()
    caseNames = easyBackTrack.keys()
    for n in caseNames:
        start = time.time()
        b.setBoard(easyBackTrack[n])
        b.solve()
        stop = time.time() - start
        mem = memory_usage((b.setBoard, (easyBackTrack[n],)), max_usage=True)
        mem += memory_usage((b.solve, ), max_usage=True)
        backtrackTimes[n] = stop
        backtrackMemory[n] = mem
        print()
    print()

    ###  LHL TIMING
    lhlTimes = {}
    lhlMem = {}
    lee = LHL()
    caseNames = easyLHL.keys()
    for n in caseNames:
        start = time.time()
        lee.solveSudoku(easyLHL[n])
        stop = time.time() - start
        mem = memory_usage((lee.solveSudoku, (easyLHL[n],)), max_usage=True)
        lhlTimes[n] = stop
        lhlMem[n] = mem
    print()
    
    ### SIMULATED ANNEALING
    saTimes = {}
    saMemory = {}
    caseNames = easySet.keys()
    for n in caseNames:
        start = time.time()
        simAn = solvers.solve_simulated_annealing(easySet[n])
        solvers.display(simAn)
        stop = time.time() - start
        mem, simAn = memory_usage((solvers.solve_simulated_annealing, (easySet[n],)), max_usage=True, retval=True)
        mem += memory_usage((solvers.display, (simAn,)), max_usage=True)
        saTimes[n] = stop
        saMemory[n] = mem

    ### Norvig CSP
    norvigTimes = {}
    norvigMemory = {}
    for n in caseNames:
        start = time.time()
        norvig = solvers.solve(easySet[n])
        solvers.display(norvig)
        stop = time.time() - start
        mem, norvig = memory_usage((solvers.solve, (easySet[n],)), max_usage=True, retval=True)
        mem += memory_usage((solvers.display, (norvig,)), max_usage=True)
        norvigTimes[n] = stop
        norvigMemory[n] = mem

    ### Genetic Algorithm
    # gaTimes = {}
    # gaMemory = {}
    # caseNames = easyGA.keys()
    # genetic = ga.Sudoku()
    # for n in caseNames:
    #     start = time.time()
    #     grid = np.array(list(easyGA[n])).reshape((9,9)).astype(int)
    #     genetic.load(grid)
    #     generation, solution = genetic.solve()
    #     print(solution.values)
    #     stop = time.time() - start
    #     mem = memory_usage((genetic.load, (grid,)), max_usage=True)
    #     gaMemory[n] = mem
    #     mem, gs = memory_usage((genetic.solve, ), max_usage=True, retval=True)
    #     gaTimes[n] = stop
    #     gaMemory[n] += mem
    

    ### PRINT TIMES
    print("---- TIME TO COMPLETE EASY ----")
    print(btime + str(backtrackTimes))
    print(line)
    print(lhlStr + str(lhlTimes))
    print(line)
    print(saStr + str(saTimes))
    print(line)
    print(cspStr + str(norvigTimes))
    print(line)
    #print("Genetic Algorithm Times:\n" + str(gaTimes))

    ### PRINT MEMORY
    print(memUse)
    print(bmem + str(backtrackMemory))
    print(line)
    print(lhlmemStr + str(lhlMem))
    print(line)
    print(samemStr + str(saMemory))
    print(line)
    print(cspmemStr + str(norvigMemory))
    print(line)

    ### AVERERAGE TIMES
    print(avgTimeStr)
    print(btimeMean + str(average(backtrackTimes)))
    print(line)
    print(lhltimeMean + str(average(lhlTimes)))
    print(line)
    print(satimeMean + str(average(saTimes)))
    print(line)
    print(csptimeMean + str(average(norvigTimes)))
    print(line)

    ### AVERAGE MEMORY
    print(avgMemStr)
    print(bmemMean + str(average(backtrackMemory)))
    print(line)
    print(lhlmemMean + str(average(lhlMem)))
    print(line)
    print(samemMean + str(average(saMemory)))
    print(line)
    print(cspmemMean + str(average(norvigMemory)))
    print(line)


from boards import medBackTrack, medLHL, mediumSet
def compareMed():
    ### BACKTRACK TIMING
    backtrackTimes = {}
    backtrackMemory = {}
    b = Backtrack()
    caseNames = medBackTrack.keys()
    for n in caseNames:
        start = time.time()
        b.setBoard(medBackTrack[n])
        b.solve()
        stop = time.time() - start
        mem = memory_usage((b.setBoard, (medBackTrack[n],)), max_usage=True)
        mem += memory_usage((b.solve, ), max_usage=True)
        backtrackTimes[n] = stop
        backtrackMemory[n] = mem
        print()
    print()

    ###  LHL TIMING
    lhlTimes = {}
    lhlMem = {}
    lee = LHL()
    caseNames = medLHL.keys()
    for n in caseNames:
        start = time.time()
        lee.solveSudoku(medLHL[n])
        stop = time.time() - start
        mem = memory_usage((lee.solveSudoku, (medLHL[n],)), max_usage=True)
        lhlTimes[n] = stop
        lhlMem[n] = mem
    print()
    
    ### SIMULATED ANNEALING
    saTimes = {}
    saMemory = {}
    caseNames = mediumSet.keys()
    for n in caseNames:
        start = time.time()
        simAn = solvers.solve_simulated_annealing(mediumSet[n])
        solvers.display(simAn)
        stop = time.time() - start
        mem, simAn = memory_usage((solvers.solve_simulated_annealing, (mediumSet[n],)), max_usage=True, retval=True)
        mem += memory_usage((solvers.display, (simAn,)), max_usage=True)
        saTimes[n] = stop
        saMemory[n] = mem

    ### Norvig CSP
    norvigTimes = {}
    norvigMemory = {}
    for n in caseNames:
        start = time.time()
        norvig = solvers.solve(mediumSet[n])
        solvers.display(norvig)
        stop = time.time() - start
        mem, norvig = memory_usage((solvers.solve, (mediumSet[n],)), max_usage=True, retval=True)
        mem += memory_usage((solvers.display, (norvig,)), max_usage=True)
        norvigTimes[n] = stop
        norvigMemory[n] = mem

    ### Genetic Algorithm (VOID TAKES TOO LONG)
    # gaTimes = {}
    # gaMemory = {}
    # caseNames = easyGA.keys()
    # genetic = ga.Sudoku()
    # for n in caseNames:
    #     start = time.time()
    #     grid = np.array(list(easyGA[n])).reshape((9,9)).astype(int)
    #     genetic.load(grid)
    #     generation, solution = genetic.solve()
    #     print(solution.values)
    #     stop = time.time() - start
    #     mem = memory_usage((genetic.load, (grid,)), max_usage=True)
    #     gaMemory[n] = mem
    #     mem, gs = memory_usage((genetic.solve, ), max_usage=True, retval=True)
    #     gaTimes[n] = stop
    #     gaMemory[n] += mem
    

    ### PRINT TIMES
    print("---- TIME TO COMPLETE MEDIUM ----")
    print(btime + str(backtrackTimes))
    print(line)
    print(lhlStr + str(lhlTimes))
    print(line)
    print(saStr + str(saTimes))
    print(line)
    print(cspStr + str(norvigTimes))
    print(line)
    #print("Genetic Algorithm Times:\n" + str(gaTimes))

    ### PRINT MEMORY
    print(memUse)
    print(bmem + str(backtrackMemory))
    print(line)
    print(lhlmemStr + str(lhlMem))
    print(line)
    print(samemStr + str(saMemory))
    print(line)
    print(cspmemStr + str(norvigMemory))
    print(line)

    ### AVERERAGE TIMES
    print(avgTimeStr)
    print(btimeMean + str(average(backtrackTimes)))
    print(line)
    print(lhltimeMean + str(average(lhlTimes)))
    print(line)
    print(satimeMean + str(average(saTimes)))
    print(line)
    print(csptimeMean + str(average(norvigTimes)))
    print(line)

    ### AVERAGE MEMORY
    print(avgMemStr)
    print(bmemMean + str(average(backtrackMemory)))
    print(line)
    print(lhlmemMean + str(average(lhlMem)))
    print(line)
    print(samemMean + str(average(saMemory)))
    print(line)
    print(cspmemMean + str(average(norvigMemory)))
    print(line)


from boards import hardBackTrack, hardLHL, hardSet
def compareHard():
    ### BACKTRACK TIMING
    backtrackTimes = {}
    backtrackMemory = {}
    b = Backtrack()
    caseNames = hardBackTrack.keys()
    for n in caseNames:
        start = time.time()
        b.setBoard(hardBackTrack[n])
        b.solve()
        stop = time.time() - start
        mem = memory_usage((b.setBoard, (hardBackTrack[n],)), max_usage=True)
        mem += memory_usage((b.solve, ), max_usage=True)
        backtrackTimes[n] = stop
        backtrackMemory[n] = mem
        print()
    print()

    ###  LHL TIMING
    lhlTimes = {}
    lhlMem = {}
    lee = LHL()
    caseNames = hardLHL.keys()
    for n in caseNames:
        start = time.time()
        lee.solveSudoku(hardLHL[n])
        stop = time.time() - start
        mem = memory_usage((lee.solveSudoku, (hardLHL[n],)), max_usage=True)
        lhlTimes[n] = stop
        lhlMem[n] = mem
    print()
    
    ### SIMULATED ANNEALING
    saTimes = {}
    saMemory = {}
    caseNames = hardSet.keys()
    for n in caseNames:
        start = time.time()
        simAn = solvers.solve_simulated_annealing(hardSet[n])
        solvers.display(simAn)
        stop = time.time() - start
        mem, simAn = memory_usage((solvers.solve_simulated_annealing, (hardSet[n],)), max_usage=True, retval=True)
        mem += memory_usage((solvers.display, (simAn,)), max_usage=True)
        saTimes[n] = stop
        saMemory[n] = mem

    ### Norvig CSP
    norvigTimes = {}
    norvigMemory = {}
    for n in caseNames:
        start = time.time()
        norvig = solvers.solve(hardSet[n])
        solvers.display(norvig)
        stop = time.time() - start
        mem, norvig = memory_usage((solvers.solve, (hardSet[n],)), max_usage=True, retval=True)
        mem += memory_usage((solvers.display, (norvig,)), max_usage=True)
        norvigTimes[n] = stop
        norvigMemory[n] = mem

    ### Genetic Algorithm (TAKES TOO LONG)
    # gaTimes = {}
    # gaMemory = {}
    # caseNames = hardGA.keys()
    # genetic = ga.Sudoku()
    # for n in caseNames:
    #     start = time.time()
    #     grid = np.array(list(hardGA[n])).reshape((9,9)).astype(int)
    #     genetic.load(grid)
    #     generation, solution = genetic.solve()
    #     print(solution.values)
    #     stop = time.time() - start
    #     mem = memory_usage((genetic.load, (grid,)), max_usage=True)
    #     gaMemory[n] = mem
    #     mem, gs = memory_usage((genetic.solve, ), max_usage=True, retval=True)
    #     gaTimes[n] = stop
    #     gaMemory[n] += mem
    

    ### PRINT TIMES
    print("---- TIME TO COMPLETE HARD ----")
    print(btime + str(backtrackTimes))
    print(line)
    print(lhlStr + str(lhlTimes))
    print(line)
    print(saStr + str(saTimes))
    print(line)
    print(cspStr + str(norvigTimes))
    print(line)
    #print("Genetic Algorithm Times:\n" + str(gaTimes))

    ### PRINT MEMORY
    print(memUse)
    print(bmem + str(backtrackMemory))
    print(line)
    print(lhlmemStr + str(lhlMem))
    print(line)
    print(samemStr + str(saMemory))
    print(line)
    print(cspmemStr + str(norvigMemory))
    print(line)

    ### AVERERAGE TIMES
    print(avgTimeStr)
    print(btimeMean + str(average(backtrackTimes)))
    print(line)
    print(lhltimeMean + str(average(lhlTimes)))
    print(line)
    print(satimeMean + str(average(saTimes)))
    print(line)
    print(csptimeMean + str(average(norvigTimes)))
    print(line)

    ### AVERAGE MEMORY
    print(avgMemStr)
    print(bmemMean + str(average(backtrackMemory)))
    print(line)
    print(lhlmemMean + str(average(lhlMem)))
    print(line)
    print(samemMean + str(average(saMemory)))
    print(line)
    print(cspmemMean + str(average(norvigMemory)))
    print(line)


#compareEasy()
#compareMed()
compareHard()


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


#Simulated Annealing Times (BEFORE COLLECTING MEMORY):
# {'Easy1': 0.00503087043762207, 'Easy2': 0.004664897918701172, 
# 'Easy3': 0.005076885223388672, 'Easy4': 0.0048139095306396484, 
# 'Easy5': 0.0037000179290771484, 'Easy6': 0.0038671493530273438, 
# 'Easy7': 0.004639863967895508, 'Easy8': 0.004517078399658203, 
# 'Easy9': 0.003696918487548828, 'Easy1.': 0.003927946090698242}

#Simulated Annealing Times:
# {'Easy1': 0.08587193489074707, 'Easy2': 0.08969926834106445,
# 'Easy3': 0.08126187324523926, 'Easy4': 0.09015417098999023, 
# 'Easy5': 0.0728461742401123, 'Easy6': 0.07573771476745605, 
# 'Easy7': 0.13298606872558594, 'Easy8': 0.08292579650878906, 
# 'Easy9': 0.12128520011901855, 'Easy1.': 0.09370207786560059}



#Genetic Algorithm Times:
# {'Easy1': 11.565937757492065, 'Easy2': 14.857425212860107,
# 'Easy3': 16.82987904548645, 'Easy4': 7.253486156463623,
# 'Easy5': 9.057284832000732, 'Easy6': 8.421495199203491,
# 'Easy7': 15.95216679573059, 'Easy8': 11.79118013381958, 
# 'Easy9': 5.475762844085693, 'Easy10': 16.946889877319336}

#Genetic Algorithm Memory:
# {'Easy1': 101.6640625, 'Easy2': 102.2265625,
# 'Easy3': 102.45703125, 'Easy4': 102.4765625, 
# 'Easy5': 102.484375, 'Easy6': 102.5078125, 
# 'Easy7': 102.89453125, 'Easy8': 103.28515625, 
# 'Easy9': 74.5234375, 'Easy10': 74.54296875}