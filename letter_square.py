layers = int(input("Layers:"))
width = layers + layers-1
#print(width)

letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

topBotdict = {}
i = 1
for value in letters:
    length = i+i-1
    topBotdict[value] = length*value
    i += 1
#print(topBotdict)

layerList = []

i = 1
for key, value in topBotdict.items():
    layerList.append(topBotdict[letters[layers-i]])
    if i == layers:
        break
    i += 1
#print(f"layerlist: {layerList}")

def addWidth(string: str, maxWidth: int, lettersList: str):
    letter = string[0]
    #print(letter)
    startingIndex = lettersList.index(letter)
    #print(startingIndex)
    newString = string
    i = startingIndex
    while len(newString) < maxWidth:
        newString = lettersList[i+1] + newString + lettersList[i+1]
        i += 1
    return newString
#print(addWidth(layerList[6], width, letters))

endgameList = []
for value in layerList:
    endgameList.append(
        addWidth(value, width, letters)
    )
#print(f"endgame: {endgameList}")

for value in endgameList:
    print(value)
endgameList.reverse()
#print(endgameList)
i = 1
while i < len(endgameList):
    print(endgameList[i])
    i += 1