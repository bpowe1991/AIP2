from .Board import Board

class Player:
    def __init__(self, maxStatus):
        self.__availableValues = []
        self.__isMax = maxStatus
        self.__availableSpaces = []

    def setAvailableSpaces(self, board):
        self.__availableSpaces = board.__availableSpaces


