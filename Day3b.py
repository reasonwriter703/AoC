import sys
import os
import time
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()

def key(x, y):
    return str(x) + "." + str(y)

file1 = open('Day3-input.txt', 'r')
Lines = file1.readlines()

tbl = {}
allNums = {}
allGears = {}
GearRatio = {}
y = 0
for line in Lines:
    nextNum = ""
    x = 0
    for i in line:
        if i != "\n":
            tbl[key(x,y)] = i

        #index all numbers by leftmost digit
        if i.isnumeric():
            nextNum = nextNum + i
        elif nextNum != "":
            allNums[key(x-len(nextNum),y)] = int(nextNum)
            nextNum = ""

        #index symbols
        #if not i.isnumeric() and i != ".":
        if i == "*":
            allGears[key(x,y)] = 0
            GearRatio[key(x,y)] = 1

        x += 1
    y += 1
print(allNums)

def tryget(x, y, val):
    r = tbl.get(key(x, y))
    if r is None:
        return ""
    else:
        if r == "*":
            allGears[key(x, y)] += 1
            GearRatio[key(x,y)] = GearRatio[key(x,y)] * val
        return r

partNums = []
for k in allNums:
    x = int(k[:k.find(".")])
    y = int(k[k.find(".")+1:])

    #for each digit, check surrounding area for symbol
    nearby = ""
    loop = len(str(allNums[k]))
    for i in range(loop):
        if i == 0:   #first - left column
            nearby += tryget(x - 1, y - 1, allNums[k])
            nearby += tryget(x - 1, y, allNums[k])
            nearby += tryget(x - 1, y + 1, allNums[k])
        if i == loop - 1:  #last - right column
            nearby += tryget(x + 1, y - 1, allNums[k])
            nearby += tryget(x + 1, y, allNums[k])
            nearby += tryget(x + 1, y + 1, allNums[k])

        nearby += tryget(x, y - 1, allNums[k])
        nearby += tryget(x, y + 1, allNums[k])
        x += 1

    nearby = nearby.replace(".","")
    print(k, allNums[k], nearby, sep='\t')


    if nearby != "":
        partNums.append(allNums[k])
#    else:
        #debug print
#        #if not ((loop == 3 and allNearby == "............") or (loop == 2 and allNearby == "..........")):
#            print(k, allNums[k], allNearby, sep='\t')
#            print("")

for g in allGears:
    if allGears[g] != 2:
        del GearRatio[g]

print(allGears)
print(GearRatio)
print(sum(GearRatio.values()))
print('Time taken:', time.time() - start_time)