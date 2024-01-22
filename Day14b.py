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
    if 'O.' not in pre: return pre
    rocks = pre.count('O')
    return '.' * (len(pre) - rocks) + ('O' * rocks)

start_time = time.time()
tbl = [row.strip('\n') for row in open('Day14-demo.txt', 'r')]

#SPIN CYCLE
cycles = 1000000
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
        for r, col in enumerate(tbl):
            pre = ''.join(col[::-1])
            if 'O.' not in pre: continue
            col = ''
            for runway in pre.split('#'):
                col += roll(runway) + '#'
            col = col[:-1]
            tbl[r] = col[::-1]

    #SOUTH, EAST
    for j in range(2):
        tbl = [list(i) for i in zip(*tbl)]  #transpose
        for r, col in enumerate(tbl):
            pre = ''.join(col)
            if 'O.' not in pre: continue
            col = ''
            for runway in pre.split('#'):
                col += roll(runway) + '#'
            tbl[r] = col[:-1]

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