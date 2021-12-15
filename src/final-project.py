import time
import funcs
from Backtrack import Backtrack
from LHL import LHL
import Solvers as solvers
from boards import easyBackTrack, easyLHL, easySet
from memory_profiler import memory_usage

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
        mem = memory_usage((b.setBoard, (easyBackTrack[n],)))#, max_usage=True)
        mem = sum(mem)
        mem += sum(memory_usage((b.solve, )))#, max_usage=True))
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
        mem = sum(memory_usage((lee.solveSudoku, (easyLHL[n],))))#, max_usage=True)
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
        mem, simAn = memory_usage((solvers.solve_simulated_annealing, (easySet[n],)), retval=True) #, max_usage=True, retval=True)
        mem = sum(mem)
        mem += sum(memory_usage((solvers.display, (simAn,))))#, max_usage=True)
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
        mem, norvig = memory_usage((solvers.solve, (easySet[n],)), retval=True) #, max_usage=True, retval=True)
        mem = sum(mem)
        mem += sum(memory_usage((solvers.display, (norvig,))))#, max_usage=True)
        norvigTimes[n] = stop
        norvigMemory[n] = mem

    print("---- TIME TO COMPLETE EASY ----")
    funcs.printResults(backtrackTimes, lhlTimes, saTimes, norvigTimes, backtrackMemory, lhlMem, saMemory, norvigMemory)
    funcs.writeResults(backtrackTimes, lhlTimes, saTimes, norvigTimes, backtrackMemory, lhlMem, saMemory, norvigMemory, "ResultsEasy.txt") 
    funcs.plotCases(backtrackTimes, lhlTimes, saTimes, norvigTimes, "Easy")
    funcs.plotMemory(backtrackMemory, lhlMem, saMemory, norvigMemory, "Easy")



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
        #mem = memory_usage((b.setBoard, (medBackTrack[n],)), max_usage=True)
        #mem += memory_usage((b.solve, ), max_usage=True)
        mem = sum(memory_usage((b.setBoard, (medBackTrack[n],))))#, max_usage=True)
        mem += sum(memory_usage((b.solve, )))#, max_usage=True))
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
        #mem = memory_usage((lee.solveSudoku, (medLHL[n],)), max_usage=True)
        mem = sum(memory_usage((lee.solveSudoku, (medLHL[n],))))#, max_usage=True)
        #mem += sum(mem)
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
        #mem, simAn = memory_usage((solvers.solve_simulated_annealing, (mediumSet[n],)), max_usage=True, retval=True)
        #mem += memory_usage((solvers.display, (simAn,)), max_usage=True)
        mem, simAn = memory_usage((solvers.solve_simulated_annealing, (mediumSet[n],)), retval=True) #, max_usage=True, retval=True)
        mem = sum(mem)
        mem += sum(memory_usage((solvers.display, (simAn,))))#, max_usage=True)
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
        #mem, norvig = memory_usage((solvers.solve, (mediumSet[n],)), max_usage=True, retval=True)
        #mem += memory_usage((solvers.display, (norvig,)), max_usage=True)
        mem, norvig = memory_usage((solvers.solve, (mediumSet[n],)), retval=True) #, max_usage=True, retval=True)
        mem = sum(mem)
        mem += sum(memory_usage((solvers.display, (norvig,))))#, max_usage=True)
        norvigTimes[n] = stop
        norvigMemory[n] = mem    

    ### PRINT TIMES
    print("---- TIME TO COMPLETE MEDIUM ----")
    funcs.printResults(backtrackTimes, lhlTimes, saTimes, norvigTimes, backtrackMemory, lhlMem, saMemory, norvigMemory)
    funcs.writeResults(backtrackTimes, lhlTimes, saTimes, norvigTimes, backtrackMemory, lhlMem, saMemory, norvigMemory, "ResultsMed.txt")
    funcs.plotCases(backtrackTimes, lhlTimes, saTimes, norvigTimes, "Medium")
    funcs.plotMemory(backtrackMemory, lhlMem, saMemory, norvigMemory, "Medium")


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
        #mem = memory_usage((b.setBoard, (hardBackTrack[n],)), max_usage=True)
        #mem += memory_usage((b.solve, ), max_usage=True)
        mem = sum(memory_usage((b.setBoard, (hardBackTrack[n],))))#, max_usage=True)
        mem += sum(memory_usage((b.solve, )))#, max_usage=True))
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
        #mem = memory_usage((lee.solveSudoku, (hardLHL[n],)), max_usage=True)
        mem = sum(memory_usage((lee.solveSudoku, (hardLHL[n],))))#, max_usage=True)
        #mem += sum(mem)
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
        #mem, simAn = memory_usage((solvers.solve_simulated_annealing, (hardSet[n],)), max_usage=True, retval=True)
        #mem += memory_usage((solvers.display, (simAn,)), max_usage=True)
        mem, simAn = memory_usage((solvers.solve_simulated_annealing, (hardSet[n],)), retval=True) #, max_usage=True, retval=True)
        mem = sum(mem)
        mem += sum(memory_usage((solvers.display, (simAn,))))#, max_usage=True)
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
        #mem, norvig = memory_usage((solvers.solve, (hardSet[n],)), max_usage=True, retval=True)
        #mem += memory_usage((solvers.display, (norvig,)), max_usage=True)
        mem, norvig = memory_usage((solvers.solve, (hardSet[n],)), retval=True) #, max_usage=True, retval=True)
        mem = sum(mem)
        mem += sum(memory_usage((solvers.display, (norvig,))))#, max_usage=True)
        norvigTimes[n] = stop
        norvigMemory[n] = mem

    ### PRINT TIMES
    print("---- TIME TO COMPLETE HARD ----")
    funcs.printResults(backtrackTimes, lhlTimes, saTimes, norvigTimes, backtrackMemory, lhlMem, saMemory, norvigMemory)
    funcs.writeResults(backtrackTimes, lhlTimes, saTimes, norvigTimes, backtrackMemory, lhlMem, saMemory, norvigMemory, "ResultsHard.txt")
    funcs.plotCases(backtrackTimes, lhlTimes, saTimes, norvigTimes, "Hard")
    funcs.plotMemory(backtrackMemory, lhlMem, saMemory, norvigMemory, "Hard")

