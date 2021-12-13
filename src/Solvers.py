# Author: Maxime Daigle
# Source Code: https://github.com/MaximeDaigle/sudoku


## Solve Every Sudoku Puzzle

## See http://norvig.com/sudoku.html for orignal

## Throughout this program we have:
##   r is a row,    e.g. 'A'
##   c is a column, e.g. '3'
##   s is a square, e.g. 'A3'
##   d is a digit,  e.g. '9'
##   u is a unit,   e.g. ['A1','B1','C1','D1','E1','F1','G1','H1','I1']
##   grid is a grid,e.g. 81 non-blank chars, e.g. starting with '.18...7...
##   values is a dict of possible values, e.g. {'A1':'12349', 'A2':'8', ...}

from random import randrange
import random
import math

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]

digits   = '123456789'
rows     = 'ABCDEFGHI'
cols     = digits
squares  = cross(rows, cols)
unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
units = dict((s, [u for u in unitlist if s in u])
             for s in squares)
peers = dict((s, set(sum(units[s],[]))-set([s]))
             for s in squares)

columns = [cross(rows, c) for c in cols]
lines = [cross(r, cols) for r in rows]
boxes = dict((s, set(sum([units[s][2]],[]))-set([s]))
             for s in squares)


try_counter = 0


################ Constraint Propagation ################

def assign(values, s, d):
    """Eliminate all the other values (except d) from values[s] and propagate.
    Return values, except return False if a contradiction is detected."""
    global try_counter
    try_counter += 1
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False

def eliminate(values, s, d):
    """Eliminate d from values[s]; propagate when values or places <= 2.
    Return values, except return False if a contradiction is detected."""
    if d not in values[s]:
        return values ## Already eliminated
    values[s] = values[s].replace(d,'')
    ## (1) If a square s is reduced to one value d2, then eliminate d2 from the peers.
    if len(values[s]) == 0:
        return False ## Contradiction: removed last value
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    ## (2) If a unit u is reduced to only one place for a value d, then put it there.
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False ## Contradiction: no place for this value
        elif len(dplaces) == 1:
            # d can only be in one place in unit; assign it there
            if not assign(values, dplaces[0], d):
                return False
    return values


############### Constraint propagation (in the boxes) for initialization of Hill Climbing ########################
def assign_HC(values, s, d):
    """Eliminate all the other values (except d) from values[s] and propagate in the box.
    Return values, except return False if a contradiction is detected in the box."""
    other_values = values[s].replace(d, '')
    if all(eliminate_HC(values, s, d2) for d2 in other_values):
        return values
    else:
        return False

def eliminate_HC(values, s, d):
    """Eliminate d from values[s]; propagate when values or places <= 2.
    Return values, except return False if a contradiction is detected."""
    if d not in values[s]:
        return values ## Already eliminated
    values[s] = values[s].replace(d,'')
    ## (1) If a square s is reduced to one value d2, then eliminate d2 from the box.
    if len(values[s]) == 0:
        return False ## Contradiction: removed last value
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate_HC(values, s2, d2) for s2 in boxes[s]):
            return False
    ## (2) If a unit u is reduced to only one place for a value d, then put it there.
    for u in [units[s][2]]:
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False ## Contradiction: no place for this value
        elif len(dplaces) == 1:
            # d can only be in one place in unit; assign it there
            if not assign_HC(values, dplaces[0], d):
                return False
    return values

def evaluation(values):
    # l'evaluation est egal a: 0 - nb de conflit sur les lignes et colonnes
    conflicts = 0
    for line in lines:
        l = []
        for s in line:
            l.append(values[s])
        conflicts += len(set(l)) - 9
    for column in columns:
        c = []
        for s in column:
            c.append(values[s])
        conflicts += len(set(c)) - 9
    return conflicts

############### Simulated annealing ##############

def initialize_hill_climbing(values):
    "En tenant compte seulement des boites, remplit chaque carre, avec au hasard, un des chiffre possibles"
    new_values = values.copy()
    #tant quil y a un carre vide
    while max(len(new_values[s]) for s in squares) > 1:
        ## Chose the unfilled square s with the fewest possibilities
        n, s = min((len(new_values[s]), s) for s in squares if len(new_values[s]) > 1)
        random_index = randrange(0, len(new_values[s]))
        d = new_values[s][random_index]
        assign_HC(new_values, s, d)
    return new_values

def solve_simulated_annealing(grid):
    #met le compteur a zero a chaque nouvelle grille de sudoku
    global try_counter
    try_counter = 0
    values = parse_grid(grid)
    return simulated_annealing(initialize_hill_climbing(values))

def simulated_annealing(values):
    global try_counter
    current = values
    t = 1
    alpha = 0.99
    for i in range(10000):
        t = alpha * t
        if t == 0:
            return current
        if solved(current):
            return current
        nxt = random_neighbor(current)
        deltaE = evaluation(nxt) - evaluation(current)
        if deltaE > 0:
            current = nxt
            try_counter += 1
        elif jump(probability=math.exp(deltaE / t)):
            current = nxt
            try_counter += 1
    return values #return current values if not solved after trying 10k neighbors

def random_neighbor(current):
    newNode = current.copy()
    s = random.choice(squares)
    s2 = random.sample(boxes[s],1)[0]
    newNode[s], newNode[s2] = newNode[s2], newNode[s]
    return newNode

def jump(probability):
    return random.random() < probability

################ Parse a Grid ################

def parse_grid(grid):
    """Convert grid to a dict of possible values, {square: digits}, or
    return False if a contradiction is detected."""
    ## To start, every square can be any digit; then assign values from the grid.
    values = dict((s, digits) for s in squares)
    for s,d in grid_values(grid).items():
        if d in digits and not assign(values, s, d):
            return False ## (Fail if we can't assign d to square s.)
    return values

def grid_values(grid):
    "Convert grid into a dict of {square: char} with '0' or '.' for empties."
    chars = [c for c in grid if c in digits or c in '0.']
    assert len(chars) == 81
    return dict(zip(squares, chars))


def solved(values):
    "A puzzle is solved if each unit is a permutation of the digits 1 to 9."
    def unitsolved(unit): return set(values[s] for s in unit) == set(digits)
    return values is not False and all(unitsolved(unit) for unit in unitlist)

################ Display as 2-D grid ################

def display(values):
    "Display these values as a 2-D grid."
    width = 1+max(len(values[s]) for s in squares)
    #print("WIDTH: " + str(width))
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r + c].center(width) + ('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    print()

################ Search ################

def solve(grid):
    #met le compteur a zero a chaque nouvelle grille de sudoku
    global try_counter
    try_counter = 0
    return search(parse_grid(grid))

def search(values):
    "Using depth-first search and propagation, try all possible values."
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in squares):
        return values ## Solved!
    ## Chose the unfilled square s with the fewest possibilities
    n,s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d))
                for d in values[s])

################ Utilities ################

def some(seq):
    "Return some element of seq that is true."
    for e in seq:
        if e: return e
    return False

# def from_file(filename, sep='\n'):
#     "Parse a file into a list of strings, separated by sep."
#     return file(filename).read().strip().split(sep)

#solution_norvig = solve(grid2)
#print(solved(solution_norvig))
#print(try_counter)
#display(solution_norvig)
#solve_all(from_file("100sudoku.txt"), "Norvig", None)