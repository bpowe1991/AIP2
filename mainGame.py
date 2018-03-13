import random
import math
import Board
import Player
import os
import copy

def iterativeDeepeningMiniMax(state, players):
    moves = []
    for d in range(1, 2):
        moves = minValue(state, players, d)
        sorted(moves, key=lambda move: move[1])
    return moves[0]


def minValue(state, players, depth):
    # print("::Welcome to MIN::")
    flag = 0
    print("Depth:",depth)
    if depth == 0 or state.isTerminalState():
        print(state.printWinningSpace())
        #del s,p
        return utility(state, flag)
    v = math.inf
    actions = generateMoves(state, players, flag)
    # print("Availible Moves:",actions)
    move = []
    for a in actions:
        print("Availible Moves:",actions)
        s = copy.deepcopy(state)
        p = copy.deepcopy(players)
        print("Current Move:",a)
        print("Current Board:",s.getBoardState())
        # print("Available Spaces(Odd):",p[flag].getAvailableSpaces())
        # print("Available Spaces(Even):",p[1].getAvailableSpaces())
        # print("Odd Player Values:",p[0].getAvailibleValues())
        # print("Even Player Values:",p[1].getAvailibleValues())
        # print("Current Flag(0=odd,1=even):",flag)
        p[flag].compMakeMove(a[0], a[1], s)
        p[1].setAvailableSpaces(s)
        print("Board After Move:",s.getBoardState(),"\n\n")
        # print("Available Spaces(Odd):",p[flag].getAvailableSpaces())
        # print("Available Spaces(Even):",p[1].getAvailableSpaces())
        # print("Odd Player Values:",p[0].getAvailibleValues())
        # print("Even Player Values:",p[1].getAvailibleValues())
        # print("Current Flag(0=odd,1=even):",flag,"\n\n\n")
        # answer = None

        v = min(v, maxValue(s,p, depth-1))
        move.append([a,v])
        del s,p
        # while answer is None:
        #         answer = input("To continue enter any key:\n")
    return move

def maxValue(state, players, depth):
    # print("::Welcome to MAX::")
    flag = 1
    print("Depth:",depth)
    if depth == 0 or state.isTerminalState():
        print(state.printWinningSpace())
        #del s,p
        return utility(state, flag)
    v = -math.inf
    actions = generateMoves(state, players, flag)
    move = []
    for a in actions:
        print("Availible Moves:",actions)
        s = copy.deepcopy(state)
        p = copy.deepcopy(players)
        print("Current Move:",a)
        print("Current Board:",s.getBoardState())
        # print("Available Spaces(Odd):",p[flag].getAvailableSpaces())
        # print("Available Spaces(Even):",p[1].getAvailableSpaces())
        # print("Odd Player Values:",p[0].getAvailibleValues())
        # print("Even Player Values:",p[1].getAvailibleValues())
        # print("Current Flag(0=odd,1=even):",flag)
        p[flag].compMakeMove(a[0], a[1], s)
        p[0].setAvailableSpaces(s)
        print("Board After Move:",s.getBoardState(),"\n\n")
        # print("Available Spaces(Odd):",p[flag].getAvailableSpaces())
        # print("Available Spaces(Even):",p[1].getAvailableSpaces())
        # print("Odd Player Values:",p[0].getAvailibleValues())
        # print("Even Player Values:",p[1].getAvailibleValues())
        # print("Current Flag(0=odd,1=even):",flag,"\n\n\n")
        # answer = None

        # if s.isTerminalState():
        #     print(s.printWinningSpace())
        #     del s,p
            
            # while answer is None:
            #     answer = input("To continue enter any key:\n")
            # continue
        # while answer is None:
        #         answer = input("To continue enter any key:\n")    
        v = max(minValue(s,p, depth-1))
        move.append([a,v])
        del s,p
    return move

def utility(state, flag):
    score = 0
    state.setValue(15,15)
    print(state.getSums())
    if state.getSums().__contains__(34):
        print("True")
        if flag == 0:
            score += 100
        else:
            score -= 100
    else:
        if state.availableMoves() == []:
            score += 0
        else:
            for space in state.getWinSpaceValues():
                numElements = 0
                numEven = 0
                numOdd = 0
                for value in space:
                    if value != 0:
                        numElements += 1
                        if value % 2 == 0:
                            numEven += 1
                        else:
                            numOdd += 1
                if flag == 0:
                    if numElements == 0:
                        score -= 1
                    elif numElements == 1:
                        if numEven > numOdd:
                            score -= 5
                        else:
                            score += 5
                    elif numElements == 2:
                        if numEven == numOdd:
                            score -= 5
                    elif numElements == 3:
                        if numEven == 2:
                            score -= 10
                        elif numOdd == 2:
                            score -= 15
                else:
                    if numElements == 0:
                        score += 1
                    elif numElements == 1:
                        if numEven > numOdd:
                            score += 5
                        else:
                            score -= 5
                    elif numElements == 2:
                        if numEven == numOdd:
                            score += 5
                    elif numElements == 3:
                        if numEven == 2:
                            score += 10
                        elif numOdd == 2:
                            score += 15
    return score




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
##iterativeDeepeningMiniMax(state,players)


#print(utility(board, flag))
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