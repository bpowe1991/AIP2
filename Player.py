import Board
import os
import copy

class Player:
    def __init__(self, maxStatus):
        self.__availableValues = []
        self.__isMax = maxStatus
        self.__availableSpaces = []
        self.__currentState = []
        self.__setAvailableValues()
        self.__usedValues = []

    def getIsMax(self):
        return self.__isMax

    def setAvailableSpaces(self, board):
        self.__availableSpaces = board.availableMoves()

    def getAvailableSpaces(self):
        return self.__availableSpaces

    def setState(self, board):
        self.__currentState = board.getBoardState()

    def resetState(self):
        self.__currentState = [0,0,0,0,
                               0,0,0,0,
                               0,0,0,0,
                               0,0,0,0]

    def __setAvailableValues(self):
        if self.__isMax == True:
            self.__availableValues = [1,3,5,7,9,11,13,15]
        else:
            self.__availableValues = [2,4,6,8,10,12,14,16]

    def getAvailibleValues(self):
        return self.__availableValues

    def makeMove(self, board):
        value = index = None
        #Input validation for value and index
        self.setAvailableSpaces(board)
        while value is None:
            
            try:
                chosenValue = input("\nEnter a value: \n\n")
                value = int(chosenValue)
                if not self.__availableValues.__contains__(value):
                    print("\nError! Please enter the available values: ", self.__availableValues)
                    value = None
                else:

                     while index is None:
                         try:
                             chosenIndex = input("\nEnter the index(0-15): \n\n")
                             index = int(chosenIndex)
                             if not self.__availableSpaces.__contains__(index):
                                 print("\nError! Please eneter the availible indexes: ", self.__availableSpaces)
                                 index = None
                             else:
                                board.setValue(value, index)
                                self.setState(board)
                                self.setAvailableSpaces(board)
                                self.__usedValues.append(self.__availableValues.pop(index))
                         except ValueError:
                            print("\nError! Please only enter an integer for value and index.")   
            
            except ValueError:
                print("\nError! Please only enter an integer for value and index.")

    def getUsedValues(self):
        return self.__usedValues

    def compMakeMove(self, value, index, board):
        print("Before: ", self.__availableValues, "\n", self.__availableSpaces)
        board.setValue(value, index)
        self.setState(board)
        self.setAvailableSpaces(board)
        self.__usedValues.append(self.__availableValues.pop(index))
        print("After: ", self.__availableValues, "\n", self.__availableSpaces)
        
# board = Board.Board()
# maxS = True
# player1 = Player(maxS)
# maxS2 = False
# player2 = Player(maxS2)


# turn = 0
# previousTurn = 1
# while board.isTerminalState() != True:
#     if turn == 0:
#         board.printBoard()
#         print("Turn - Player 1")
#         print("Available Values: ", player1.getAvailibleValues())
#         player1.setAvailableSpaces(board)
#         print("Available Spaces: ", player1.getAvailableSpaces())
#         player1.makeMove(board)
#         turn = 1
#         previousTurn = 0
#         os.system('cls' if os.name == 'nt' else 'clear')
#     else:
#         board.printBoard()
#         print("Turn - Player 2")
#         print("Available Values: ", player2.getAvailibleValues())
#         player2.setAvailableSpaces(board)
#         print("Available Spaces: ", player2.getAvailableSpaces())
#         player2.makeMove(board)
#         turn = 0
#         previousTurn = 1
#         os.system('cls' if os.name == 'nt' else 'clear')

# board.printBoard()
# print("End of game")
# if board.printWinningSpace() != []:
#     if previousTurn == 0:
#         print("Player 1 Wins!\nWinning Space:", board.printWinningSpace())
#     else:
#         print("Player 2 Wins!\nWinning Space:", board.printWinningSpace())
# else:
#     print("Tie Game!")

# print("\n\n\n")
# del player1, player2, board