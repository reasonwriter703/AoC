import sys
import os
import time
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()
from functools import lru_cache

@lru_cache(maxsize=None)
def roll(row):
    if 'O.' not in row: return row
    rocks = row.count('O')
    return '.' * (len(row) - rocks) + ('O' * rocks)

@lru_cache(maxsize=None)
def tilt(col):
    if 'O.' not in col: return col
    new = ''
    for runway in col.split('#'):
        new += roll(runway) + '#'
    return new[:-1]

start_time = time.time()
tbl = [row.strip('\n') for row in open('Day14-input.txt', 'r')]
total = 0
states = {}

cycles = 1000000000
modu = None
for c in range(cycles):
    if modu == None:
        snapshot = hash(';'.join([i for i in tbl]))
        if snapshot not in states:
            states[snapshot] = c
        else: #found first repeated state. run cycles until modulo hits 0
            modu = (cycles - states[snapshot]) % (c - states[snapshot])
    else:
        modu -= 1
    if modu == 0: break
    
    #NORTH, WEST, SOUTH, EAST
    for j in range(4):
        tbl = [''.join(i[::-1]) for i in zip(*tbl)]  #rotate (transpose & invert)
        for r, col in enumerate(tbl):
            tbl[r] = tilt(col)
print('')
# for v in states.values():
#     print(v)

for rownum, col in enumerate(reversed(tbl)):
    total += col.count('O') * (rownum + 1)

print(total)
print('Time taken:', time.time() - start_time)