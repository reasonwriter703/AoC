import sys
import os
import time
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()
file1 = open('Day9-input.txt', 'r')
Lines = file1.readlines()
Lines[:] = [line.strip() for line in Lines]

OASIS = []
for line in Lines:
    line = line.split()
    line = [int(i) for i in line]
    seq = []
    seq.append(line)
    print(line)
    
    #create sub sequences for difference between each number in line
    #loop until differences are 0
    while True:
        subseq = []
        prev_n = seq[-1][0]
        for n in seq[-1][1:]:
            subseq.append(n - prev_n)
            prev_n = n

        if all(i == subseq[0] for i in subseq) and subseq[0] == 0:
            # add 0 to last line and append
            subseq.insert(0, 0)
            seq.append(subseq)
            break
        else:
            seq.append(subseq)

    while len(seq) > 1:
        #add the last item of the previous subseq to the last item of the current one. append.
        seq[-2].insert(0, seq[-2][0] - seq[-1][0])
        print(seq[-1])
        seq.pop()   #remove sub sequences until only one remains
    print(seq[0])
    OASIS.append(seq[0][0])
    print()
print(OASIS)
print(sum(OASIS))
print('Time taken:', time.time() - start_time)