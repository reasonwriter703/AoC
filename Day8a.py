import sys
import os
import time
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()

def loopInst(node):
    for i in inst:
        print(node)
        node = dict[node+"-"+i]
        global count
        count += 1
    return node

inst = "LRRLRRLRLLLRLLRLRRLRRLRRLRRLLRLLRRRLRRRLRRLLLRLRRLLLLLRRRLRRRLRRRLRRLRRLRLRLRLRLRRRLRRRLRRRLRRLRRLRLRLRRLLRRRLLRRLRRLRRRLRLLRRLRRLRRRLRRRLRRRLRRRLRRLLLRRRLLRRLLLRRLRRLLRRLRRRLRRLRRLRRRLRRLLLRLRRRLLRRRLRLRRLRLRLRLRRRLRLRLRRLLRRLRRLRRLRRLLRLRLRRRLRRLRRLRRLRLRRRLRRLRLLRRLLRRLRLLLRLLRRRLRLRLLRRRR"
#inst = "LLR"

#load each L/R element into key-value pairs
file1 = open('Day8-input.txt', 'r')
Lines = file1.readlines()
dict = {}
for line in Lines:
    dict[line[:3] + "-L"] = line[7:10]
    dict[line[:3] + "-R"] = line[12:15]

#for k in dict:
#    print(k, dict[k])


#set starting values
thisNode = "AAA"
count = 0

while thisNode != "ZZZ":
    thisNode = loopInst(thisNode)
    #print(count)

print("RESULT: ", count)
print('Time taken:', time.time() - start_time)