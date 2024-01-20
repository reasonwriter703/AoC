import sys
import os
import time
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()

class part:
    def __init__(c, x,m,a,s):
        c.x=x
        c.m=m
        c.a=a
        c.s=s

file1 = open('Day19-input.txt', 'r')
Lines = file1.readlines()
Lines[:] = [line.strip() for line in Lines]

parts = []
fns = {}

#parse txt file
for line in Lines:
    line = line.replace("}", "")
    if line == "": continue
    elif line[:1] == "{":   #add part
        line = line.split(",")
        line[:] = [l[l.find("=")+1:] for l in line]
        parts.append(part(int(line[0]), int(line[1]), int(line[2]), int(line[3])))
    else:   #add function
        line = line.split("{")
        fns[line[0]] = line[1]

def parse_fn(x,m,a,s, fn):
    fn = fn.split(",")
    for f in fn[:-1]:
        colon = f.find(":")
        if eval(f[:colon]):
            return f[colon+1:]
    return fn[-1]

total = 0
for part in parts:
    fn = "in"
    while True:
        fn = parse_fn(part.x, part.m, part.a, part.s, fns[fn])
        print(part.x, fn)
        if fn not in fns:
            print()
            break

    if fn == "A":
        total += (part.x + part.m + part.a + part.s)
print(total)
print('Time taken:', time.time() - start_time)