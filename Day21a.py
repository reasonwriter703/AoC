file1 = open('Day21-input.txt', 'r')
Lines = file1.readlines()
Lines[:] = [line.strip() for line in Lines]
Lines[:] = [line.replace(".", "_") for line in Lines]
tbl = [list(i) for i in Lines]  #create matrix

#find S, set to O
for rS, row in enumerate(tbl):
    if "S" in row: break
for cS, col in enumerate(tbl[rS]):
    if col == "S": break
tbl[rS][cS] = "O"


def take_step(tbl, y, x):
    if tbl[y][x] != "_": return tbl[y][x]
    try:
        if tbl[y+1][x] == "O":
            return "n"
    except IndexError: pass
    try:
        if tbl[y-1][x] == "O":
            return "n"
    except IndexError: pass
    try:
        if tbl[y][x+1] == "O":
            return "n"
    except IndexError: pass
    try:
        if tbl[y][x-1] == "O":
            return "n"
    except IndexError: pass
    return tbl[y][x]

#take n steps
for i in range(198):
    for y, row in enumerate(tbl):
        for x, col in enumerate(row):
            tbl[y][x] = take_step(tbl, y, x)

    for row in tbl:
        row[:] = [r.replace("O", "_") for r in row]
        row[:] = [r.replace("n", "O") for r in row]
#        print("".join(row))
#    print("")

#count finishing positions
count = 0
for row in tbl:
    print("".join(row))
    count += sum(1 for x in row if x == "O")
print(count)