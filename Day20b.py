import sys
import os
import time
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()

class module:
    def __init__(c, type, dest):
        c.type = type
        c.dest = dest
        c.on = False
        c.conj = {}

def send(tpl):
    mod_sent, p, mod_dest = tpl
    p_list.pop(0)
    try:
        module = mods[mod_dest]
    except KeyError:
        # assumes mod_dest always == 'rx':
        for m in mods[mod_sent].conj:
            if mods[mod_sent].conj[m] and m not in sq_list:
                sq_list[m] = press
                print(sq_list)
        return
    match module.type:
        case '%':   #Flip-flop - if given lo pulse, toggles on/off. Sends hi pulse of turned on, lo pulse if turned off
            if p: return
            module.on = not module.on
            p = module.on
        
        case '&':   #Conjunction - remembers last pulse from each connected module. Sends lo if all are hi, else sends hi
            module.conj[mod_sent] = p
            p = 0 in module.conj.values()

    for d in module.dest:
        p_list.append((mod_dest, p, d))
    return

from functools import reduce
from math import gcd
def lcf(numbers):
    # Use the 'reduce' function to apply a lambda function that calculates the LCF for a pair of numbers.
    return reduce((lambda x, y: int(x * y / gcd(x, y))), numbers)

#load all modules
mods = {}
for row in open('Day20-input.txt', 'r'):
    id, dest = row.split(' -> ')
    if id[0] in '%&':
        mods[id[1:]] = module(id[0], [d.strip() for d in dest.split(',')])
    else:
        mods[id] = module(id, [d.strip() for d in dest.split(',')])

#load conjunction inputs
for m in mods:
    for d in mods[m].dest:
        try:
            if mods[d].type == '&':
                mods[d].conj[m] = 0
        except KeyError:
            pass

#press button until first instance of all hi pulses to sq inputs are located
press = 0
sq_list = {}
while True:
    press += 1
    #button sends lo pulse to broadcaster
    p_list = [('button', 0, 'broadcaster')]
    while p_list:
        send(p_list[0])
    if len(sq_list) == len(mods['sq'].conj): break

print('RESULT: ', lcf(sq_list.values()))
print('Time taken:', time.time() - start_time)