import sys
import os
import time
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()

tbl = [row.strip('\n') for row in open('Day16-input.txt', 'r')]

def make_key(dr,y,x):
    return dr + str(y) + '.' + str(x)

def travel(dr,y,x):
    del splits[make_key(dr,y,x)]
    while x >= 0 and y >= 0:
        try:
            tile = tbl[y][x]
        except IndexError:
            break
        
        n_key = str(y) + '.' + str(x)
        try:
            nrg[n_key] += 1
        except KeyError:
            nrg[n_key] = 1
        
        match tile:
            case '/':
                if dr in 'UR':
                    dr = 'UR'.replace(dr,'')
                else:
                    dr = 'DL'.replace(dr,'')
            
            case '\\':
                if dr in 'UL':
                    dr = 'UL'.replace(dr,'')
                else:
                    dr = 'DR'.replace(dr,'')
            
            case '-':
                if dr in 'LR':
                    pass
                else:
                    if nrg[n_key] <= 4:
                        splits[make_key('L',y,x-1)] = ('L',y,x-1)
                        splits[make_key('R',y,x+1)] = ('R',y,x+1)
                    return

            case '|':
                if dr in 'UD':
                    pass
                else:
                    if nrg[n_key] <= 4:
                        splits[make_key('U',y-1,x)] = ('U',y-1,x)
                        splits[make_key('D',y+1,x)] = ('D',y+1,x)
                    return

        match dr:
            case 'U': y -= 1
            case 'D': y += 1
            case 'L': x -= 1
            case 'R': x += 1
    return

start = ('R','L','D','U')
max_nrg = 0
for edge in start:
    const = len(tbl[0]) - 1 if edge in 'UL' else 0
    for i in range(len(tbl[0])):
        if edge in 'UD':
            splits = {make_key(edge,const,i):(edge,const,i)}
        else:
            splits = {make_key(edge,i,const):(edge,i,const)}
        
        nrg = {}
        
        while True:
            try:
                i = next(iter(splits.values()))
                travel(i[0], i[1], i[2])
            except StopIteration:
                break

        if len(nrg) > max_nrg: max_nrg = len(nrg)
    print('max moving ' + edge + ':', max_nrg)

print('RESULT: ', max_nrg)
print('Time taken:', time.time() - start_time)