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

def plotCases(backtrackTimes, lhlTimes, saTimes, norvigTimes, difficulty):
    plt.clf()
    names = ['1','2','3','4','5','6','7','8','9','10']
    bVals, lhlVals = list(backtrackTimes.values()), list(lhlTimes.values())
    saVals, norvigVals = list(saTimes.values()), list(norvigTimes.values())
    avgTime = [(average(backtrackTimes) + average(lhlTimes) + average(saTimes) + average(norvigTimes))/4]*10
    plt.plot(names, avgTime, 'k', label="Average")
    plt.plot(names, bVals, '--bo', label="Backtrack")
    plt.plot(names, lhlVals, '--x', color='orange', label="LHL")
    plt.plot(names, saVals, '-g^', label="Simulated Annealing")
    plt.plot(names, norvigVals, '--rH', label="CSP")
    plt.legend()
    
    #x = [1,2,3,4,5,6,7,8,9,10]
    #plt.xticks(np.arange(min(x), max(x), 1.0))
    plt.ylabel("Time (s)")
    plt.xlabel(str(difficulty) + " Test Cases")
    plt.savefig('./Plots/'+str(difficulty)+'Times.png')
    #plt.show()

def plotMemory(backtrackMemory, lhlMem, saMemory, norvigMemory, difficulty):
    plt.clf()
    names = ['1','2','3','4','5','6','7','8','9','10']
    bVals, lhlVals = list(backtrackMemory.values()), list(lhlMem.values())
    saVals, norvigVals = list(saMemory.values()), list(norvigMemory.values())
    avgTime = [(average(backtrackMemory) + average(lhlMem) + average(saMemory) + average(norvigMemory))/4]*10
    plt.plot(names, avgTime, 'k', label="Average")
    plt.plot(names, bVals, '--bo', label="Backtrack")
    plt.plot(names, lhlVals, '--x', color='orange', label="LHL")
    plt.plot(names, saVals, '-g^', label="Simulated Annealing")
    plt.plot(names, norvigVals, '--rH', label="CSP")

    plt.legend()
    
    #x = [1,2,3,4,5,6,7,8,9,10]
    #plt.xticks(np.arange(min(x), max(x), 1.0))
    plt.ylabel("Memory (MiB)")
    plt.xlabel(str(difficulty) + " Test Cases")
    plt.savefig('./Plots/'+str(difficulty)+'Memory.png')
    #plt.show()   plt.show()


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


"""
The values below were taken from the GeneticResEasy and GeneticResMed txt files,
which were obtained from the latest run of GA_Usage.py.
Note, that any subsiquent runs of GA_Usage.py or final-project.py will result in different values,
thus, not making the graphs produed in the function below 
consistent with the latest results (only by a very minor margin).
This is an easy fix and may be resolved in a future update.
"""
gaEasyTimes = {'Easy1': 14.909852743148804, 'Easy2': 20.13157081604004, 
'Easy3': 9.558997631072998, 'Easy4': 5.218157052993774,
'Easy5': 8.034236907958984, 'Easy6': 5.641728162765503,
'Easy7': 22.846338987350464, 'Easy8': 14.405819177627563,
'Easy9': 6.870084047317505, 'Easy10': 17.181368112564087}

gaEasyMem = {'Easy1': 4744.70703125, 'Easy2': 12397.203125,
'Easy3': 4354.58984375, 'Easy4': 4047.515625,
'Easy5': 4713.5625, 'Easy6': 6660.46875,
'Easy7': 10250.01953125, 'Easy8': 6817.2890625,
'Easy9': 3536.7890625, 'Easy10': 8868.27734375}

gaEasyAVG_T = 12.479815363883972
gaEasyAVG_M = 6639.0421875


gaMedTimes = {'med1': 94.94164800643921, 'med2': 82.5857081413269,
'med3': 74.2910430431366,'med4': 157.1837031841278,
'med5': 98.8330659866333, 'med6': 43.543466329574585,
'med7': 59.52175188064575, 'med8': 50.27414393424988,
'med9': 26.307454347610474, 'med10': 76.36888694763184}

