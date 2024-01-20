import numpy as np
import sys
import os
import time
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()

file1 = open('Day5-input.txt', 'r')
Lines = file1.readlines()

map = {}
#A - seeds
#B - soil
#C - fertilizer
#D - water
#E - light
#F - temperature
#G - humidity
#H - location

class coord:
    def __init__(g, dest, sorc, rng):
        g.dest = dest
        g.sorc = sorc
        g.rng = rng

#get maps
for line in Lines[1:]:
    if line == "\n": continue
    mkey = line.find('-to-')
    if mkey != -1:
        mmkey = line[:1] + '2' + line[mkey+4:mkey+5]
        map[mmkey] = []
    else:
        line = line.strip()
        line = line.split()
        map[mmkey].append(coord(int(line[0]), int(line[1]), int(line[2])))


#get seeds
seeds = []
#seeds.append(np.arange(79, 79+14))
#seeds.append(np.arange(55, 55+13))

seeds.append(np.arange(348350443, 410212616))
seeds.append(np.arange(514585599, 520687690))
seeds.append(np.arange(626861593, 765648080))
seeds.append(np.arange(825403564, 1303406955))
seeds.append(np.arange(1450194064, 1477976316))
seeds.append(np.arange(1972667147, 2378259165))
seeds.append(np.arange(2526020300, 2541511753))
seeds.append(np.arange(2886966111, 3162265119))
seeds.append(np.arange(3211013652, 3757205391))
seeds.append(np.arange(3911195009, 4092364215))

minseed = -1
for i, arr in enumerate(seeds):
    for mkey in map:
        for l in map[mkey]:
            arr = np.where(np.logical_and(l.sorc <= arr, arr < (l.sorc + l.rng)), -(arr + (l.dest - l.sorc)), arr)
        arr = np.abs(arr)
    mins = np.min(arr)
    if minseed == -1 or mins < minseed:
        minseed = mins
    print("min of seeds[" + str(i) + "]: ", mins)
print("min: ", minseed)
print('Time taken:', time.time() - start_time)