from boards import cases, tests

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

print(makeCaseNums(cases["case1"]))