import sys
import os
import time
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()

def sym(tbl, transp = False):
    for y, row in enumerate(tbl):
        try:
            if tbl[y-1] == tbl[y]:
                neg = y-1
                pos = y
                x = 1
                while True:
                    try:
                        if tbl[neg - x] == None or tbl[pos + x] == None:
                            print(neg + 1, pos + 1)
                            if transp:
                                return neg + 1
                            else:
                                return (neg + 1) * 100
                        elif tbl[neg - x] == tbl[pos + x]:
                            x += 1
                        else:
                            return 0
                    except IndexError:
                        print(neg + 1, pos + 1)
                        if transp:
                            return neg + 1
                        else:
                            return (neg + 1) * 100
        except IndexError:
            pass
        # try:
        #     if tbl[y-1] == tbl[y+1]:
        #         sym_ext(y-1, y+1)
        # except IndexError:
        #     pass

    print(tbl)

tbl = []
total = 0
for row in open('Day13-demo.txt', 'r'):
    row = row.replace('\n','')
    col = []
    if row == '':
        total += sym(tbl)
        tbl = [list(i) for i in zip(*tbl)]  #transpose
        total += sym(tbl, True)

        tbl = []
        continue
    for c in row:
        col.append(c)
    tbl.append(col)
total += sym(tbl)
tbl = [list(i) for i in zip(*tbl)]  #transpose
total += sym(tbl, True)

print(total)
print('Time taken:', time.time() - start_time)