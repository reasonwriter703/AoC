import sys
import os
import time
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()

inst = "LRRLRRLRLLLRLLRLRRLRRLRRLRRLLRLLRRRLRRRLRRLLLRLRRLLLLLRRRLRRRLRRRLRRLRRLRLRLRLRLRRRLRRRLRRRLRRLRRLRLRLRRLLRRRLLRRLRRLRRRLRLLRRLRRLRRRLRRRLRRRLRRRLRRLLLRRRLLRRLLLRRLRRLLRRLRRRLRRLRRLRRRLRRLLLRLRRRLLRRRLRLRRLRLRLRLRRRLRLRLRRLLRRLRRLRRLRRLLRLRLRRRLRRLRRLRRLRLRRRLRRLRLLRRLLRRLRLLLRLLRRRLRLRLLRRRR"
file1 = open('Day8-input.txt', 'r')

#load each L/R element into key-value pairs
Lines = file1.readlines()
dict = {}
AllNodes = []
for line in Lines:
    dict[line[:3] + "-L"] = line[7:10]
    dict[line[:3] + "-R"] = line[12:15]
    if line[2:3] == "A":
        AllNodes.append(line[:3])
print("Starting nodes:", len(AllNodes))


count = 0
factors = []
for i in range(len(AllNodes)):
    factors.append(0)

from functools import reduce
from math import gcd
def lcf(numbers):
    # Use the 'reduce' function to apply a lambda function that calculates the LCF for a pair of numbers.
    return reduce((lambda x, y: int(x * y / gcd(x, y))), numbers)

while True:
    for i in inst:
        count += 1
        AllNodes = [dict[n + "-" + i][:3] for n in AllNodes]

        for l, k in enumerate(AllNodes):
            if k[2:] == 'Z' and factors[l] == 0:
                factors[l] = count

    print(count, factors)
    if not any(f == 0 for f in factors):
        break

print(lcf(factors))
print('Time taken:', time.time() - start_time)