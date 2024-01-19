smudge = [True]

def smudge_match(row_n, row_p):
    if row_n == row_p:
        return True
    elif smudge[0]:
        false_ct = 0
        for i in range(len(row_n)):
            #check by char
            if row_n[i] != row_p[i]:
                false_ct += 1
            if false_ct > 1:
                return False
        smudge[0] = False
        return True
    else:
        return False

def sym(tbl):
    factor = 100
    for q in range(2):
        for y, row in enumerate(tbl):
            if y == 0: continue
            smudge[0] = True
            if smudge_match(tbl[y-1], tbl[y]):
                neg = y - 1
                pos = y
                while True:
                    neg -= 1
                    pos += 1
                    try:
                        if not smudge[0] and (neg < 0 or tbl[pos] == None): #only accept answer if smudge is found
                            print(y, y + 1, '><' if factor == 1 else 'X')
                            return y * factor
                        elif smudge_match(tbl[neg], tbl[pos]):
                            continue
                        else:
                            smudge[0] = True
                            break
                    except IndexError:
                        if not smudge[0]:   #only accept answer if smudge is found
                            print(y, y + 1, '><' if factor == 1 else 'X')
                            return y * factor
                        else:
                            break
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

#38110 is too high