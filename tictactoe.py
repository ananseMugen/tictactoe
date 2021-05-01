#!/usr/bin/python3
#Alex Drew 04-30-21 (AKA 0xdeadbeef or ananseMugen)
#A terminal based tictactoe game. Main purpose of this is
#mostly just programming practice to get used to python before trying somehting more
#complex.
#If you like this program for whatever reason and it has brought you joy, buy me a beer
#if we ever meet :-)
#I'm not liable for damages incured while trying to use this program. You are, however
#obligated to tell how you managed to incur damages. I always like a good story
#I miss my semicolons, but fuck does this look neat.
#Yeetus maximus this is a stage test



import sys, random

#----------------All fucntions below here --------------------------------------
def printGrid(gridString):
    print(grid)

#Pass strings, really hate not defining types, self documenting my black fat ass
def updateBoard(player, location):
    board[location] = player

def greeting():
    print("""Hello, I'm your computer! Care for a game of tic-tac-toe? Y / n
          """)
    while True:
        answer = input()
        if answer.lower() == "y" :
            print("""Then let us play!
                     E on the board stands for
                     an empty space""")

            break
        elif answer.lower() == "n":
            sys.exit("Why did you summon me then, human? Very well, good bye.")
        else:
            print("Please use y for yes or n for no")

# gets play input, useable by human or AI. position takes the form of
#UpperLeft, UpperRight, ETC (yes all one word cause I'm lazy lol. Might manipulate
#input to allow for variations later)
def getPlayerInput(player):
    if player['symbol'] == 'X':
        print("Your move?")
        print("""
              Possible commands: UpperLeft/Center/Right
                                 MiddleLeft/Center/Right
                                 LowerLeft/Middle/Right
              """)
        position = None
        while position not in board.keys():
            position = input()
            if position not in board.keys():
                print("Please enter a valid command")
                continue
            else:
                if (board[position] != 'X') and (board[position] != 'O'):
                    updateBoard(player['symbol'], position)
                else:
                    print("That spots already taken, don't cheat! You're losing your turn!")
    else:
        #Fur AI
        print("My move!")
        position = AIdecisionMaker()
        while((board[position] != 'X') and (board[position] != 'O')):
            updateBoard(player['symbol'], position)

#Checks for win condition. If I hadn't defined the board as a dictionary, this probably
#Could have been waaaaaay neater.
def checkForWinCondition():
    if board['UpperLeft'] == 'X' and board['UpperCenter'] == 'X' and board['UpperRight'] == 'X':
        print("You win!")
        return True
    elif board['MiddleLeft'] == 'X' and board['MiddleCenter'] == 'X' and board['MiddleRight'] == 'X':
        print("You win!")
        return True
    elif board['LowerLeft'] == 'X' and board['LowerCenter'] == 'X' and board['LowerRight'] == 'X':
        print("You win!")
        return True
    elif board['UpperLeft'] == 'X' and board['MiddleLeft'] == 'X' and board['LowerLeft'] == 'X':
        print("You win!")
        return True
    elif board['UpperCenter'] == 'X' and board['MiddleCenter'] == 'X' and board['LowerCenter'] == 'X':
        print("You win!")
        return True
    elif board['UpperRight'] == 'X' and board['MiddleRight'] == 'X' and board['LowerRight'] == 'X':
        print("You win!")
        return True
    elif board['UpperLeft'] == 'X' and board['MiddleCenter'] == 'X' and board['LowerRight'] == 'X':
        print("You win!")
        return True
    elif board['UpperRight'] == 'X' and board['MiddleCenter'] == 'X' and board['LowerLeft'] == 'X':
        print("You win!")
        return True
    elif board['UpperLeft'] == 'O' and board['UpperCenter'] == 'O' and board['UpperRight'] == 'O':
        print("I win!")
        return True
    elif board['MiddleLeft'] == 'O' and board['MiddleCenter'] == 'O' and board['MiddleRight'] == 'O':
        print("I win!")
        return True
    elif board['LowerLeft'] == 'O' and board['LowerCenter'] == 'O' and board['LowerRight'] == 'O':
        print("I win!")
        return True
    elif board['UpperLeft'] == 'O' and board['MiddleLeft'] == 'O' and board['LowerLeft'] == 'O':
        print("I win!")
        return True
    elif board['UpperCenter'] == 'O' and board['MiddleCenter'] == 'O' and board['LowerCenter'] == 'O':
        print("I win!")
        return True
    elif board['UpperRight'] == 'O' and board['MiddleRight'] == 'O' and board['LowerRight'] == 'O':
        print("I win!")
        return True
    elif board['UpperLeft'] == 'O' and board['MiddleCenter'] == 'O' and board['LowerRight'] == 'O':
        print("I win!")
        return True
    elif board['UpperRight'] == 'O' and board['MiddleCenter'] == 'O' and board['LowerLeft'] == 'O':
        print("I win!")
        return True
    else:
        return False


# The computer "AI"
def AIdecisionMaker():
    res = key, val = random.choice(list(board.items()))
    #If val is E, then place, otherwise pick another spot
    while True:
        res = key, val = random.choice(list(board.items()))
        if val == 'E':
            return res[0]
            break

#-----------All functions above here -------------------------------------------


#Human is X, AI is O.
human = {'symbol': 'X'}
AI    = {'symbol': 'O'}

#E for empty
board = {'UpperLeft': 'E','UpperCenter': 'E','UpperRight': 'E',
         'MiddleLeft': 'E','MiddleCenter': 'E','MiddleRight': 'E',
         'LowerLeft': 'E','LowerCenter': 'E','LowerRight': 'E'}


greeting()
winCondition = False
grid = """
     {UpperLeft} || {UpperCenter} || {UpperRight}
    =============
     {MiddleLeft} || {MiddleCenter} || {MiddleRight}
    =============
     {LowerLeft} || {LowerCenter} || {LowerRight}
      """.format(**board)

printGrid(grid)

#main game loop
while(winCondition == False):
    getPlayerInput(human)
    grid = """
         {UpperLeft} || {UpperCenter} || {UpperRight}
        =============
         {MiddleLeft} || {MiddleCenter} || {MiddleRight}
        =============
         {LowerLeft} || {LowerCenter} || {LowerRight}
          """.format(**board)

    printGrid(grid)
    winCondition = checkForWinCondition()
    getPlayerInput(AI)
    grid = """
         {UpperLeft} || {UpperCenter} || {UpperRight}
        =============
         {MiddleLeft} || {MiddleCenter} || {MiddleRight}
        =============
         {LowerLeft} || {LowerCenter} || {LowerRight}
          """.format(**board)

    printGrid(grid)
    winCondition = checkForWinCondition()
