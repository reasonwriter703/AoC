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

@lru_cache(maxsize=None)
def tilt(col):
    if 'O.' not in col: return col
    new = ''
    for runway in col.split('#'):
        new += roll(runway) + '#'
    return new[:-1]

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

    #NORTH, WEST, SOUTH, EAST
    for j in range(4):
        tbl = [list(i[::-1]) for i in zip(*tbl)]  #rotate (transpose & invert)
        for r, col in enumerate(tbl):
            tbl[r] = tilt(''.join(col))

total = 0
for val, col in enumerate(reversed(tbl)):
    total += col.count('O') * (val + 1)

print(total)
print('Time taken:', time.time() - start_time)