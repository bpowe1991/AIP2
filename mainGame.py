import random
import math
import Board
import Player
import os
import copy

def iterativeDeepeningMiniMax(state, players):
    for depth in range(1,17):
        flag = 1
        #actions = minValue(state, depth, flag, players)
        #print(actions)


def minValue(state, players):
    print("::Welcome to MIN::")
    flag = 0
    actions = generateMoves(state, players, flag)
    print("Availible Moves:",actions)

    for a in actions:
        s = copy.deepcopy(state)
        p = copy.deepcopy(players)
        print("Current Move:",a)
        print("Current Board:",s.getBoardState())
        print("Available Spaces(Odd):",p[flag].getAvailableSpaces())
        print("Available Spaces(Even):",p[1].getAvailableSpaces())
        print("Odd Player Values:",p[0].getAvailibleValues())
        print("Even Player Values:",p[1].getAvailibleValues())
        print("Current Flag(0=odd,1=even):",flag)
        p[flag].compMakeMove(a[0], a[1], s)
        p[1].setAvailableSpaces(s)
        print("Board After Move:",s.getBoardState())
        print("Available Spaces(Odd):",p[flag].getAvailableSpaces())
        print("Available Spaces(Even):",p[1].getAvailableSpaces())
        print("Odd Player Values:",p[0].getAvailibleValues())
        print("Even Player Values:",p[1].getAvailibleValues())
        print("Current Flag(0=odd,1=even):",flag,"\n\n\n")
        answer = None

        if s.isTerminalState():
            print(s.printWinningSpace())
            while answer is None:
                answer = input("To continue enter any key:\n")
            continue
        maxValue(s,p)
        while answer is None:
                answer = input("To continue enter any key:\n")

def maxValue(state, players):
    print("::Welcome to MAX::")
    flag = 1
    actions = generateMoves(state, players, flag)
    print("Availible Moves:",actions)

    for a in actions:
        s = copy.deepcopy(state)
        p = copy.deepcopy(players)
        print("Current Move:",a)
        print("Current Board:",s.getBoardState())
        print("Available Spaces(Odd):",p[flag].getAvailableSpaces())
        print("Available Spaces(Even):",p[1].getAvailableSpaces())
        print("Odd Player Values:",p[0].getAvailibleValues())
        print("Even Player Values:",p[1].getAvailibleValues())
        print("Current Flag(0=odd,1=even):",flag)
        p[flag].compMakeMove(a[0], a[1], s)
        p[0].setAvailableSpaces(s)
        print("Board After Move:",s.getBoardState())
        print("Available Spaces(Odd):",p[flag].getAvailableSpaces())
        print("Available Spaces(Even):",p[1].getAvailableSpaces())
        print("Odd Player Values:",p[0].getAvailibleValues())
        print("Even Player Values:",p[1].getAvailibleValues())
        print("Current Flag(0=odd,1=even):",flag,"\n\n\n")
        answer = None

        if s.isTerminalState():
            print(s.printWinningSpace())
            del s,p
            
            while answer is None:
                answer = input("To continue enter any key:\n")
            continue
        while answer is None:
                answer = input("To continue enter any key:\n")    
        minValue(s,p)
# def minValue(state, depth, flag, players):

#     actions = generateMoves(state, flag, players)

#     for a in actions:
#         actions = generateMoves(state, flag, players)
#         p = copy.deepcopy(players)
#         s = copy.deepcopy(state)
#         print("Actions: ", actions)
        
#         print("Board: ", s.getBoardState())
#         print("Odd Player Values: ",p[0].getAvailibleValues())
#         print("Even Player Values: ",p[1].getAvailibleValues())
#         print(a)
#         p[flag].compMakeMove(a[0], a[1], s)
#         p[flag+1].setAvailableSpaces(s)
#         print(a,"\n", s.getBoardState(),"\n",p[flag].getAvailibleValues(),"\n", p[flag].getAvailableSpaces())
#         flag = 1
#         print("Spaces Left: ", p[flag].getAvailableSpaces(),"\n")
#         if s.isTerminalState():
#             print("True")
#             print(s.printWinningSpace(), "\n\n")
#             flag = 0
#             del p,s

#             continue
#         maxValue(s, depth, flag, p)
#         print("Hello, I am MIN", flag)
#         print(s.getBoardState(),"\nCurrent Move:",a)


# def maxValue(state, depth, flag, players):
#     print("Hello, I am MAX", flag)
#     actions = generateMoves(state, flag, players)

#     for a in actions:
#         actions = generateMoves(state, flag, players)
#         p = copy.deepcopy(players)
#         s = copy.deepcopy(state)
#         print("Board: ", s.getBoardState())
#         print("Odd Player Values: ",p[0].getAvailibleValues())
#         print("Even Player Values: ",p[1].getAvailibleValues())
#         print(a)
#         p[flag].compMakeMove(a[0], a[1], s)
#         p[flag-1].setAvailableSpaces(s)
#         print(a,"\n", s.getBoardState(),"\n",p[flag].getAvailibleValues(),"\n", p[flag].getAvailableSpaces())
#         flag = 0
#         print("Spaces Left: ", p[flag].getAvailableSpaces(),"\n\n")
#         if s.isTerminalState():
#             print("True")
#             print(s.printWinningSpace(), "\n\n")
#             del p,s
#             flag = 1
#             continue
#         minValue(s, depth, flag, p)
#         print("Hello, I am MAX", flag)
#         print(s.getBoardState(),"\nCurrent Move:",a)


def utility(state, flag):
    if flag == 0:
        return 100
    else:
        return -100

def generateMoves(state, players, flag):
    moves = []
    for value in players[flag].getAvailibleValues():
        for space in players[flag].getAvailableSpaces():
                moves.append([value, space])
    return moves

board = Board.Board()
maxS = True
player1 = Player.Player(maxS)
maxS2 = False
player2 = Player.Player(maxS2)
player1.setAvailableSpaces(board)
player2.setAvailableSpaces(board)
# print(generateMoves(player1))
# print("\n",generateMoves(player2))
players = [copy.deepcopy(player1), copy.deepcopy(player2)]
state = copy.deepcopy(board)
flag = 0
d = 4
minValue(state, players)
#minValue(state, d, flag, players)
#print(generateMoves(state, flag, players))
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