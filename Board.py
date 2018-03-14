""""
Programmer: Briton A. Powe          Program Homework Assignment #2
Date: 3/13/18                       Class: Introduction to A.I.
Version: 1.0.2
File: Board Class
------------------------------------------------------------------------
Program Description:
This is the board class required for the main program
***This program uses Python 3.6.4***
"""
#Class for game board
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
                                
    #return the current state of the board
    def getBoardState(self):
        return self.__gameBoard

    #resets the board
    def resetBoard(self):
        for index in range(len(self.__gameBoard)):
            self.__gameBoard[index] = 0
        self.__isTerminal = False
        self.__winSpaceValues[:] = []
        self.__currentSums[:] = []
    
    #keep track of the values in the possible win positions
    def __setWinSpaceValues(self):
        self.__winSpaceValues[:]=[]  
        currentSpaceGroup = []
        for element in self.__winSpaceIndex:
            for index in element:
                currentSpaceGroup.append(self.__gameBoard[index])
            self.__winSpaceValues.append(currentSpaceGroup)
            currentSpaceGroup = []

    #calculates the sums of the win positions
    def __setSums(self):
        self.__currentSums[:] = []
        for index in range(len(self.__winSpaceValues)):
            self.__currentSums.append(sum(self.__winSpaceValues[index]))

    #recalculates sums when there is a change
    def __recalculate(self):
        self.__setWinSpaceValues()
        self.__setSums()

    #determine if the game is over
    def isTerminalState(self):
        if not self.__gameBoard.__contains__(0):
            self.__isTerminal = True
        else:
            for sumIndex, sumValue in enumerate(self.__currentSums, 0):
                if sumValue == self.__endSUM:
                    if not self.__winSpaceValues[sumIndex].__contains__(0):
                        self.__isTerminal = True
        return self.__isTerminal

    #places value on board
    def setValue(self, value, index):
        self.__gameBoard[index] = value
        self.__recalculate()
        self.isTerminalState()

    #prints info about board
    def getInfo(self):
        print("Sum of Win Spaces: ", self.__currentSums)
        print("Win Space Values: ", self.__winSpaceValues)
        print("current Board: ", self.getBoardState())
        print("Is in Terminal State: ", self.isTerminalState())

    #prints board to screen
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
    
    #calculate available moves
    def availableMoves(self):
        moves = []
        for element in range(len(self.__gameBoard)):
            if self.__gameBoard[element] == 0:
                moves.append(element)
        return moves

    #returns winning space if there is one
    def printWinningSpace(self):
        if self.__currentSums.__contains__(self.__endSUM):
            index = self.__currentSums.index(self.__endSUM)
            return self.__winSpaceValues[index]
        else:
            return "N/A"

    #returns current sums of win positions
    def getSums(self):
        return self.__currentSums

    #returns current values in win positions
    def getWinSpaceValues(self):
        return self.__winSpaceValues