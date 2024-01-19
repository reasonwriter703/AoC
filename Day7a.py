import operator

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
hexrank = {'A': 'e', 'K': 'd', 'Q': 'c', 'J': 'b', 'T': 'a'}

H = []
for line in Lines:
    h = line[:5]
    b = line[6:]
    for char in hexrank.keys():
        h = h.replace(char, hexrank[char])

    dic = {}
    for char in h:
        dic[char] = dic.get(char, 0) + 1
    matches = max(dic.values())
    if matches == 3:
        if 2 in dic.values(): matches = 3.2
    elif matches == 2:
        if operator.countOf(dic.values(), 2) == 2: matches = 2.2

    H.append(hand(h, b, matches, int(h, 16)))

H.sort(key=operator.attrgetter("hexval"))
H.sort(key=operator.attrgetter("matches"))

winnings = 0
for i, hand in enumerate(H):
    print(i + 1, hand.hand, hand.bet, hand.hexval, hand.matches, sep="\t")
    winnings += int(hand.bet) * (i + 1)
print(winnings)