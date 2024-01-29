import sys
import os
import time
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()
from functools import lru_cache

@lru_cache(maxsize=None)    # use LRU Cache
def validate(scope, rec):
    if not scope:
        return len(rec) == 0
    if not rec:
        return '#' not in scope

    match scope[0]:
        case '.':
            return validate(scope[1:], rec)
        case '#':
            if (len(scope) >= rec[0]
            and '.' not in scope[:rec[0]]
            and scope[rec[0]] != '#'):
                return validate(scope[rec[0]+1:], rec[1:])
            else:
                return 0
        case '?':
            return validate('#' + scope[1:], rec) + validate('.' + scope[1:], rec)

start_time = time.time()
all_configs = 0
for i, row in enumerate(open('Day12-input.txt', 'r')):
    spring, record = row.split()
    record = tuple([int(n) for n in record.split(',')]) * 5
    spring = '?'.join([spring for i in range(5)]).strip('.') + '.'
    
    configs = validate(spring, record)
    all_configs += configs
    print("Line " + str(i + 1), configs) #, spring, record, sep:='\t')
print(all_configs)
print('Time taken:', time.time() - start_time)