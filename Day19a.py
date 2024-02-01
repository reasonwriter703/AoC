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

parts = []
fns = {}
#parse txt file
for line in open('Day19-demo.txt', 'r'):
    line = line.strip()
    if line == '': continue
    elif line[0] == '{':   #add part
        line = [int(l[l.find('=')+1:]) for l in line[:-1].split(',')]
        parts.append(part(line[0], line[1], line[2], line[3]))
    else:   #add function
        line = line.split('{')
        fns[line[0]] = line[1][:-1]

def parse_fn(x,m,a,s, fn):
    for f in fn.split(','):
        try:
            oper, output = f.split(':')
            if eval(oper):
                return output
        except ValueError:  #use else output
            return f

total = 0
for part in parts:
    fn = 'in'
    while True:
        fn = parse_fn(part.x, part.m, part.a, part.s, fns[fn])
        print(part.x, fn)
        if fn not in fns:
            print()
            break

    if fn == 'A':
        total += (part.x + part.m + part.a + part.s)
print(total)
print('Time taken:', time.time() - start_time)