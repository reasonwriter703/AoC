import sys
import os
import time
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()

def take_step(tbl, y, x):
    if tbl[y][x] != "_": return tbl[y][x]
    try:
        if tbl[y + 1][x] == "O":
            return "n"
    except IndexError:
        pass
    if y != 0 and tbl[y - 1][x] == "O":
        return "n"

    try:
        if tbl[y][x + 1] == "O":
            return "n"
    except IndexError:
        pass
    if x != 0 and tbl[y][x - 1] == "O":
        return "n"

    return tbl[y][x]
def fillmap(y, x, steps):
    tbl = [list(i) for i in Lines]  # reset matrix
    tbl[y][x] = "O"     #set new starting point

    for i in range(steps-1):
        for y, row in enumerate(tbl):
            if sum(1 for j in row if j == "O") == 0: continue
            for x, col in enumerate(row):
                tbl[y][x] = take_step(tbl, y, x)

        for row in tbl:
            row[:] = [r.replace("O", "_") for r in row]
            row[:] = [r.replace("n", "O") for r in row]
    #        print("".join(row))
    #    print("")
    count = getCount(tbl)
    print("+", count, "", steps, "steps")
    print("")
    return count
def getCount(tbl, section = ""):
    # count finishing positions
    count = 0
    for i, row in enumerate(tbl):
        if i == 2:
            print("...")
        elif i in {0, 1, maplen - 2, maplen - 1}:
            print("".join(row))
        count += sum(1 for j in row if j == "O")
    print("total:", plots, "", section + ": +", count)
    print("")
    return count

file1 = open('Day21-input.txt', 'r')
Lines = file1.readlines()
Lines[:] = [line.strip() for line in Lines]
Lines[:] = [line.replace(".", "_") for line in Lines]
tbl0 = [list(i) for i in Lines]  #create matrix
# find S
for rS, row in enumerate(tbl0):
    if "S" in row: break
for cS, col in enumerate(tbl0[rS]):
    if col == "S": break
tbl0 = [list(i) for i in Lines]
tbl0[rS][cS] = "_"
maplen = len(row)

StepsLeft = 26501365
isOdd = StepsLeft % 2 == 1
plots = 0

#build 7x7 grid
tbl1 = []
tbl7 = []
for row in tbl0:
    tbl1.append(row + row + row + row + row + row + row)
for k in range(7):
    for row in tbl1:
        tbl7.append(row.copy())

# go 3x the length of a map + modulo
tbl7[int(rS + maplen*3)][int(cS + maplen*3)] = "O"
for z in range((StepsLeft % maplen) + (maplen * 3)):     #
    for y, row in enumerate(tbl7):
        for x, col in enumerate(row):
            tbl7[y][x] = take_step(tbl7, y, x)

    for row in tbl7:
        row[:] = [r.replace("O", "_") for r in row]
        row[:] = [r.replace("n", "O") for r in row]
        #print("".join(row))

    StepsLeft -= 1
    if StepsLeft <= 0: break

map0 = getCount([row[maplen * 3:maplen * 4] for row in tbl7[maplen * 3:maplen * 4]], "CENTER")  # 7354
map1 = getCount([row[maplen * 2:maplen * 3] for row in tbl7[maplen * 3:maplen * 4]], "OFF-CENTER")  # 7362 (14,716 total)
this_ring = 0
n = 2
while StepsLeft >= maplen:
    # skip via centered square formula
    n += 1
    last_ring = this_ring
    this_ring =  n * n + ((n - 1) * (n - 1))
    plots += (map1 if n % 2 == isOdd else map0) * (this_ring - last_ring)
    StepsLeft -= maplen
#    print("steps left:", StepsLeft, "", "filled plots:", plots ,"n:", n, sep="\t")
n -= 2
print("n:", n)
plots += getCount(tbl7[:maplen*2], "TOP 2x7")
plots += getCount([row[:maplen * 3] for row in tbl7[maplen * 2:maplen * 3]], "NW") * n
plots += getCount([row[maplen * 4:maplen * 7] for row in tbl7[maplen * 2:maplen * 3]], "NE") * n
plots += getCount([row[:maplen*2] for row in tbl7[maplen*3:maplen*4]], "LEFT 2x1")
plots += getCount([row[maplen*5:maplen*7] for row in tbl7[maplen*3:maplen*4]], "RIGHT 2x1")
plots += getCount([row[:maplen * 3] for row in tbl7[maplen * 4:maplen * 5]], "SW") * n
plots += getCount([row[maplen * 4:maplen * 7] for row in tbl7[maplen * 4:maplen * 5]], "SE") * n
plots += getCount(tbl7[maplen*5:maplen*7], "BOTTOM 2x7")

print('Time taken:', time.time() - start_time)

# #count original 7x7
# for row in tbl7:
#     print("".join(row))
#     plots += sum(1 for j in row if j == "O")
# print("steps left:", StepsLeft, "", "filled plots:", plots, sep="\t")

# 602253595426282 is too low
# 602259568801068 is too high


   #   
  ###  
 ##@## 
##@#@##
 ##@## 
  ###  
   #   

    #
   ###   
  ##@##  
 ##@#@## 
##@###@##
 ##@#@## 
  ##@##  
   ###   
    #

# assuming S is always placed at center...
# to go from any 1 side to another takes 131 steps
    # Top to bottom fills 5555 spots
    # bottom to top, 5541
    # left to right, 5538
    # right to left, 5558