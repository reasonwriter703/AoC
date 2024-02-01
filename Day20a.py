import sys
import os
import time
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()
p_hi = 0
p_lo = 0
mods = {}

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
    except KeyError: return
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

#load all modules
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

for press in range(1000):
    #button sends lo pulse to broadcaster
    p_list = [('button', 0, 'broadcaster')]
    while p_list:
        if press < 3: print(p_list[0][0] + (' -hi-> ' if p_list[0][1] else ' -lo-> ') + p_list[0][2])
        if p_list[0][1]:    p_hi += 1
        else:               p_lo += 1
        send(p_list[0])
    if press < 3: print('')

print('lo: ', p_lo, '', 'hi: ', p_hi, sep:='\t')
print('RESULT: ', p_lo * p_hi)
print('Time taken:', time.time() - start_time)