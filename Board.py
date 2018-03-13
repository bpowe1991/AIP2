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
        for index in range(len(self.__gameBoard)):
            self.__gameBoard[index] = 0
        self.__isTerminal = False
        self.__winSpaceValues[:] = []
        self.__currentSums[:] = []
    
    def __setWinSpaceValues(self):
        self.__winSpaceValues[:]=[]  
        currentSpaceGroup = []
        for element in self.__winSpaceIndex:
            for index in element:
                currentSpaceGroup.append(self.__gameBoard[index])
            self.__winSpaceValues.append(currentSpaceGroup)
            currentSpaceGroup = []

    def __setSums(self):
        self.__currentSums[:] = []
        for index in range(len(self.__winSpaceValues)):
            self.__currentSums.append(sum(self.__winSpaceValues[index]))

    def __recalculate(self):
        self.__setWinSpaceValues()
        self.__setSums()

    def isTerminalState(self):
        if not self.__gameBoard.__contains__(0):
            self.__isTerminal = True
        else:
            for sumIndex, sumValue in enumerate(self.__currentSums, 0):
                if sumValue == self.__endSUM:
                    if not self.__winSpaceValues[sumIndex].__contains__(0):
                        self.__isTerminal = True
        return self.__isTerminal

    def setValue(self, value, index):
        self.__gameBoard[index] = value
        self.__recalculate()
        self.isTerminalState()

    def getInfo(self):
        print("Sum of Win Spaces: ", self.__currentSums)
        print("Win Space Values: ", self.__winSpaceValues)
        print("current Board: ", self.getBoardState())
        print("Is in Terminal State: ", self.isTerminalState())

    def printBoard(self):
        print("\n\n")
        index = 0
        for row in range(4):
            for col in range(4):
                if col != 3:
                    if self.__gameBoard[index] != 0:
                        print("\t", self.__gameBoard[index], "\t|", end='')
                    else:
                        print("\t \t|", end='')
                else:
                    if self.__gameBoard[index] != 0:
                        print("\t", self.__gameBoard[index])
                    else:
                        print(" ")
                index += 1
            if row != 3:
                print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
            else:
                print("\n\n")
    
    def availableMoves(self):
        moves = []
        for element in range(len(self.__gameBoard)):
            if self.__gameBoard[element] == 0:
                moves.append(element)
        return moves

    def printWinningSpace(self):
        if self.__currentSums.__contains__(self.__endSUM):
            index = self.__currentSums.index(self.__endSUM)
            return self.__winSpaceValues[index]
        else:
            return "N/A"

    def getSums(self):
        return self.__currentSums

    def getWinSpaceValues(self):
        return self.__winSpaceValues