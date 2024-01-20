import sys
import os
import time
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()

def find_configs(s, r):
    s = s.strip('.') + '.'
    s_potential = s.replace('?','#')
    configs = ['']
    for rec_i, rec in enumerate(r):
        newconfigs = []
        trim_r = 1 + sum(r[rec_i+1:]) + len(r[rec_i+1:])
        lastrec = (rec_i == len(record) - 1)
        for config in configs:
            for scope_i in range(((len(s) - len(config) - trim_r) - rec) + 1):
                trim_l = len(config) + scope_i
                haystack = s_potential[trim_l:trim_l + rec]
                if haystack != ('#' * rec) or s[trim_l + len(haystack)] == '#' or '#' in s[max(len(config) - 1, 0):trim_l]: continue
                new = config + ('.' * scope_i) + haystack + '.'
                if lastrec and '#' in s[len(new):]: continue   #on last iter, extra check for spare #s in tail
                newconfigs.append(new)
        if len(newconfigs) != 0:
            configs = newconfigs

    print(len(configs), s, r)
    for c in configs:
        print(c)
    print('')
    return len(configs)

total_arrangements = 0
for row in open('Day12-demo.txt', 'r'):
    spring, record = row.split()
    record = [int(n) for n in record.split(',')]
    total_arrangements += find_configs(spring, record)
print(total_arrangements)
print('Time taken:', time.time() - start_time)

#7676 is too high