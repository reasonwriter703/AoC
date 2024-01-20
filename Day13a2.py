import sys
import os
import time
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()

def sym(tbl):
    factor = 100
    for q in range(2):
        for y, row in enumerate(tbl):
            if y == 0: continue
            if tbl[y-1] == tbl[y]:
                neg = y - 1
                pos = y
                while True:
                    try:
                        if neg < 0 or tbl[pos] == None:
                            print(y, y + 1, '><' if factor == 1 else 'X')
                            return y * factor
                        elif tbl[neg] == tbl[pos]:
                            neg -= 1
                            pos += 1
                        else:
                            break
                    except IndexError:
                        print(y, y + 1, '><' if factor == 1 else 'X')
                        return y * factor
        tbl = [list(i) for i in zip(*tbl)]  #transpose, then loop
        factor = 1
    print(tbl)  #code will only reach this point if NO symmetry is found

tbl = []
total = 0
for row in open('Day13-input.txt', 'r'):
    row = row.replace('\n','')
    col = []
    if row == '':
        total += sym(tbl)
        tbl = []
        continue
    for c in row:
        col.append(c)
    tbl.append(col)
total += sym(tbl)   #repeast sym for last tbl

print(total)
print('Time taken:', time.time() - start_time)