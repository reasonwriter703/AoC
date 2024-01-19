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

def fillmap(y, x, steps, stretch = ""):
    if stretch == "x":
        tbl = [list(i + i) for i in Lines]
    #    x *= 2
    elif stretch == "y":
        tbl = [list(i + i + i) for i in Lines]
        tbl0 = [list(i + i + i) for i in Lines]
        for r in tbl0:
            tbl.append(r)
    #    x += maplen
    #    y *= 2
    else:
        tbl = [list(i) for i in Lines]  # reset matrix
    for row in tbl:
        row[:] = [r.replace("S", "_") for r in row]

    tbl[y][x] = "O"     #set new starting point

    # take n steps
    for i in range(steps-1):
        for y, row in enumerate(tbl):
            for x, col in enumerate(row):
                tbl[y][x] = take_step(tbl, y, x)

        for row in tbl:
            row[:] = [r.replace("O", "_") for r in row]
            row[:] = [r.replace("n", "O") for r in row]
    #        print("".join(row))
    #    print("")

    # count finishing positions
    count = 0
    for row in tbl:
        print("".join(row))
        count += sum(1 for j in row if j == "O")
    print("+", count, "", steps, "steps")
    print("")
    return count

file1 = open('Day21-demo.txt', 'r')
Lines = file1.readlines()
Lines[:] = [line.strip() for line in Lines]
Lines[:] = [line.replace(".", "_") for line in Lines]
tbl = [list(i) for i in Lines]  #create matrix
# find S
for rS, row in enumerate(tbl):
    if "S" in row: break
for cS, col in enumerate(tbl[rS]):
    if col == "S": break


# assuming S is always placed at center...
# to go from any 1 side to another takes 131 steps
    # Top to bottom fills 5555 spots
    # bottom to top, 5541
    # left to right, 5538
    # right to left, 5558

StepsLeft = 50 #26501365
isEven = (StepsLeft % 2 == 0)
#StepsLeft -= rS + 1  #start at center # from center, all 4 sides are reached on the 66th step.
plots = 0
maplen = len(row)   #131

#get amt of plots on completely filled maps
evenp = fillmap(rS, cS, maplen*2)       #7354
oddp = fillmap(rS, cS, (maplen*2)-1)    #7362

# skip via centered square formula
n = 1
fullmaps = 0
while StepsLeft > maplen*2:
    lastring = fullmaps
    fullmaps =  n * n + ((n - 1) * (n - 1))
    plots += (evenp if n % 2 == isEven else oddp) * (fullmaps - lastring)
    StepsLeft -= maplen
    n += 1
#    print(StepsLeft, plots, sep="\t")
print("steps left:", StepsLeft, "", "filled plots:", plots ,"n:", n, sep="\t")
n = n-2 # save for edge calcs
if n > 0:
    #EDGES
    plots += fillmap(maplen-1,0, StepsLeft, "x")*n
    plots += fillmap(0,0, StepsLeft, "x")*n
    plots += fillmap(0,maplen*2-1, StepsLeft, "x")*n
    plots += fillmap(maplen-1,maplen*2-1, StepsLeft, "x")*n

StepsLeft -= rS + 1 #add center steps back in
#TOP 3x2
plots += fillmap(0,cS + maplen, StepsLeft, "y")
#BOTTOM 3x2
plots += fillmap(maplen*2-1,cS + maplen, StepsLeft, "y")
#LEFT
plots += fillmap(rS,0, StepsLeft, "x")
#RIGHT
plots += fillmap(rS,maplen*2-1, StepsLeft, "x")
print("finishing plots:", plots)


# 602253595426282 is too low
# 602250651607978