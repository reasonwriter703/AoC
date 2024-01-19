inst = "LRRLRRLRLLLRLLRLRRLRRLRRLRRLLRLLRRRLRRRLRRLLLRLRRLLLLLRRRLRRRLRRRLRRLRRLRLRLRLRLRRRLRRRLRRRLRRLRRLRLRLRRLLRRRLLRRLRRLRRRLRLLRRLRRLRRRLRRRLRRRLRRRLRRLLLRRRLLRRLLLRRLRRLLRRLRRRLRRLRRLRRRLRRLLLRLRRRLLRRRLRLRRLRLRLRLRRRLRLRLRRLLRRLRRLRRLRRLLRLRLRRRLRRLRRLRRLRLRRRLRRLRLLRRLLRRLRLLLRLLRRRLRLRLLRRRR"
file1 = open('Day8-input.txt', 'r')
# inst = "LR"
# file1 = open('Day8-demo.txt', 'r')

#load each L/R element into key-value pairs
Lines = file1.readlines()
dict = {}
AllNodes = []
for line in Lines:
    dict[line[:3] + "-L"] = line[7:10]
    dict[line[:3] + "-R"] = line[12:15]
    if line[2:3] == "A":
        AllNodes.append(line[:3])
print("Starting nodes:", len(AllNodes))


count = 0
while True:
    for i in inst:
        count += 1
        AllNodes = [dict[n + "-" + i][:3] for n in AllNodes]

        print(count, AllNodes)
        if AllNodes[0][2:] == 'Z' and all(i[2:] == AllNodes[0][2:] for i in AllNodes):
            AllNodes = 0
            break

    if AllNodes == 0:
        break

print("RESULT: ", count)