import sys
import os
import time
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()

file1 = open('Day14-input.txt', 'r')
Lines = file1.readlines()
Lines[:] = [line.strip() for line in Lines]
tbl = [list(i) for i in Lines]

"""
for i in range(len(tbl)):
    stop = 0
    for j in range(len(tbl)):
        print(tbl[i][j])
"""

#SPIN CYCLE
printcounter = 0
for c in range(1000000000):
    if (printcounter == 1000000):
        print(str(c/10000000) + "%...")
        printcounter = 0
    printcounter += 1

    #NORTH, WEST
    for j in range(2):
        tbl = [list(i) for i in zip(*tbl)]  #transpose
        for col in tbl:
            stop = 0
            for k in range(len(col)):
                if col[k] == "O":
                    col.insert(stop, col.pop(k))
                elif col[k] == "#":
                    stop = k + 1

    #SOUTH, EAST
    for j in range(2):
        tbl = [list(i) for i in zip(*tbl)]  #transpose
        for col in tbl:
            stop = len(col)
            for k in reversed(range(len(col))):
                if col[k] == "O":
                    col.insert(stop, col.pop(k))
                elif col[k] == "#":
                    stop = k - 1


total = 0
for col in tbl:
    print("".join(col))
    load = 0
    for c in col[::-1]:
        load += 1
        if c == "O":
            total += load

print(total)
print('Time taken:', time.time() - start_time)