import sys
import os
import time
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()
file1 = open('Day4-input.txt', 'r')
Lines = file1.readlines()

class Card:
    def __init__(g, CardID, wns, yns, copies):
        g.CardID = CardID
        g.wns = wns
        g.yns = yns
        g.copies = copies

#lists of Cards with winning numbers, and your numbers
Cards = []
Cards.append(Card(0, [], [], 0))
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
    Cards.append(Card(int(card), wns, yns, 1))

total = 0
for card in Cards:
    for c in range(card.copies):
        wcount = 0
        for w in card.wns:
            if w in card.yns:
                wcount += 1
                Cards[card.CardID + wcount].copies += 1

    for p in Cards:
        print(p.CardID, p.copies)
    print("")

print("TOTAL: ", sum(card.copies for card in Cards))
print('Time taken:', time.time() - start_time)