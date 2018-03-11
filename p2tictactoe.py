import random

class Board:
    def __init__(self):
        self.__endSUM = 34
        self.__isTerminal = False
        self.__currentSums = []
        self.__winSpaceValues = []
        self.__gameBoard = [0,0,0,0,
                            0,0,0,0,
                            0,0,0,0,
                            0,0,0,0]
        self.__winSpaceIndex = [[0,1,2,3],
                                [4,5,6,7],
                                [8,9,10,11],
                                [12,13,14,15],
                                [0,4,8,12],
                                [1,5,9,13],
                                [2,6,10,14],
                                [3,7,11,15],
                                [0,5,10,15],
                                [3,6,9,12]]
    
    def getBoardState(self):
        return self.__gameBoard

    def resetBoard(self):
        for index in self.__gameBoard:
            self.__gameBoard[index] = 0
        self.__isTerminal = False
        self.__winSpaceValues[:] = []
        self.__currentSums[:] = []
    
    def __setWinSpaceValues(self):
        self.__winSpaceValues[:]=[]  
        currentSpaceGroup = []
        for element in winSpaceIndex:
            for index in element:
                currentSpaceGroup.append(self.__gameBoard[index])
            self.__winSpaceValues.append(currentSpaceGroup)
            currentSpaceGroup = []

    def __setSums(self):
        self.__currentSums[:] = []
        for index in range(len(self.__winSpaceValues)):
            self.__currentSums.append(sum(self.__winSpaceValues[index]))

    def recalculate(self):
        self.__setWinSpaceValues


    def setValue(self, value, index):
        self.__gameBoard[index] = value



gameBoard = [0,0,10,10,
             0,0,0,0,
             0,0,0,0,
             0,0,0,0]

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
    winSpaceValues[:]=[]  
    currentSpaceGroup = []
    for element in winSpaceIndex:
        for index in element:
            currentSpaceGroup.append(gameBoard[index])
        winSpaceValues.append(currentSpaceGroup)
        currentSpaceGroup = []
    #print(winSpaceValues)

calculateSpaceValues()


def calculateSums():
    currentSums[:] = []
    for index in range(len(winSpaceValues)):
        currentSums.append(sum(winSpaceValues[index]))
    #print(currentSums)


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


def reevaluateBoard():
    #print(winSpaceValues)
    calculateSpaceValues()
    calculateSums()


def insertValue(value, index, board):
    board[index] = value
    reevaluateBoard()

def resetBoard(board, state):
    for index in board:
        board[index] = 0
    state = False


value = index = None
#Input validation for income
while value is None or index is None:
    
    try:
        #Convert user input into integer and check if in range
        value, index = [int(x) for x in input("Enter a value(first) and index(0-15)(second): \n\n").split()]
        if value <= 0:
            print("\nError! value must be greater than 0.")
            value = None
        elif index < 0 or index > 15:
            print("\nError! index must be between 0 and 15(0-15).")
            index = None
        else:
            insertValue(value,index, gameBoard)

    except ValueError:
        #Error message for non-integer input
        print("\nError! Please only enter an integer for value and index.")

determineEndState(inEndState)

resetBoard(gameBoard, inEndState)
determineEndState(inEndState)