import sys
import os
import time
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()
result = 0
fns = {}
fullrange = {'x_min': 1, 'x_max': 4001, 'm_min': 1, 'm_max': 4001, 'a_min': 1, 'a_max': 4001, 's_min': 1, 's_max': 4001}

#parse txt file
for line in open('Day19-input.txt', 'r'):
    try:
        line = line.strip().split('{')
        fns[line[0]] = line[1][:-1]
    except IndexError: break    #ignore parts

def run_workflow(fn, ranges):
    if fn in fns:
        for f in fns[fn].split(','):
            try:
                range_branch = ranges.copy()
                oper, output = f.split(':')
                if oper[1] == '<':
                    range_branch[oper[0] + '_max'] = int(oper[2:])
                    ranges[oper[0] + '_min'] = int(oper[2:])
                else:
                    range_branch[oper[0] + '_min'] = int(oper[2:]) + 1
                    ranges[oper[0] + '_max'] = int(oper[2:]) + 1
                run_workflow(output, range_branch)

            except ValueError:  #else output
                run_workflow(f, ranges)
    else:
        match fn:
            case 'A':
                global result
                result += len(range(ranges['x_min'], ranges['x_max'])) * len(range(ranges['m_min'], ranges['m_max'])) * len(range(ranges['a_min'], ranges['a_max'])) * len(range(ranges['s_min'], ranges['s_max']))
            case 'R':
                pass
            case _: 
                print('error - unknown fn: ' + fn)
        return

run_workflow('in', fullrange)
print(result)
print('Time taken:', time.time() - start_time)