""""
Programmer: Briton A. Powe          Program Homework Assignment #2
Date: 3/13/18                       Class: Introduction to A.I.
Version: 1.0.2
File: Board Class
------------------------------------------------------------------------
Program Description:
Plays a game of numeric tic tac toe. Uses iterative deepening on minimax
***This program uses Python 3.6.4***
"""

import random
import math
import Board
import Player
import os
import copy
import time

#global for time keeping
startTime = 0

#Iterative mini max function
def iterativeDeepeningMiniMax(state, players):
    global startTime
    startTime = time.time()
    #Starting loop for mininmax algorithm
    for d in range(1, 100):
        moves = generateMoves(state, players, 1)
        minValueList = []
        for m in moves:
            #create copies of state and players for calculation
            s = copy.deepcopy(state)
            p = copy.deepcopy(players)
            p[1].compMakeMove(m[0], m[1], s)
            p[0].setAvailableSpaces(s)
            minValueList.append(minValue(s, p, d))
            del s, p

    maxValueInList = max(minValueList)
    bestMoves = []
    for index in range(len(minValueList)):
        if minValueList[index] == maxValueInList:
            bestMoves.append(index)
    minmaxIndex = bestMoves[random.randint(0,(len(bestMoves)-1))]
    return moves[minmaxIndex]

#Min function for minimax
def minValue(state, players, depth):
    #global for start time
    global startTime

    flag = 0
    if depth == 0 or state.isTerminalState() or time.time()-startTime >= 2:
        return utility(state, flag)
    v = math.inf
    actions = generateMoves(state, players, flag)
    move = []
    for a in actions:
        s = copy.deepcopy(state)
        p = copy.deepcopy(players)
        p[flag].compMakeMove(a[0], a[1], s)
        p[1].setAvailableSpaces(s)
        v = min(v,maxValue(s,p, depth-1))
        move.append([a,v])
        del s,p
    return v

#Max function for minimax
def maxValue(state, players, depth):
    global startTime
    flag = 1
    if depth == 0 or state.isTerminalState() or time.time()-startTime >= 2:
        return utility(state, flag)
    v = -math.inf
    actions = generateMoves(state, players, flag)
    move = []
    for a in actions:
        s = copy.deepcopy(state)
        p = copy.deepcopy(players)
        p[flag].compMakeMove(a[0], a[1], s)
        p[0].setAvailableSpaces(s)
        v = max(v, minValue(s,p, depth-1))
        move.append([a,v])
        del s,p
    return v

"""utitlit function to judge move. Values each move according number of even and odd
numbers"""
def utility(state, flag):
    score = 0
    state.setValue(15,15)
    if state.getSums().__contains__(34):
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
                #calculate for min
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
                #calculate for max
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



#function to create moves in minimax
def generateMoves(state, players, flag):
    moves = []
    for value in players[flag].getAvailibleValues():
        for space in players[flag].getAvailableSpaces():
                moves.append([value, space])
    return moves

#function for computer vs computer
def compVsComp():
    os.system('cls' if os.name == 'nt' else 'clear')
    board = Board.Board()
    comp1 = Player.Player(True)
    comp2 = Player.Player(False)
    comp1.setAvailableSpaces(board)
    comp2.setAvailableSpaces(board)
    oddPlayer = [comp2, comp1]
    evenPlayer = [comp1, comp2]

    turn = 0
    while not board.isTerminalState():
        #computer 1 start
        turn = 1
        print("Player 1 making move....")
        board.printBoard()
        print("Player 1 Values:", comp1.getAvailibleValues())
        comp1.setAvailableSpaces(board)
        print("Player 1 Available Spaces:", comp1.getAvailableSpaces())
        compMove = iterativeDeepeningMiniMax(board,oddPlayer)
        comp1.compMakeMove(compMove[0],compMove[1],board)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Player - 1")
        board.printBoard()
        print("Best Calculated Move:", compMove)
        print("Values Remaining:", comp1.getAvailibleValues())
        print("Spaces Remaining:", comp1.getAvailableSpaces())       
        
        if board.isTerminalState():
            break
        
        toContinue = None
        while toContinue is None:
            toContinue = input("To continue press ENTER:\n")
        #computer 2 start
        os.system('cls' if os.name == 'nt' else 'clear')
        turn = 2
        print("Player 2 making move....")
        board.printBoard()
        print("Player 2 Values:", comp2.getAvailibleValues())
        comp2.setAvailableSpaces(board)
        print("Player 2 Available Spaces:", comp2.getAvailableSpaces())
        compMove = iterativeDeepeningMiniMax(board,evenPlayer)
        comp2.compMakeMove(compMove[0],compMove[1],board)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Player - 2")
        board.printBoard()
        print("Best Calculated Move:", compMove)
        print("Values Remaining:", comp2.getAvailibleValues())
        print("Spaces Remaining:", comp2.getAvailableSpaces())     

        toContinue = None
        while toContinue is None:
            toContinue = input("To continue press ENTER:\n")
        os.system('cls' if os.name == 'nt' else 'clear')

    board.printBoard()    
    print("\n\nResult:")
    if turn == 1 and board.getSums().__contains__(34):
        print("Player 1 Wins!")
        print("Winning Space:", board.printWinningSpace())
    elif turn == 2 and board.getSums().__contains__(34):
        print("Player 2 Wins!")
        print("Winning Space:", board.printWinningSpace())
    else:
        print("Tie game!")
    del comp1, comp2, board

