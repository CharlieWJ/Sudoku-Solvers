import matplotlib.pyplot as plt
import numpy as np

btime = "Backtrack Times:\n"
btimeMean = "Backtracking Avg. Time:\n"
lhlStr = "LHL Times:\n"
lhltimeMean = "LHL Avg. Time:\n"
saStr = "Simulated Annealing Times:\n"
satimeMean = "Simulated Annealing Avg. Time:\n"
cspStr = "Norvig CSP Times:\n"
csptimeMean = "Norvig CSP Avg. Time:\n"
gaStr = "Genetic Algorithm Times:\n"
gaTimeMean = "Genetic Algorithm Avg. Time:\n"
line = "----------"

bmem = "Backtrack Memory:\n"
bmemMean = "Backtracking Avg. Memory:\n"
lhlmemStr = "LHL Memory:\n"
lhlmemMean = "LHL Avg. Memory:\n"
samemStr = "Simulated Annealing Memory:\n"
samemMean = "Simulated Annealing Avg. Memory:\n"
cspmemStr = "Norvig CSP Memory:\n"
cspmemMean = "Norvig CSP Avg. Memory:\n"
gamemStr = "Genetic Algorithm Memory:\n"
gamemMean = "Genetic Algorithm Avg. Memory:\n"
memUse = "---- MEMORY USAGE ----"
avgTimeStr = "---- AVERAGE TIMES ----"
avgMemStr = "---- AVERAGE MEMORY USAGE ----"


def average(dct):
    vals = dct.values()
    mean = sum(vals)/len(vals)
    return mean

def plotCases(backtrackTimes, lhlTimes, saTimes, norvigTimes, backtrackMemory, lhlMem, saMemory, norvigMemory, difficulty):
    bVals, lhlVals, saVals, norvigVals = backtrackTimes.values(), lhlTimes.values(), saTimes.values(), norvigTimes.values()
    plt.plot(bVals, label="Backtrack")
    plt.plot(lhlVals, label="LHL")
    plt.plot(saVals, label="Simulated Annealing")
    plt.plot(norvigVals, label="CSP")
    plt.legend()

    plt.ylabel("Time (s)")
    plt.xlabel(str(difficulty) + " Test Cases")
    plt.show()
    plt.savefig('/Plots/'+str(difficulty)+'Cases.png')

def plotMemory():
    plt.show()


def printResults(backtrackTimes, lhlTimes, saTimes, norvigTimes, backtrackMemory, lhlMem, saMemory, norvigMemory):
    ### PRINT TIMES
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

def writeResults(backtrackTimes, lhlTimes, saTimes, norvigTimes, backtrackMemory, lhlMem, saMemory, norvigMemory, fname):
    f = open(fname, "w")
    f.write("---- TIME TO COMPLETE ----\n")
    f.write(btime + str(backtrackTimes) + "\n")
    f.write(line + "\n")
    f.write(lhlStr + str(lhlTimes) + "\n")
    f.write(line + "\n")
    f.write(saStr + str(saTimes) + "\n")
    f.write(line + "\n")
    f.write(cspStr + str(norvigTimes) + "\n")
    f.write(line + "\n")
    #print("Genetic Algorithm Times:\n" + str(gaTimes))
    ### PRINT MEMORY
    f.write(memUse + "\n")
    f.write(bmem + str(backtrackMemory) + "\n")
    f.write(line + "\n")
    f.write(lhlmemStr + str(lhlMem) + "\n")
    f.write(line + "\n")
    f.write(samemStr + str(saMemory) + "\n")
    f.write(line + "\n")
    f.write(cspmemStr + str(norvigMemory) + "\n")
    f.write(line + "\n")
    ### AVERERAGE TIMES
    f.write(avgTimeStr + "\n")
    f.write(btimeMean + str(average(backtrackTimes)) + "\n")
    f.write(line + "\n")
    f.write(lhltimeMean + str(average(lhlTimes)) + "\n")
    f.write(line + "\n")
    f.write(satimeMean + str(average(saTimes)) + "\n")
    f.write(line + "\n")
    f.write(csptimeMean + str(average(norvigTimes)) + "\n")
    f.write(line + "\n")
    ### AVERAGE MEMORY
    f.write(avgMemStr + "\n")
    f.write(bmemMean + str(average(backtrackMemory)) + "\n")
    f.write(line + "\n")
    f.write(lhlmemMean + str(average(lhlMem)) + "\n")
    f.write(line + "\n")
    f.write(samemMean + str(average(saMemory)) + "\n")
    f.write(line + "\n")
    f.write(cspmemMean + str(average(norvigMemory)) + "\n")
    f.write(line + "\n")
    f.close()

def writeGAResults(gaTimes, gaMemory, fname):
    f = open(fname, "w")
    f.write("---- TIME TO COMPLETE ----")
    f.write(gaStr + str(gaTimes) + "\n")
    f.write(line + "\n")
    f.write(memUse + "\n")
    f.write(gamemStr + str(gaMemory) + "\n")
    f.write(line + "\n")
    f.write(avgTimeStr + "\n")
    f.write(gaTimeMean  + str(average(gaTimes)) + "\n")
    f.write(line + "\n")
    f.write(avgMemStr + "\n")
    f.write(gamemMean + str(average(gaMemory)) + "\n")
    f.write(line + "\n")
    f.close