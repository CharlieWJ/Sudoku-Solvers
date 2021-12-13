from boards import cases, tests, easyLHL, medLHL, hardLHL
from GA_Probs import easy, medium, hard, expert

def makeCaseNums(array):
    case = []
    for x in array:
        row = []
        for n in x:
            if n == ".":
                row.append(0)
            else:
                row.append(int(n))
        case.append(row)
    return case

def makeCaseStr(array):
    case = []
    for x in array:
        row = []
        for n in x:
            if x == 0:
                row.append(".")
            else:
                row.append(str(n))
        case.append(row)
    return case

def makeCase1D(array):
    case = []
    for x in array:
        for n in x:
            case.append(n)
    return case

def makeCaseLHLfromGA(string):
    case = []
    row = []
    for i in range(len(string)):
        if len(row) == 9:
            case.append(row)
            row = []
        if string[i] == "0":
            row.append(".")
        else:
            row.append(string[i])
    case.append(row)
    return case


#print(makeCaseNums(cases["case1"]))
#print(makeCase1D(tests['test1']))
#print(makeCase1D(tests['case2']))
"""
keys = hard.keys()
x = 1
for k in keys:
    print('"hard' + str(x) + '" : [')
    case = makeCaseLHLfromGA(hard[k])
    for r in case:
        print(str(r) + ",")
    print("],")
    x += 1
    print()
"""

keys = easyLHL.keys()
x = 1
for k in keys:
    print('"easy' + str(x) + '" : [')
    case = makeCaseNums(easyLHL[k])
    for r in case:
        print(str(r) + ",")
    print("],")
    x += 1
    print()

keys = medLHL.keys()
x = 1
for k in keys:
    print('"med' + str(x) + '" : [')
    case = makeCaseNums(medLHL[k])
    for r in case:
        print(str(r) + ",")
    print("],")
    x += 1
    print()

keys = hardLHL.keys()
x = 1
for k in keys:
    print('"hard' + str(x) + '" : [')
    case = makeCaseNums(hardLHL[k])
    for r in case:
        print(str(r) + ",")
    print("],")
    x += 1
    print()
