import sys
import os
import time
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()

with open('Day15-input.txt', 'r') as f:
    str = f.read().rstrip()
allv = []
for i in str.split(','):
    v = 0
    for c in i:
        v += ord(c)
        v *= 17
        v %= 256
    print(v)
    allv.append(v)

print(sum(allv))
print('Time taken:', time.time() - start_time)