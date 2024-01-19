class planet:
    def __init__(g, i, x, y):
        g.i = i
        g.x = x
        g.y = y

file1 = open('Day11-input.txt', 'r')
Lines = file1.readlines()
Lines[:] = [line.strip() for line in Lines]
tbl = [list(i) for i in Lines]

#apply cosmic expansion
for k in range(2):
    ins = []
    tbl = [list(i) for i in zip(*tbl)]  #transpose
    for i, row in enumerate(tbl):
        if sum(1 for j in row if j == "#") == 0:
            ins.insert(0, i)
    for i in ins:
        tbl.insert(i, tbl[i])

P = []
for y, row in enumerate(tbl):
    for x, col in enumerate(row):
        if col == "#":
            P.append(planet(len(P) + 1, x,y))
            row[x] = len(P)

allsteps = 0
steps = 0
Q = P.copy()
for p in P:
    del Q[0]
    for q in Q:
        steps = abs(q.x - p.x) + abs(q.y - p.y)
        allsteps += steps
        print(str(p.i) + '-' + str(q.i), steps, sep='\t')
print(allsteps)
