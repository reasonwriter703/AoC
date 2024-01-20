import sys
import os
import time
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()

file1 = open('Day14-demo.txt', 'r')
Lines = file1.readlines()
Lines[:] = [line.strip() for line in Lines]

tbl = []
for r in range(len(Lines[0])):
    col = []
    for c in range(len(Lines)):
        col.append(Lines[c][r:r+1])
    tbl.append(col)

for col in tbl:
    stop = 0
    for i in range(len(col)):
        if col[i] == "O":
            col.insert(stop, col.pop(i))
        elif col[i] == "#":
            stop = i + 1

for col in tbl:
    print(col)
print("")
tbl = [list(i) for i in zip(*tbl)]
for col in tbl:
    print(col)

total = 0
for col in tbl:
    load = 0
    for c in col[::-1]:
        load += 1
        if c == "O":
            total += load

print(total)
print('Time taken:', time.time() - start_time)