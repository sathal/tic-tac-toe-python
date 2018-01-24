import sys

board = {'ul':' ', 'um':' ', 'ur':' ',
         'ml':' ', 'mm':' ', 'mr':' ',
         'll':' ', 'lm':' ', 'lr':' '}

# Draw the current state of the Tic Tac Toe Board
def drawBoard():
    print(" ")
    print(board['ul'] + "|" + board['um'] + "|" + board['ur'])
    print("_|_|_")
    print(board['ml'] + "|" + board['mm'] + "|" + board['mr'])
    print("_|_|_")
    print(board['ll'] + "|" + board['lm'] + "|" + board['lr'])

# Determine if the user would like to quit the game
def quitGame(move):
    if(move == "quit"):
        return True
    else:
        return False

# Check that the user input is valid input
def isValidMove(move):
    if(move not in board.keys()):
        return False
    else:
        return True

# Check that the move is placed on an available square
def isLegalMove(move):
    if(board[move] == ' '):
        return True
    else:
        return False

# Check to see if all of the spaces have been used
def isBlackout():
    if(' ' not in board.values()):
        return True
    else:
        return False

# Check to see if placing a character on UL completed the game
def assessUL(turn):
    if(turn == board['um'] == board['ur']):
        return True
    elif(turn == board['ml'] == board['ll']):
        return True
    elif(turn == board['mm'] == board['lr']):
        return True
    else:
        return False

# Check to see if placing a character on UM completed the game
def assessUM(turn):
    if(turn == board['ul'] == board['ur']):
        return True
    elif(turn == board['mm'] == board['lm']):
        return True
    else:
        return False

# Check to see if placing a character on UR completed the game
def assessUR(turn):
    if(turn == board['ul'] == board['um']):
        return True
    elif(turn == board['mr'] == board['lr']):
        return True
    elif(turn == board['mm'] == board['ll']):
        return True
    else:
        return False

# Check to see if placing a character on ML completed the game
def assessML(turn):
    if(turn == board['ul'] == board['ll']):
        return True
    elif(turn == board['mm'] == board['mr']):
        return True
    else:
        return False

# Check to see if placing a character on MM completed the game
def assessMM(turn):
    if(turn == board['um'] == board['lm']):
        return True
    elif(turn == board['ml'] == board['mr']):
        return True
    elif(turn == board['ul'] == board['lr']):
        return True
    elif(turn == board['ll'] == board['ur']):
        return True
    else:
        return False

# Check to see if placing a character on MR completed the game
def assessMR(turn):
    if(turn == board['ur'] == board['lr']):
        return True
    elif(turn == board['mm'] == board['ml']):
        return True
    else:
        return False

# Check to see if placing a character on LL completed the game
def assessLL(turn):
    if(turn == board['lm'] == board['lr']):
        return True
    elif(turn == board['ml'] == board['ul']):
        return True
    elif(turn == board['mm'] == board['ur']):
        return True
    else:
        return False

# Check to see if placing a character on LM completed the game
def assessLM(turn):
    if(turn == board['ll'] == board['lr']):
        return True
    elif(turn == board['mm'] == board['um']):
        return True
    else:
        return False

# Check to see if placing a character on LR completed the game
def assessLR(turn):
    if(turn == board['ll'] == board['lm']):
        return True
    elif(turn == board['mr'] == board['ur']):
        return True
    elif(turn == board['mm'] == board['ul']):
        return True
    else:
        return False

# Check to see if someone won, there is a blackout, or the game should continue
def gameComplete(move, turn):
    d = {'ul':assessUL(turn),
         'um':assessUM(turn),
         'ur':assessUR(turn),
         'ml':assessML(turn),
         'mm':assessMM(turn),
         'mr':assessMR(turn),
         'll':assessLL(turn),
         'lm':assessLM(turn),
         'lr':assessLR(turn)}

    # if game is assessed to be complete, then someone won
    if(d.get(move) == True):
        return True
    elif(isBlackout()):
        print("Cats! Its a draw!")
        sys.exit()
    else:
        return False

turn = "X"
otherTurn = "Y"

print("\nWelcome to Tic Tac Toe!")
print("Valid moves:")
print("\tul = Upper Left")
print("\tum = Upper Middle")
print("\tur = Upper Right")
print("\tml = Middle Left")
print("\tmm = Middle Middle")
print("\tmr = Middle Right")
print("\tll = Lower Left")
print("\tlm = Lower Middle")
print("\tlr = Lower Right")
print("\ttype \"quit\" to exit game")

while True:
    drawBoard()
    print(turn + "'s turn: ")
    move = raw_input()
    if(quitGame(move) == True):
        sys.exit()
    if(isValidMove(move) == False):
        print(move + " is not a valid move!")
        continue
    elif(isLegalMove(move) == False):
        print("Position " + move + " is already taken!")
        continue

    board[move] = turn
    if(gameComplete(move, turn)):
        drawBoard()
        print(turn + "'s won!")
        sys.exit()
    turn, otherTurn = otherTurn, turn
