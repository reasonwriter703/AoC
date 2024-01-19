class race:
    def __init__(r, time, dist):
        r.time = time
        r.dist = dist

races = []
if False:    #true = demo data
    races.append(race(71530,940200))
else:
    races.append(race(51926890,222203111261225))

prod = 1
for r in races:
    mrg = 0
    for i in range(1,r.time):
        dist = i * (r.time-i)
        if dist > r.dist: mrg += 1
    prod *= mrg
    print(prod)