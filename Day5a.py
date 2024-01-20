import sys
import os
import time
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()
file1 = open('Day5-input.txt', 'r')
Lines = file1.readlines()

seeds = {}
#map = {'soil':[], 'fert':[], 'water':[], 'light':[], 'temp':[], 'hum':[], 'loc':[]}
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

#get seeds
line = Lines[0][6:].strip()
line = line.split()
for n in line:
    seeds[n] = int(n)

#get map
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


for s in seeds:
    print("mapping " + s + "...")
    for mkey in map:
        shift = 0
        for l in map[mkey]:
            if l.sorc <= seeds[s] < (l.sorc + l.rng):
                seeds[s] += l.dest - l.sorc
                break
        print(mkey, seeds[s])
    print("")

print(min(seeds.values()))
print('Time taken:', time.time() - start_time)