gaMedMem = {'med1': 72277.375, 'med2': 33674.04296875,
'med3': 54837.6640625, 'med4': 50928.00390625,
'med5': 70855.57421875, 'med6': 27952.28515625,
'med7': 36035.5625, 'med8': 18614.96875,
'med9': 19233.40625, 'med10': 49695.53125}

gaMedAVG_T = 76.38508718013763
gaMedAVG_M = 43410.44140625
def plotGA():
    plt.clf()
    names = ['1','2','3','4','5','6','7','8','9','10']
    gaT, gaM = list(gaEasyTimes.values()), list(gaEasyMem.values())
    ## Average times for the Easy runs
    timeSum = 0.004820442199707032 + 0.00530695915222168 + 0.004529285430908203 + 0.004145002365112305
    avgTime = [timeSum / 4]*10
    timeSum += gaEasyAVG_T
    avgTimeGA = [timeSum / 5]*10
    plt.plot(names, avgTime, 'k', label="Average (GA Excluded)")
    plt.plot(names, avgTimeGA, ':c', label="Average (All)")
    plt.plot(names, gaT, '--mx', label="Genetic Algorithm")
    
    plt.ylabel("Time (s)")
    plt.xlabel("Easy Test Cases")
    plt.legend()
    plt.savefig('./Plots/GAEasyTime.png')

    ## Medium time runs
    plt.clf()
    gaT = list(gaMedTimes.values())
    ## Average times for Medium runs
    timeSum = 0.1041818380355835 + 0.03308241367340088 + 0.00426483154296875 + 0.00492703914642334
    avgTime = [timeSum / 4]*10
    timeSum += gaMedAVG_T
    avgTimeGA = [timeSum / 5]*10
    plt.plot(names, avgTime, 'k', label="Average (GA Excluded)")
    plt.plot(names, avgTimeGA, ':c', label="Average (All)")
    plt.plot(names, gaT, '--mx', label="Genetic Algorithm")
    
    plt.ylabel("Time (s)")
    plt.xlabel("Medium Test Cases")
    plt.legend()
    plt.savefig('./Plots/GAMediumTime.png')

    ## Easy memory runs
    plt.clf()
    ## Average memory usage for the Easy runs
    memSum = 601.284765625 + 196.2046875 + 569.64609375 + 569.680078125
    avgMem = memSum / 4
    memSum += gaEasyAVG_M
    avgMemGA = memSum / 5
    #memData = {'Genetic Algorithm':gaEasyAVG_M, 'Average (All)':avgMemGA, 'Average (GA Excluded)':avgMem}
    xAxis = ['Genetic Algorithm', 'Average (All)', 'Average (GA Excluded)']
    yAxis = [gaEasyAVG_M, avgMemGA, avgMem]
    plt.bar(xAxis, yAxis, color ='c', width = 0.5)
    
    plt.ylabel("Memory (MiB)")
    plt.xlabel("Easy Test Cases")
    plt.savefig('./Plots/GAEasyMemory.png')
    plt.clf()
    
    ## Medium memory runs
    ## Average memory usage for Medium runs
    memSum = 1040.0703125 + 196.39453125 + 530.925 + 616.290625
    avgMem = memSum / 4
    memSum += gaEasyAVG_M
    avgMemGA = memSum / 5
    #memData = {'Genetic Algorithm':gaEasyAVG_M, 'Average (All)':avgMemGA, 'Average (GA Excluded)':avgMem}
    #xAxis = ['Genetic Algorithm', 'Average (All)', 'Average (GA Excluded)']
    yAxis = [gaMedAVG_M, avgMemGA, avgMem]
    plt.bar(xAxis, yAxis, color ='c', width = 0.5)
    
    plt.ylabel("Memory (MiB)")
    plt.xlabel("Medium Test Cases")
    plt.savefig('./Plots/GAMediumMemory.png')

plotGA()