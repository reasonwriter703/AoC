import sys
import os
import time
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()

import re
result = 0
for row in open('Day1-input.txt', 'r'):
    num = row
    num_c = 0
    while len(num) != num_c:
        num_c = len(num)
        num = num.replace("one", "o1e").replace("two", "t2o").replace("three", "t3e").replace("four", "f4r").replace("five", "f5e").replace("six", "s6x").replace("seven", "s7n").replace("eight", "e8t").replace("nine", "n9e")
    num = re.sub('[^0-9]','', num)
    print(num)
    result += int(num[0] + num[-1])

print('RESULT: ', result)
print('Time taken:', time.time() - start_time)