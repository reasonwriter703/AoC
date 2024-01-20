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
    num = re.sub('[^0-9]','', row)
    result += int(num[0] + num[-1])

print('RESULT: ', result)
print('Time taken:', time.time() - start_time)