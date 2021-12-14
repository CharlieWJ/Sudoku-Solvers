import time
import funcs
import GA as ga
from GA_Probs import easyGA, mediumGA, hardGA, expertGA
import numpy as np
from memory_profiler import memory_usage


def geneticEasy():
    caseNames = easyGA.keys()
    gaTimes = {}
    gaMemory = {}
    genetic = ga.Sudoku()

    for n in caseNames:
        start = time.time()
        grid = np.array(list(easyGA[n])).reshape((9,9)).astype(int)
        genetic.load(grid)
        generation, solution = genetic.solve()
        print(solution.values)
        stop = time.time() - start
        mem = sum(memory_usage((genetic.load, (grid,))))#, max_usage=True)
        mem += sum(memory_usage((genetic.solve, )))#, max_usage=True, retval=True)
        gaTimes[n] = stop
        gaMemory[n] = mem
    funcs.writeGAResults(gaTimes, gaMemory, "GeneticResEasy.txt")


def geneticMed():
    caseNames = mediumGA.keys()
    gaTimes = {}
    gaMemory = {}
    genetic = ga.Sudoku()

    for n in caseNames:
        start = time.time()
        grid = np.array(list(mediumGA[n])).reshape((9,9)).astype(int)
        genetic.load(grid)
        generation, solution = genetic.solve()
        print(solution.values)
        stop = time.time() - start
        mem = sum(memory_usage((genetic.load, (grid,))))#, max_usage=True)
        mem += sum(memory_usage((genetic.solve, )))#, max_usage=True, retval=True)
        gaTimes[n] = stop
        gaMemory[n] = mem
    funcs.writeGAResults(gaTimes, gaMemory, "GeneticResMed.txt")

def geneticHard():
    caseNames = hardGA.keys()
    gaTimes = {}
    gaMemory = {}
    genetic = ga.Sudoku()

    for n in caseNames:
        start = time.time()
        grid = np.array(list(hardGA[n])).reshape((9,9)).astype(int)
        genetic.load(grid)
        generation, solution = genetic.solve()
        print(solution.values)
        stop = time.time() - start
        mem = sum(memory_usage((genetic.load, (grid,))))#, max_usage=True)
        mem += sum(memory_usage((genetic.solve, )))#, max_usage=True, retval=True)
        gaTimes[n] = stop
        gaMemory[n] = mem
    funcs.writeGAResults(gaTimes, gaMemory, "GeneticResHard.txt")

def geneticExpert():
    caseNames = expertGA.keys()
    gaTimes = {}
    gaMemory = {}
    genetic = ga.Sudoku()

    for n in caseNames:
        start = time.time()
        grid = np.array(list(expertGA[n])).reshape((9,9)).astype(int)
        genetic.load(grid)
        generation, solution = genetic.solve()
        print(solution.values)
        stop = time.time() - start
        mem = sum(memory_usage((genetic.load, (grid,))))#, max_usage=True)
        mem += sum(memory_usage((genetic.solve, )))#, max_usage=True, retval=True)
        gaTimes[n] = stop
        gaMemory[n] = mem
    funcs.writeGAResults(gaTimes, gaMemory, "GeneticResExpert.txt")


#geneticEasy()
#geneticMed()
#geneticHard()
#geneticExpert()