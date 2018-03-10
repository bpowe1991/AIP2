import random

gameBoard = [0,0,0,0,
             0,0,0,0,
             0,0,0,0
             0,0,0,0]

winSpaces = [[0,1,2,3],
             [4,5,6,7],
             [8,9,10,11],
             [12,13,14,15],
             [0,4,8,12],
             [1,5,9,13],
             [2,6,10,14],
             [3,7,11,15],
             [0,5,10,15],
             [3,6,9,12]]

currentSums = [0,0,0,0,0,0,0,0,0,0]

def calculateSum():
    total = 0
    currentSpace = []
    currentSumsIndex = 0
    for element in winSpaces:
        for index in element:
            currentSpace.append(gameBoard[index])
        print(currentSpace)
        currentSums[currentSumsIndex]sum(currentSpace)


#def checkTerminalState()
