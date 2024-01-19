
file1 = open('Day2-input.txt', 'r')
Lines = file1.readlines()

#create class object
class Draw:
    def __init__(g, GameID, R, G, B):
        g.GameID = GameID
        g.R = R
        g.G = G
        g.B = B

#create list of all draws
Games = []
Draws = []

# Strips the newline character
for line in Lines:
    thisGame = line[:line.find(':')]
    line = line[len(thisGame)+1:]
    thisGame = int(thisGame[5:])
    Games.append(thisGame)
    
    line = line.strip()
    line = line.split(';')
    for d in line:
        red = 0
        grn = 0
        blu = 0
        d = d.split(',')
        for i in d:
            i = i.strip()
            i = i.split()
            match i[1]:
                case "red":
                    red = int(i[0])
                case "green":
                    grn = int(i[0])
                case "blue":
                    blu = int(i[0])
        
        #append class obj to list
        Draws.append(Draw(thisGame, red, grn, blu))

print("Total Games: ", len(Games))
for d in Draws:
    if d.R > 12 or d.G > 13 or d.B > 14:
        #impossible - do nothing
        try:
            Games.remove(d.GameID)
        except ValueError:
            pass  # do nothing!

print("Possible Games: ", len(Games))
print("SUM OF POSSIBLE GAMES: ", sum(Games))
