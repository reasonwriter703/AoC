import sys
import os
import time
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()

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
    tbl = [list(i) for i in zip(*tbl)]  #transpose
    for i, row in enumerate(tbl):
        if sum(1 for j in row if j == "#") == 0:
            row[:] = [r.replace(".", "_") for r in row]
# for i in tbl:
#     print("".join(i))

P = []
for y, row in enumerate(tbl):
    for x, col in enumerate(row):
        if col == "#":
            P.append(planet(len(P) + 1, x,y))
            row[x] = len(P)

allsteps = 0
Q = P.copy()
for p in P:
    del Q[0]
    for q in Q:
        steps = 0
        expansion = 1000000
        ymin = min(q.y, p.y)
        xmin = min(q.x, p.x)
        ymax = max(q.y, p.y)
        xmax = max(q.x, p.x)
        for i in range(ymax - ymin):
            steps += expansion if tbl[ymax - i][xmax] == "_" else 1
            print(str(p.i) + '-' + str(q.i), q.y - i, p.x, tbl[q.y - i][p.x - 1], sep='\t')
        
        for i in range(xmax - xmin):
            steps += expansion if tbl[ymax][xmax - i] == "_" else 1
            print(str(p.i) + '-' + str(q.i), p.y - i, q.x, tbl[p.y - i][q.x - 1], sep='\t')
        
        print(str(p.i) + '-' + str(q.i), steps, sep='\t')
        allsteps += steps
print(allsteps)
print('Time taken:', time.time() - start_time)