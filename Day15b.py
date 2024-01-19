import sys
import os
import time
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()

with open('Day15-input.txt', 'r') as f:
    str = f.read().rstrip()

box = []
for i in range(256):
    box.append({})
for i in str.split(","):
    v = 0
    lbl = ""
    for c in i:
        if c == "-" or c == "=":
            if c == "-":
                try:
                    del box[v][lbl]
                except:
                    pass
            elif c == "=":
                box[v][lbl] = int(i[i.find("=")+1:])
            break
        else:
            lbl = lbl + c
            v += ord(c)
            v *= 17
            v %= 256

fpow = []
for b, dic in enumerate(box):
    for slot, lbl in enumerate(dic):
        fpow.append(int((1 + b) * (slot + 1) * dic[lbl]))

print(fpow)
print(sum(fpow))
print('Time taken:', time.time() - start_time)