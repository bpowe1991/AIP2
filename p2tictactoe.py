import random

gameBoard = [1,1,1,0,
             2,3,3,3,
             2,4,5,5,
             2,4,6,7]

winSpaceIndex = [[0,1,2,3],
             [4,5,6,7],
             [8,9,10,11],
             [12,13,14,15],
             [0,4,8,12],
             [1,5,9,13],
             [2,6,10,14],
             [3,7,11,15],
             [0,5,10,15],
             [3,6,9,12]]

winSpaceValues = []
currentSums = []
END_SUM = 34
inEndState = False


def calculateSpaceValues():
    currentSpaceGroup = []
    for element in winSpaceIndex:
        for index in element:
            currentSpaceGroup.append(gameBoard[index])
        winSpaceValues.append(currentSpaceGroup)
        currentSpaceGroup = []
  

calculateSpaceValues()


def calculateSums():
    for index in range(len(winSpaceValues)):
        currentSums.append(sum(winSpaceValues[index]))
    print(currentSums)


calculateSums()


def determineEndState(inEndState):
    if not gameBoard.__contains__(0):
        inEndState = True
    else:
        for sumIndex, sumValue in enumerate(currentSums, 0):
            if sumValue == END_SUM:
                if not winSpaceValues[sumIndex].__contains__(0):
                    inEndState = True
    print(inEndState)

determineEndState(inEndState)

def insertValue(value, index):
    gameBoard[index] = value

def reevaluateBoard():
    
