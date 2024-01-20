import sys
import os
import time
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()
file1 = open('Day4-demo.txt', 'r')
Lines = file1.readlines()

class Card:
    def __init__(g, CardID, wns, yns):
        g.CardID = CardID
        g.wns = wns
        g.yns = yns

#lists of Cards with winning numbers, and your numbers
Cards = []
for line in Lines:
    card = line[:line.find(':')]
    line = line[len(card)+1:]
    card = int(card[5:])

    wns = []
    yns = []
    line = line.strip()
    line = line.split()
    prepipe = 1
    for n in line:
        if n == "|":
            prepipe = 0
        elif prepipe:
            wns.append(int(n))
        else:
            yns.append(int(n))
    Cards.append(Card(card, wns, yns))

total = 0
for card in Cards:
    wcount = 0
    for w in card.wns:
        if w in card.yns:
            wcount += 1
    if wcount: total += 2**(wcount-1)

print("TOTAL: ", total)
print('Time taken:', time.time() - start_time)