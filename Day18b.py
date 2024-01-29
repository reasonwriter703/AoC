import sys
import os
import time
import numpy as np
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()

def area_by_shoelace(x, y):
    #Assumes x,y points go around the polygon in one direction
    return abs( sum(i * j for i, j in zip(x,             y[1:] + y[:1]))
               -sum(i * j for i, j in zip(x[1:] + x[:1], y            ))) / 2

direc = ('R', 'D', 'L', 'U')
x, y = 0, 0
points = []
go_prev = ''
for row in open('Day18-input.txt', 'r'):
    #part 1
    # go, dist = row[0], int(row[1:row.find('(#')].strip())

    #part 2
    inst = row.find('(#')+2
    inst = row[inst:inst+6]
    go, dist = direc[int(inst[-1])], int(inst[:-1], 16)
    print(go, dist)

    if go_prev == '':
        #skip first inst, add back in at end
        go_first = go
        add_x = 0
        add_y = 0
    else:
        # convert instructions to xy points on OUTSIDE EDGE of lagoon
        #use DL corner as default
        add_x = 'D' in go_prev + go
        add_y = 'R' in go_prev + go
        points.append((x + add_x, y + add_y))

    go_prev = go

    match go:
        case 'R':
            x += dist
        case 'D':
            y -= dist
        case 'L':
            x -= dist
        case 'U':
            y += dist

add_x = 'D' in go + go_first
add_y = 'R' in go + go_first
points.append((x + add_x, y + add_y))

x, y = zip(*points)
print(area_by_shoelace(x, y))
print('Time taken:', time.time() - start_time)