#Function for human vs player
def humanVsPlayer(currentOrder):
    os.system('cls' if os.name == 'nt' else 'clear')
    board = Board.Board()
    currentPlayer = 0
    if currentOrder == 1:
        player = Player.Player(True)
        comp = Player.Player(False)
        currentPlayer = 1
        players = [player, comp]
        humanLabel = "Player 1"
        comLabel = "Player 2"
    else:
        player = Player.Player(False)
        comp = Player.Player(True)
        currentPlayer = 2
        players = [player, comp]
        humanLabel = "Player 2"
        comLabel = "Player 1"

    #Start of game
    while board.isTerminalState() == False:
        if currentPlayer == 1:
            #human player
            board.printBoard()
            print("Turn -", humanLabel)
            print("Available Values: ", player.getAvailibleValues())
            player.setAvailableSpaces(board)
            print("Available Spaces: ", player.getAvailableSpaces())
            player.makeMove(board)
            currentPlayer = 2
            previousTurn = 1
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            #computer player
            print(comLabel, "making move....")
            board.printBoard()
            print(comLabel, "Values:", comp.getAvailibleValues())
            comp.setAvailableSpaces(board)
            print(comLabel, "Available Spaces:", comp.getAvailableSpaces())
            compMove = iterativeDeepeningMiniMax(board, players)
            comp.compMakeMove(compMove[0],compMove[1],board)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(comLabel)
            board.printBoard()
            print("Best Calculated Move:", compMove)
            print("Values Remaining:", comp.getAvailibleValues())
            print("Spaces Remaining:", comp.getAvailableSpaces())
            currentPlayer = 1
            previousTurn = 2
            os.system('cls' if os.name == 'nt' else 'clear')


    board.printBoard()
    print("End of game")
    if board.printWinningSpace() != []:
        if previousTurn == 1:
            print("Player 1 Wins!\nWinning Space:", board.printWinningSpace(), "\n\n")
        else:
            print("Player 2 Wins!\nWinning Space:", board.printWinningSpace(), "\n\n")
    else:
        print("Tie Game!")

    del player, comp, board


#Start of program with menu
print("+========================WELCOME========================+")
print("\n\n\t\t 4 X 4 NUMERIC TIC TAC TOE\n\n")
print("+========================*0X0X0*========================+")

choice = "Y"
while choice == "Y":
        gameMode = None
        while gameMode is None:
            try:
                print("\n\n Please choose a game mode\n\n")
                print("+=======================* MENU *=======================+")
                print("\n\t1. PLAYER VS. COMPUTER\n\t2. COMPUTER VS. COMPUTER\n\n")
                mode = input("Enter 1 or 2: ")
                gameMode = int(mode)
                if (gameMode != 1):
                    if(gameMode != 2):
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("\nInvalid Option! Please only enter 1 or 2.Hi\n")
                        gameMode = None
                    
            except ValueError:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(gameMode)
                print("\nInvalid Option! Please Enter 1 or 2Ho\n")
        
        #Choosing game mode
        if gameMode == 1:
            #human vs computer mode
            order = None
            while order is None:
                try:
                    order = int(input("\nDo you want to go 1st(odd = 1) or 2nd(even = 2)?: "))
                    if order != 1:
                        if order != 2:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("\nInvalid Option! 1 for 1st(odd) or 2 for 2nd(even).\n")
                            order = None
                except ValueError:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("\nInvalid Option! 1 for 1st(odd) or 2 for 2nd(even)WHY.\n")
                    order = None
                humanVsPlayer(order)

        elif gameMode == 2:
            #computer vs computer mode
            compVsComp()

        #Ask user to play another game
        currentChoice = None
        while currentChoice is None:
            currentChoice = input("Play another game(Y/N)?: ")
            if currentChoice.upper() == "Y":
                choice = currentChoice.upper()
            elif currentChoice.upper() == "N":
                print("Good-bye!")
                choice = currentChoice.upper()
            else:
                print("\nInvalid Option! Please enter Y(yes) or N(no).\n")
                currentChoice = None

            




