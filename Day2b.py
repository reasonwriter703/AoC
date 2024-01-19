import sys
import os
import time
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()

PowerSum = 0
for game in open('Day2-input.txt', 'r'):
    game = game[game.find(':')+1:]
    g = {'red':0, 'green':0, 'blue':0}

    for draw in game.split(';'):
        draw = draw.split(',')
        for i in draw:
            i = i.strip().split()
            g[i[1]] = max(g[i[1]], int(i[0]))
    PowerSum += (g['red'] * g['green'] * g['blue'])

print("SUM OF GAME SETS: ", PowerSum)
print('Time taken:', time.time() - start_time)