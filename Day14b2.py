import sys
import os
import time
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()
from functools import lru_cache

@lru_cache(maxsize=None)
def roll(pre):
    if pre == '':
        return post
    
    stop = pre.find('#')
    if stop == -1:
        roll(pre)
    else:
        roll(pre[stop:])

start_time = time.time()
tbl = []
for i, row in enumerate(open('Day14-demo.txt', 'r')):
    col = []
    for c in row.strip('\n'):
        col.append(c)
    tbl.append(col)
    print(''.join(col))
print('')

#SPIN CYCLE
cycles = 3
printcycles = int(cycles / 100)
printcounter = 0
for c in range(cycles):
    if (printcounter == printcycles):
        try:
            print(str(c/printcycles) + '%...')
        except:
            pass
        printcounter = 0
    printcounter += 1

    #NORTH, WEST
    for j in range(2):
        tbl = [list(i) for i in zip(*tbl)]  #transpose
#        newtbl = []
        for col in tbl:
            if 'O' not in col: continue
            col = roll(''.join(col))    #col[::-1]

            # stop = 0
            # for k in range(len(col)):
            #     if col[k] == 'O':
            #         col.insert(stop, col.pop(k))
            #     elif col[k] == '#':
            #         stop = k + 1

    #SOUTH, EAST
    for j in range(2):
        tbl = [list(i) for i in zip(*tbl)]  #transpose
        for col in tbl:
            stop = len(col)
            for k in reversed(range(len(col))):
                if col[k] == 'O':
                    col.insert(stop, col.pop(k))
                elif col[k] == '#':
                    stop = k - 1

total = 0
for col in tbl:
    print(''.join(col))
    load = 0
    for c in col[::-1]:
        load += 1
        if c == 'O':
            total += load

print(total)
print('Time taken:', time.time() - start_time)