from boards import expertBackTrack, expertLHL, expertSet
def compareExpert():
    ### BACKTRACK TIMING
    backtrackTimes = {}
    backtrackMemory = {}
    b = Backtrack()
    caseNames = expertBackTrack.keys()
    for n in caseNames:
        start = time.time()
        b.setBoard(expertBackTrack[n])
        b.solve()
        stop = time.time() - start
        #mem = memory_usage((b.setBoard, (expertBackTrack[n],)), max_usage=True)
        #mem += memory_usage((b.solve, ), max_usage=True)
        mem = sum(memory_usage((b.setBoard, (expertBackTrack[n],))))#, max_usage=True)
        mem += sum(memory_usage((b.solve, )))#, max_usage=True))
        backtrackTimes[n] = stop
        backtrackMemory[n] = mem
        print()
    print()

    ###  LHL TIMING
    lhlTimes = {}
    lhlMem = {}
    lee = LHL()
    caseNames = expertLHL.keys()
    for n in caseNames:
        start = time.time()
        lee.solveSudoku(expertLHL[n])
        stop = time.time() - start
        #mem = memory_usage((lee.solveSudoku, (expertLHL[n],)), max_usage=True)
        mem = sum(memory_usage((lee.solveSudoku, (expertLHL[n],)))) #, max_usage=True)
        #mem += sum(mem)
        lhlTimes[n] = stop
        lhlMem[n] = mem
    print()
    
    ### SIMULATED ANNEALING
    saTimes = {}
    saMemory = {}
    caseNames = expertSet.keys()
    for n in caseNames:
        start = time.time()
        simAn = solvers.solve_simulated_annealing(expertSet[n])
        solvers.display(simAn)
        stop = time.time() - start
        #mem, simAn = memory_usage((solvers.solve_simulated_annealing, (expertSet[n],)), max_usage=True, retval=True)
        #mem += memory_usage((solvers.display, (simAn,)), max_usage=True)
        mem, simAn = memory_usage((solvers.solve_simulated_annealing, (expertSet[n],)), retval=True) #, max_usage=True, retval=True)
        mem = sum(mem)
        mem += sum(memory_usage((solvers.display, (simAn,))))#, max_usage=True)
        saTimes[n] = stop
        saMemory[n] = mem

    ### Norvig CSP
    norvigTimes = {}
    norvigMemory = {}
    for n in caseNames:
        start = time.time()
        norvig = solvers.solve(expertSet[n])
        solvers.display(norvig)
        stop = time.time() - start
        #mem, norvig = memory_usage((solvers.solve, (expertSet[n],)), max_usage=True, retval=True)
        #mem += memory_usage((solvers.display, (norvig,)), max_usage=True)
        mem, norvig = memory_usage((solvers.solve, (expertSet[n],)), retval=True) #, max_usage=True, retval=True)
        mem = sum(mem)
        mem += sum(memory_usage((solvers.display, (norvig,))))#, max_usage=True)
        norvigTimes[n] = stop
        norvigMemory[n] = mem

    ### PRINT TIMES
    print("---- TIME TO COMPLETE expert ----")
    funcs.printResults(backtrackTimes, lhlTimes, saTimes, norvigTimes, backtrackMemory, lhlMem, saMemory, norvigMemory)
    funcs.writeResults(backtrackTimes, lhlTimes, saTimes, norvigTimes, backtrackMemory, lhlMem, saMemory, norvigMemory, "ResultsExpert.txt")
    funcs.plotCases(backtrackTimes, lhlTimes, saTimes, norvigTimes, "Expert")
    funcs.plotMemory(backtrackMemory, lhlMem, saMemory, norvigMemory, "Expert")


#compareEasy()
#compareMed()
#compareHard()
#compareExpert()


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
# https://github.com/MaximeDaigle/sudoku

# -- CSP code
# https://norvig.com/sudoku.html
# https://gist.github.com/ksurya/3940679
# https://github.com/MaximeDaigle/sudoku 

#  -- Genetic algorithm code
# https://github.com/chinyan/Genetic-Algorithm-based-Sudoku-Solver
