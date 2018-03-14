""""
Programmer: Briton A. Powe          Program Homework Assignment #2
Date: 3/13/18                       Class: Introduction to A.I.
Version: 1.0.2
File: Player Class
------------------------------------------------------------------------
Program Description:
This is the player class required for the main program
***This program uses Python 3.6.4***
"""
import Board
import os
import copy

#class designating all players
class Player:
    def __init__(self, maxStatus):
        self.__availableValues = []
        self.__isMax = maxStatus
        self.__availableSpaces = []
        self.__currentState = []
        self.__setAvailableValues()
        self.__usedValues = []

    #determine if max
    def getIsMax(self):
        return self.__isMax

    #update the available spaces
    def setAvailableSpaces(self, board):
        self.__availableSpaces = board.availableMoves()

    #return available spaces
    def getAvailableSpaces(self):
        return self.__availableSpaces

    def setState(self, board):
        self.__currentState = board.getBoardState()

    def resetState(self):
        self.__currentState = [0,0,0,0,
                               0,0,0,0,
                               0,0,0,0,
                               0,0,0,0]

    #set players numbers based on whether max
    def __setAvailableValues(self):
        if self.__isMax == True:
            self.__availableValues = [1,3,5,7,9,11,13,15]
        else:
            self.__availableValues = [2,4,6,8,10,12,14,16]

    def getAvailibleValues(self):
        return self.__availableValues

    #Function for human move
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
                                self.__availableValues.remove(value)
                         except ValueError:
                            print("\nError! Please only enter an integer for value and index.")   
            
            except ValueError:
                print("\nError! Please only enter an integer for value and index.")

    def getUsedValues(self):
        return self.__usedValues

    #Function for computer move
    def compMakeMove(self, value, index, board):
        board.setValue(value, index)
        self.setState(board)
        self.setAvailableSpaces(board)
        self.__usedValues.append(self.__availableValues.pop(self.__availableValues.index(value)))

