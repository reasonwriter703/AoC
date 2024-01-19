import operator
import sys
import os
import time
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()

file1 = open('Day7-input.txt', 'r')
Lines = file1.readlines()
Lines[:] = [line.strip() for line in Lines]

class hand:
    def __init__(r, hand, bet, matches, hexval):
        r.hand = hand
        r.bet = bet
        r.matches = matches
        r.hexval = hexval

#hirank = {'A', 14, 'K', 13, 'Q', 12, 'J', 11, 'T', 10}
hexrank = {'A': 'e', 'K': 'd', 'Q': 'c', 'J': '0', 'T': 'a'}

H = []
for line in Lines:
    h = line[:5]
    b = line[6:]
    for char in hexrank.keys():
        h = h.replace(char, hexrank[char])

    dic = {}
    matches = 0
    maxkey = '0'
    for char in h:
        if char == '0':
            matches += 1    #jokers
            continue

        dic[char] = dic.get(char, 0) + 1
        if (dic[char] == max(dic.values()) and int(char, 16) > int(maxkey, 16)) \
        or (dic[char] > dic.get(maxkey, 0)):
            maxkey = char

    dic[maxkey] = dic.get(maxkey, 0) + matches

    if dic[maxkey] == 3:
        if 2 in dic.values(): dic[maxkey] = 3.2
    elif dic[maxkey] == 2:
        if operator.countOf(dic.values(), 2) == 2: dic[maxkey] = 2.2

    H.append(hand(h, b, dic[maxkey], int(h, 16)))

H.sort(key=operator.attrgetter("hexval"))
H.sort(key=operator.attrgetter("matches"))

winnings = 0
for i, hand in enumerate(H):
    print(i + 1, hand.hand, hand.bet, hand.matches, sep="\t")
    winnings += int(hand.bet) * (i + 1)
print(winnings)
print('Time taken:', time.time() - start_time)