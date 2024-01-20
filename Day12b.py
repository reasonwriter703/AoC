import sys
import os
import time
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()
from functools import lru_cache

@lru_cache(maxsize=None)    # use LRU Cache
def validate(spr):
    haystack = spr[:-1].replace('?','').replace('#','')
    return (len(haystack) == 0 and spr[-1] != '#')

def find_configs(spring, record):
    spring = spring.strip('.') + '.'
    configs = ('',)
    ct_mod = 0
    mod = []
    for rec_i, rec in enumerate(record):

        '''
        if rec_i % ct_rec == 0:     #shortcut
            mod.append(len(configs))
            ct_mod += 1
            #print(rec_i, len(configs))
            if len(mod) == 3:
                result = mod[2]
                # if spring1[0] + spring1[-1:] == '??':
                #     for e in range(2):
                #         result *= int(mod[2] / mod[1])
                #     result *= find_configs(spring1, record1)
                # else:
                for e in range(3):
                    result *= int(mod[2] / mod[1])
                # print(result)
                # return result
        '''
        newconfigs = []
        trim_r = 1 + sum(record[rec_i+1:]) + len(record[rec_i+1:])
        lastrec = (rec_i == len(record) - 1)
        for config in configs:
            for scope_i in range(((len(spring) - len(config) - trim_r) - rec) + 1):
                trim_l = len(config) + scope_i
                if not validate(spring[trim_l:trim_l + rec + 1]) or '#' in spring[max(len(config) - 1, 0):trim_l]: continue
                new = config + ('.' * scope_i) + ('#' * rec) + '.'
                if lastrec and '#' in spring[len(new):]: continue   #on last iter, extra check for spare #s in tail
                newconfigs.append(new)
        if len(newconfigs) != 0:
            configs = tuple(newconfigs)

    print(len(configs))#, result, sep='\t')
    return len(configs)

start_time = time.time()
total_arrangements = 0
for i, row in enumerate(open('Day12-input.txt', 'r')):
    spring1, record1 = row.split()
    record1 = tuple([int(n) for n in record1.split(',')])
    ct_rec = len(record1)
    folds = 5
    record5 = record1 * folds
    while spring1.find('..') != -1:
        spring1 = spring1.replace('..', '.')
    spring5 = '?'.join([spring1 for i in range(folds)])

    print("Line " + str(i + 1) + ' of 1000', spring1, record1)
    total_arrangements += find_configs(spring5, record5)
    print('')
print(total_arrangements)
print('Time taken:', time.time() - start_time)

#942735524121786 is too high