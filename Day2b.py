
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

# Strips the newline character
for line in Lines:
    thisGame = line[:line.find(':')]
    line = line[len(thisGame)+1:]
    thisGame = int(thisGame[5:])
    red = 0
    grn = 0
    blu = 0
    
    line = line.strip()
    line = line.split(';')
    for d in line:

        d = d.split(',')
        for i in d:
            i = i.strip()
            i = i.split()
            match i[1]:
                case "red":
                    if int(i[0]) > red:
                        red = int(i[0])
                case "green":
                    if int(i[0]) > grn:
                        grn = int(i[0])
                case "blue":
                    if int(i[0]) > blu:
                        blu = int(i[0])
        
    #append class obj to list
    Games.append(Draw(thisGame, red, grn, blu))

PowerSum = 0
for d in Games:
    PowerSum += (d.R * d.G * d.B)

print("SUM OF GAME SETS: ", PowerSum)
