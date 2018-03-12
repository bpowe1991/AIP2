import random
import math
import Board
import Player
import os
import copy

def iterativeDeepening():
    return

def utility(player):
    if player.getIsMax():
        return 100
    else:
        return -100

#def miniMax(board.getBoardState()):


# def maxValue(board, players):
#     if board.isTerminalState():
#         return utility(player)
#     v = -float(math.inf)
#     for action in generateMoves(players[0])
#         v = max(v,min)

def generateMoves(players):
    moves = []
    for player in players:
        for value in player.getAvailibleValues():
            for space in player.getAvailableSpaces():
                moves.append([value, space])
    return moves

def getOddMoves(player):
    return generateMoves(player)

board = Board.Board()
maxS = True
player1 = Player.Player(maxS)
maxS2 = False
player2 = Player.Player(maxS2)
player1.setAvailableSpaces(board)
player2.setAvailableSpaces(board)
print(generateMoves(player1))
print("\n",generateMoves(player2))
players = [player1, player2]
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
del player1, player2, board