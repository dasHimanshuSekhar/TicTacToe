import random
from os import system

system('cls')

board = [1,2,3,4,5,6,7,8,9]

score_pc = 0
score_player = 0

def display_board(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[0],"  |  ",board[1],"  |  ",board[2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[3],"  |  ",board[4],"  |  ",board[5],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[6],"  |  ",board[7],"  |  ",board[8],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

def enter_move(board):
    i = int(input("Enter your move:"))
    flag = 1
    while flag:
        if board[i - 1] == "X" or board[i - 1] == "O" :
            print("Please ! Choose a empty position :)")
            i = int(input("Enter your move:"))
        else:
            board[i - 1] = "O"
            flag = 0

def victory_for(score_pc, score_player, name):
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game
    if score_pc > score_player:
        print("PC smashed You !!  :)")
    elif score_pc == score_player:
        print("TIE !!")
    else:
        print("CONGRAST.. ", name ," !! You Beat PC ! :)")


def score_cntr(board):
    global score_pc
    global score_player
    if ((board[0] == board[3]) and (board[3] == board[6]) and (board[6] == "X")):
        score_pc += 1
    if ((board[1] == board[4]) and (board[4] == board[7]) and (board[7] == "X")):
        score_pc += 1
    if ((board[2] == board[5]) and (board[5] == board[8]) and (board[8] == "X")):
        score_pc += 1
    if ((board[0] == board[1]) and (board[1] == board[2]) and (board[2] == "X")):
        score_pc += 1
    if ((board[3] == board[4]) and (board[4] == board[5]) and (board[5] == "X")):
        score_pc += 1
    if ((board[6] == board[7]) and (board[7] == board[8]) and (board[8] == "X")):
        score_pc += 1
    if ((board[0] == board[4]) and (board[4] == board[8]) and (board[8] == "X")):
        score_pc += 1
    if ((board[2] == board[4]) and (board[4] == board[6]) and (board[6] == "X")):
        score_pc += 1
    if ((board[0] == board[3]) and (board[3] == board[6]) and (board[6] == "O")):
        score_player += 1
    if ((board[1] == board[4]) and (board[4] == board[7]) and (board[7] == "O")):
        score_player += 1
    if ((board[2] == board[5]) and (board[5] == board[8]) and (board[8] == "O")):
        score_player += 1
    if ((board[0] == board[1]) and (board[1] == board[2]) and (board[2] == "O")):
        score_player += 1
    if ((board[3] == board[4]) and (board[4] == board[5]) and (board[5] == "O")):
        score_player += 1
    if ((board[6] == board[7]) and (board[7] == board[8]) and (board[8] == "O")):
        score_player += 1
    if ((board[0] == board[4]) and (board[4] == board[8]) and (board[8] == "O")):
        score_player += 1
    if ((board[2] == board[4]) and (board[4] == board[6]) and (board[6] == "O")):
        score_player += 1
    
    return

def draw_move(board):
    flag = 1
    i = random.randrange(1, 10)
    while flag:
        if board[i - 1] == "X" or board[i - 1] == "O":
            i = random.randrange(1, 10)
        else:
            board[i - 1] = "X"
            flag = 0

#------------------------------------------------------------------------------------------------------
#--------------------------------------------DRIVER CODE-----------------------------------------------
banner = "\n\t\t\t\t\t                   !! ~~~ TIC TAC TOE ~~~ !!                          \n"
print(banner)
name = input("Enter your name:")
display_board(board)
enter_move(board)
system('cls')
print(banner)
display_board(board)
draw_move(board)
system('cls')
print(banner)
display_board(board)
enter_move(board)
system('cls')
print(banner)
display_board(board)
draw_move(board)
system('cls')
print(banner)
display_board(board)
enter_move(board)
system('cls')
print(banner)
display_board(board)
draw_move(board)
system('cls')
print(banner)
display_board(board)
enter_move(board)
system('cls')
print(banner)
display_board(board)
draw_move(board)
system('cls')
print(banner)
display_board(board)
enter_move(board)
system('cls')
print(banner)
display_board(board)
score_cntr(board)
victory_for(score_pc, score_player, name)
system('pause')